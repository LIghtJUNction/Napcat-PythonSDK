import json
import asyncio
import re
import time
import yaml
from pathlib import Path
from typing import Any
from functools import lru_cache
from tqdm.asyncio import tqdm as async_tqdm

# 配置参数
SAVE_BATCH_SIZE = 20  # 每处理多少个API保存一次
MAX_CONCURRENT_REQUESTS = 10  # 最大并发请求数
REQUEST_TIMEOUT = 30  # 请求超时时间（秒）
RETRY_COUNT = 3  # 重试次数
RETRY_DELAY = 2  # 重试延迟（秒）

root = Path(__file__).parent.parent

api_tree_path = root / "data" / "api_tree.json"
endpoint_index = root / "data" / "endpoint_index.json"
endpoint_index.touch(exist_ok=True)

# 预编译正则表达式，提高重复使用效率
YAML_PATTERN = re.compile(r"```yaml\s+([\s\S]*?)\s+```")

@lru_cache(maxsize=128)
def build_e0_url(api_id: str) -> tuple[bool, str]:
    """构建API URL，并使用LRU缓存避免重复计算"""
    if not api_id.endswith("e0"):
        return False, ""
    
    base_url = "https://napcat.apifox.cn/"
    url = f"{base_url}/{api_id}.md"
    
    return True, url

def extract_yaml_from_markdown(markdown_content: str) -> str:
    """从Markdown内容中提取YAML代码块"""
    matches = YAML_PATTERN.findall(markdown_content)
    return matches[0] if matches else ""

def parse_api_doc(yaml_content: str) -> dict[str, Any]:
    """解析OpenAPI YAML文档并提取关键信息"""
    try:
        # 解析YAML内容
        api_spec = yaml.safe_load(yaml_content)
        
        # 提取基本信息
        result: dict[str, Any] = {
            "openapi_version": api_spec.get("openapi", ""),
            "info": {
                "title": api_spec.get("info", {}).get("title", ""),
                "description": api_spec.get("info", {}).get("description", ""),
                "version": api_spec.get("info", {}).get("version", "")
            },
            "endpoint": []
        }
        
        # 处理路径
        for path, path_item in api_spec.get("paths", {}).items():
            for method, operation in path_item.items():
                if method not in ["get", "post", "put", "delete", "patch"]:
                    continue
                
                endpoint: dict[str, Any] = {
                    "path": path,
                    "method": method.upper(),
                    "summary": operation.get("summary", ""),
                    "description": operation.get("description", ""),
                    "deprecated": operation.get("deprecated", False),
                    "tags": operation.get("tags", []),
                    "parameters": [],
                    "request_body": None,
                    "responses": {}
                }
                
                # 处理参数
                for param in operation.get("parameters", []):
                    endpoint["parameters"].append({
                        "name": param.get("name", ""),
                        "in": param.get("in", ""),
                        "description": param.get("description", ""),
                        "required": param.get("required", False),
                        "schema": param.get("schema", {})
                    })
                
                # 处理请求体
                request_body = operation.get("requestBody", {})
                if request_body:
                    content_type = next(iter(request_body.get("content", {})), None)
                    if content_type:
                        schema = request_body["content"][content_type].get("schema", {})
                        properties = schema.get("properties", {})
                        required = schema.get("required", [])
                        
                        req_body: dict[str, Any] = {
                            "content_type": content_type,
                            "required_fields": required,
                            "properties": {}
                        }
                        
                        # 提取属性
                        for prop_name, prop_schema in properties.items():
                            req_body["properties"][prop_name] = {
                                "type": prop_schema.get("type", ""),
                                "description": prop_schema.get("description", ""),
                                "required": prop_name in required
                            }
                        
                        endpoint["request_body"] = req_body
                
                # 处理响应
                for status_code, response in operation.get("responses", {}).items():
                    content_type = next(iter(response.get("content", {})), None)
                    if content_type:
                        schema = response["content"][content_type].get("schema", {})
                        
                        resp: dict[str, Any] = {
                            "description": response.get("description", ""),
                            "content_type": content_type,
                            "schema": extract_schema_properties(schema)
                        }
                        
                        endpoint["responses"][status_code] = resp
                
                result["endpoint"].append(endpoint)
        
        return result
    
    except Exception as e:
        return {"error": f"解析文档时出错: {str(e)}"}


def extract_schema_properties(schema: dict[str, Any]) -> dict[str, Any]:
    """递归提取schema属性"""
    result: dict[str, Any] = {
        "type": schema.get("type", "object"),
        "properties": {},
        "required": schema.get("required", [])
    }
    
    for prop_name, prop_schema in schema.get("properties", {}).items():
        if isinstance(prop_schema, dict):
            if "properties" in prop_schema:
                # 递归处理嵌套属性
                result["properties"][prop_name] = extract_schema_properties(prop_schema) # type: ignore
            else:
                # 直接属性
                result["properties"][prop_name] = {
                    "type": prop_schema.get("type", ""), # type: ignore
                    "description": prop_schema.get("description", ""), # type: ignore
                    "required": prop_name in result["required"]
                }
    
    return result


def build_id_path_map(tree: dict, current_path: str = "") -> dict[str, str]: # type: ignore
    """递归构建API ID到路径的映射"""
    result: dict[str, str] = {}
    
    for key, value in tree.items(): # type: ignore
        # 跳过非字典值
        if not isinstance(value, dict):
            continue
        
        # 构建此节点的路径
        path = f"{current_path}/{key}" if current_path else f"/{key}"
        
        # 如果有ID，则添加到映射
        if "id" in value:
            result[value["id"]] = path
        
        # 递归处理子节点并合并结果
        result.update(build_id_path_map(value, path))
    
    return result


