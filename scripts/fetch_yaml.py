import json
import asyncio
import time
import logging
from pathlib import Path
from typing import Any
from tqdm.asyncio import tqdm as async_tqdm

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 配置参数
MAX_CONCURRENT_REQUESTS = 10  # 最大并发请求数
REQUEST_TIMEOUT = 30  # 请求超时时间（秒）
RETRY_COUNT = 3  # 重试次数
RETRY_DELAY = 2  # 重试延迟（秒）

# 基本路径配置
root = Path(__file__).parent.parent
api_tree_path = root / "data" / "api_tree.json"
yaml_output_path = root / "data" / "api_yaml_raw"  # 用于保存原始YAML数据
yaml_output_path.mkdir(exist_ok=True)

def build_e0_url(api_id: str) -> tuple[bool, str]:
    """构建API URL"""
    if not api_id.endswith("e0"):
        return False, ""
    
    base_url = "https://napcat.apifox.cn/"
    url = f"{base_url}/{api_id}.md"
    
    return True, url

def extract_yaml_from_markdown(markdown_content: str) -> str:
    """从Markdown内容中提取YAML代码块，处理可能包含嵌套代码块的情况
    
    Args:
        markdown_content: Markdown格式的内容
        
    Returns:
        提取的YAML内容，如果没有找到则返回空字符串
    """
    lines = markdown_content.split('\n')
    yaml_content = []
    in_yaml_block = False
    yaml_block_indent = 0
    nesting_level = 0
    
    logger.debug("开始解析Markdown内容以提取YAML")
    
    for line in lines:
        if not in_yaml_block:
            # 寻找YAML块的开始
            if line.strip().startswith("```yaml"):
                in_yaml_block = True
                yaml_block_indent = len(line) - len(line.lstrip())
                logger.debug(f"找到YAML块开始，缩进级别: {yaml_block_indent}")
                # 不添加开始标记行
                continue
        else:
            # 已经在YAML块内部
            stripped_line = line.strip()
            
            # 检测嵌套块的开始
            if stripped_line.startswith("```") and not stripped_line.startswith("```yaml"):
                nesting_level += 1
                logger.debug(f"检测到嵌套代码块开始，当前嵌套级别: {nesting_level}")
                yaml_content.append(line)
                continue
            
            # 检测嵌套块的结束
            if nesting_level > 0 and stripped_line == "```":
                nesting_level -= 1
                logger.debug(f"检测到嵌套代码块结束，当前嵌套级别: {nesting_level}")
                yaml_content.append(line)
                continue
            
            # 检测YAML块自身的结束（只有当不在嵌套块中时）
            if nesting_level == 0 and (stripped_line == "```" or stripped_line == '"""'):
                in_yaml_block = False
                logger.debug(f"找到YAML块结束标记: {stripped_line}")
                # 不添加结束标记行
                break
            
            # 正常的YAML内容行
            yaml_content.append(line)
    
    if not yaml_content:
        logger.warning("未找到完整的YAML代码块")
        return ""
    
    # 清理YAML内容结尾处的标记
    # 检查并移除最后几行可能的结束标记
    while yaml_content and (yaml_content[-1].strip() in ['"""', "```", "`", '```'] or yaml_content[-1].strip() == ''):
        # 注意：这里同时移除空行和各种结束标记
        logger.debug(f"移除YAML内容末尾的多余标记或空行: '{yaml_content[-1].strip()}'")
        yaml_content.pop()
    
    # 将多行内容合并为字符串
    result = "\n".join(yaml_content)
    
    # 再次检查结果中是否有尾部标记
    result = result.rstrip()
    if result.endswith('```') or result.endswith('"""'):
        logger.debug("在合并后的内容中检测到尾部标记，移除中...")
        if result.endswith('```'):
            result = result[:-3].rstrip()
        if result.endswith('"""'):
            result = result[:-3].rstrip()
    
    logger.debug(f"提取的YAML内容长度: {len(result)}")
    return result

def build_id_path_map(tree: dict, current_path: str = "") -> dict[str, str]:
    """递归构建API ID到路径的映射"""
    result: dict[str, str] = {}
    
    for key, value in tree.items():
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
                logger.debug(f"请求URL: {url}, 尝试次数: {attempt+1}")
                response = await client.get(url)
                status = response.status_code
                if (status == 200):
                    logger.debug(f"成功获取URL: {url}")
                    return True, response.text, status
                else:
                    # 特定错误码的处理
                    if status in (429, 503):  # 速率限制或服务不可用
                        retry_after = int(response.headers.get('Retry-After', RETRY_DELAY * (attempt + 1)))
                        logger.warning(f"请求限制，等待 {retry_after} 秒后重试: {url}")
                        await asyncio.sleep(retry_after)
                        continue
                    logger.error(f"HTTP错误: {status}, URL: {url}")
                    return False, f"HTTP错误: {status}", status
        except TimeoutError:
            if attempt < RETRY_COUNT:
                wait_time = RETRY_DELAY * (attempt + 1)
                logger.warning(f"请求超时，等待 {wait_time} 秒后重试: {url}")
                await asyncio.sleep(wait_time)  # 指数退避
            else:
                logger.error(f"请求最终超时: {url}")
                return False, "请求超时", 408
        except Exception as e:
            if attempt < RETRY_COUNT:
                wait_time = RETRY_DELAY * (attempt + 1)
                logger.warning(f"请求出错，等待 {wait_time} 秒后重试: {url}, 错误: {str(e)}")
                await asyncio.sleep(wait_time)
            else:
                logger.error(f"请求最终失败: {url}, 错误: {str(e)}")
                return False, f"获取失败: {str(e)}", 0
    
    return False, "达到最大重试次数", 0

async def fetch_api_yaml(client: Any, api_id: str, semaphore: asyncio.Semaphore) -> tuple[str, str]:
    """异步获取API文档并提取YAML"""
    _, url = build_e0_url(api_id)
    
    success, content, status = await fetch_with_retries(url, client, semaphore)
    
    if success:
        # 提取YAML内容
        yaml_content = extract_yaml_from_markdown(content)
        logger.info(f"成功获取API {api_id} 的YAML内容，长度: {len(yaml_content)}")
        return api_id, yaml_content
    else:
        logger.error(f"获取API {api_id} 失败: {content}")
        return api_id, ""

async def process_apis(api_ids: list[str]) -> dict[str, str]:
    """异步处理API ID列表，提取YAML内容"""
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    result: dict[str, str] = {}
    
    # 使用httpx
    try:
        import httpx
        limits = httpx.Limits(max_connections=MAX_CONCURRENT_REQUESTS, max_keepalive_connections=10)
        timeout = httpx.Timeout(REQUEST_TIMEOUT)
        
        async with httpx.AsyncClient(limits=limits, timeout=timeout) as client:
            tasks = []
            for api_id in api_ids:
                tasks.append(fetch_api_yaml(client, api_id, semaphore))
            
            if tasks:
                # 使用异步进度条
                results = await async_tqdm.gather(*tasks, desc="获取API文档")
                
                # 收集结果
                for api_id, yaml_content in results:
                    if yaml_content:  # 只保存有内容的结果
                        result[api_id] = yaml_content
                        
                        # 保存原始YAML到文件
                        yaml_file = yaml_output_path / f"{api_id}.yaml"
                        with open(yaml_file, "w", encoding="utf-8") as f:
                            f.write(yaml_content)
                            logger.debug(f"保存YAML到文件: {yaml_file}")
    except ImportError:
        logger.error("请安装httpx库: pip install httpx")
        raise
                    
    return result

async def main():
    print("开始处理API文档...")
    
    # 加载API树
    print("加载API树...")
    start_time = time.time()
    with open(api_tree_path, encoding="utf-8") as f:
        api_tree = json.load(f)
    
    # 构建ID映射
    print("构建API ID映射...")
    id_path_map = build_id_path_map(api_tree)
    
    # 保存ID到路径的映射
    id_index_path = root / "data" / "api_id_index.json"
    with open(id_index_path, 'w', encoding='utf-8') as f:
        json.dump(id_path_map, f, ensure_ascii=False, indent=2)
    
    print(f"API ID索引已保存至 {id_index_path} (耗时: {time.time() - start_time:.2f}秒)")
    
    # 筛选所有e0类型的API ID
    e0_api_ids = [api_id for api_id in id_path_map if api_id.endswith("e0")]
    print(f"找到 {len(e0_api_ids)} 个e0类型的API")
    
    # 处理所有API并获取YAML
    yaml_results = await process_apis(e0_api_ids)
    
    # 保存结果统计
    print(f"处理完成! 成功获取了 {len(yaml_results)} 个API的YAML内容")
    print(f"YAML原始数据已保存到 {yaml_output_path} 目录")
    
    # 可以添加一个简单的索引文件
    yaml_index = {
        "total": len(yaml_results),
        "api_ids": list(yaml_results.keys()),
        "timestamp": time.time()
    }
    
    with open(yaml_output_path / "index.json", "w", encoding="utf-8") as f:
        json.dump(yaml_index, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    asyncio.run(main())