async def fetch_with_retries(url: str, client: Any, semaphore: asyncio.Semaphore,
                            timeout: int = REQUEST_TIMEOUT) -> tuple[bool, str, int]:
    """使用重试逻辑获取URL内容"""
    for attempt in range(RETRY_COUNT + 1):
        try:
            async with semaphore:
                response = await client.get(url)
                status = response.status_code
                if status == 200:
                    return True, response.text, status
                else:
                    # 特定错误码的处理
                    if status in (429, 503):  # 速率限制或服务不可用
                        retry_after = int(response.headers.get('Retry-After', RETRY_DELAY * (attempt + 1)))
                        await asyncio.sleep(retry_after)
                        continue
                    return False, f"HTTP错误: {status}", status
        except TimeoutError:
            if attempt < RETRY_COUNT:
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))  # 指数退避
            else:
                return False, "请求超时", 408
        except Exception as e:
            if attempt < RETRY_COUNT:
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
            else:
                return False, f"获取失败: {str(e)}", 0
    
    return False, "达到最大重试次数", 0


async def fetch_api_doc(client: Any, api_id: str,
                        semaphore: asyncio.Semaphore) -> tuple[str, dict[str, Any] | None]:
    """异步获取API文档"""
    _, url = build_e0_url(api_id)
    
    success, content, status = await fetch_with_retries(url, client, semaphore) # type: ignore
    
    if success:
        # 提取并解析YAML内容
        yaml_content = extract_yaml_from_markdown(content)
        if not yaml_content:
            return api_id, None
            
        return api_id, parse_api_doc(yaml_content)
    else:
        return api_id, {"error": content}


async def process_api_batch(api_ids: list[str], endpoint_index_dict: dict[str, Any]) -> dict[str, Any]:
    """异步处理一批API ID"""
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    
    # 使用httpx
    try:
        import httpx
        limits = httpx.Limits(max_connections=MAX_CONCURRENT_REQUESTS, max_keepalive_connections=10)
        timeout = httpx.Timeout(REQUEST_TIMEOUT)
        
        async with httpx.AsyncClient(limits=limits, timeout=timeout) as client:
            tasks = []
            for api_id in api_ids:
                # 处理所有API
                tasks.append(fetch_api_doc(client, api_id, semaphore)) # type: ignore
            
            if tasks:
                # 使用异步进度条
                results = await async_tqdm.gather(*tasks, desc="构建endpoint index") # type: ignore
                
                # 更新索引字典
                for api_id, doc in results: # type: ignore
                    if doc is not None:
                        endpoint_index_dict[api_id] = doc
    except ImportError:
        print("请安装httpx库: pip install httpx")
        raise
                    
    return endpoint_index_dict


async def main():
    print("加载API树...")
    with open(api_tree_path, encoding="utf-8") as f:
        api_tree = json.load(f)
    
    print("构建ID反向索引...")
    start_time = time.time()
    
    # 使用优化后的函数构建ID映射
    id_path_map = build_id_path_map(api_tree)
    
    # 保存ID到路径的映射
    id_index_path = root / "data" / "api_id_index.json"
    with open(id_index_path, 'w', encoding='utf-8') as f:
        json.dump(id_path_map, f, ensure_ascii=False, indent=2)
    
    print(f"API ID索引已保存至 {id_index_path} (耗时: {time.time() - start_time:.2f}秒)")
    
    print("构建endpoint索引...")
    
    # 加载现有索引
    endpoint_index_dict: dict[str, Any] = {}
    if endpoint_index.exists() and endpoint_index.stat().st_size > 0:
        try:
            with open(endpoint_index, encoding='utf-8') as f:
                endpoint_index_dict = json.load(f)
            print(f"已加载现有索引，包含 {len(endpoint_index_dict)} 个API")
        except json.JSONDecodeError:
            print("现有索引文件格式错误，将重新创建")
    
    # 筛选所有e0类型的API ID
    e0_api_ids = [api_id for api_id in id_path_map if api_id.endswith("e0")]
    
    print(f"找到 {len(e0_api_ids)} 个e0类型的API")
    
    # 强制处理所有e0 API，无论是否已在索引中
    to_process = e0_api_ids
    print(f"强制处理 {len(to_process)} 个API")
    
    # 分批处理API
    batch_size = 50  # 每批处理的API数量
    
    try:
        for i in range(0, len(to_process), batch_size):
            batch = to_process[i:i + batch_size]
            endpoint_index_dict = await process_api_batch(batch, endpoint_index_dict)
            
            # 每次处理完批次后强制保存进度
            with open(endpoint_index, 'w', encoding='utf-8') as f:
                json.dump(endpoint_index_dict, f, ensure_ascii=False, indent=2)
            print(f"进度保存：已处理 {len(endpoint_index_dict)} 个API")
        
        # 完成后保存最终结果
        with open(endpoint_index, 'w', encoding='utf-8') as f:
            json.dump(endpoint_index_dict, f, ensure_ascii=False, indent=2)
        
        print(f"索引构建完成! 总共索引了 {len(endpoint_index_dict)} 个API，已保存至 {endpoint_index}")
    
    except KeyboardInterrupt:
        # 如果用户中断，仍然保存已处理的结果
        print("\n用户中断处理，保存已处理的索引...")
        with open(endpoint_index, 'w', encoding='utf-8') as f:
            json.dump(endpoint_index_dict, f, ensure_ascii=False, indent=2)
        print(f"已保存 {len(endpoint_index_dict)} 个API的索引")

# 运行异步主函数
if __name__ == "__main__":
    asyncio.run(main())