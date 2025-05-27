"""
Pydantic模型生成模块

提供将JSON Schema转换为Pydantic模型的核心功能
"""
import logging
from typing import Any

from pydantic import BaseModel

from build.schema_parser import (
    is_empty_schema,
    parse_property_type,
    sanitize_field_name
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ModelParts(BaseModel):
    """存储生成的模型代码片段"""
    imports: set[str] = set()
    req: str = ""
    res: str = ""
    api: str = ""
    component_models: list[str] = []


def process_schema_component(
    schema: dict[str, Any], 
    schema_name: str, 
    imports: set[str]
) -> str:
    """
    处理Schema组件，生成Pydantic模型代码
    
    Args:
        schema: JSON Schema组件
        schema_name: 模型名称
        imports: 导入语句集合，会被修改
        
    Returns:
        生成的Pydantic模型代码
    """
    logger.debug(f"处理模型: {schema_name}")
    
    # 检查Schema是否为空或只包含元数据
    if is_empty_schema(schema):
        logger.warning(f"跳过空模型: {schema_name}")
        return ""
    
    # 确保导入Field
    imports.add("from pydantic import BaseModel, Field")
    
    model_code = []
    model_code.append(f"class {schema_name}(BaseModel):")
    
    # 添加类级别注释
    if "description" in schema and schema["description"]:
        description = schema["description"].strip().replace("\n", " ")
        model_code.append(f'    """{description}"""')
    
    properties = schema.get("properties", {})
    required_fields = schema.get("required", [])
    
    if not properties:
        # 对于没有属性的模型，使用合理的默认类型并添加Field描述
        if schema.get("type") == "string":
            model_code.append("    value: str = Field(description=\"字符串值\")")
        elif schema.get("type") == "integer":
            model_code.append("    value: int = Field(description=\"整数值\")")
        elif schema.get("type") == "number":
            model_code.append("    value: float = Field(description=\"浮点数值\")")
        else:
            # 若没有明确类型，使用id和名称作为通用字段
            model_code.append("    id: str = Field(description=\"标识ID\")")
            model_code.append("    name: str | None = Field(None, description=\"名称\")")
    else:
        # 处理所有属性
        for prop_name, prop_schema in properties.items():
            # 清理字段名
            clean_prop_name = sanitize_field_name(prop_name)
            
            # 获取字段类型和额外导入
            type_str, type_imports = parse_property_type(prop_schema, prop_name)
            if type_imports:
                for imp in type_imports.split("\n"):
                    if imp.strip():
                        imports.add(imp.strip())
            
            # 确定是否为必填字段
            is_required = prop_name in required_fields
            
            # 获取字段描述
            field_doc = ""
            if "description" in prop_schema and prop_schema["description"]:
                field_doc = prop_schema["description"].strip().replace("\n", " ")
            
            # 生成字段代码 - 始终使用Field添加描述
            field_params = []
            
            # 如果原始名称与清理后的名称不同，添加别名
            if clean_prop_name != prop_name:
                field_params.append(f'alias="{prop_name}"')
                
            # 添加描述参数
            if field_doc:
                field_params.append(f'description="{field_doc}"')
            
            # 根据必填状态处理字段
            if is_required:
                if field_params:
                    field_line = f"    {clean_prop_name}: {type_str} = Field({', '.join(field_params)})"
                else:
                    # 如果没有其他参数但有描述，添加一个通用描述
                    field_line = f"    {clean_prop_name}: {type_str} = Field(description=\"{clean_prop_name}字段\")"
            else:
                # 非必填字段，添加None默认值
                field_line = f"    {clean_prop_name}: {type_str} | None"
                if field_params:
                    field_line += f" = Field(None, {', '.join(field_params)})"
                else:
                    field_line += f" = Field(None, description=\"{clean_prop_name}字段\")"
            
            model_code.append(field_line)
    
    # 添加模型配置
    model_code.append("")
    model_code.append("    model_config = {")
    model_code.append('        "extra": "allow",')
    
    # 添加别名映射 - 仅在未使用Field别名时才需要
    field_aliases = []
    for prop_name in properties:
        clean_name = sanitize_field_name(prop_name)
        if clean_name != prop_name:
            field_aliases.append(f'            "{clean_name}": "{prop_name}"')
    
    if field_aliases:
        model_code.append('        "aliases": {')
        model_code.append(",\n".join(field_aliases))
        model_code.append("        },")
    
    model_code.append("    }")
    
    return "\n".join(model_code)


def get_components_from_openapi(openapi_schema: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """
    从OpenAPI文档提取组件Schema
    
    Args:
        openapi_schema: OpenAPI文档
        
    Returns:
        组件名称到Schema的映射
    """
    logger.debug("从OpenAPI提取组件Schema")
    
    components = {}
    
    # 标准OpenAPI结构中的组件
    if "components" in openapi_schema and "schemas" in openapi_schema["components"]:
        components = openapi_schema["components"]["schemas"]
        logger.debug(f"从standard components/schemas提取了{len(components)}个组件")
    
    # 处理其他可能的组件位置
    elif "definitions" in openapi_schema:
        components = openapi_schema["definitions"]
        logger.debug(f"从definitions提取了{len(components)}个组件")
    
    # 添加req/res结构中定义的组件
    if "paths" in openapi_schema:
        for path, path_item in openapi_schema["paths"].items():
            for method in ["post", "get"]:
                if method not in path_item:
                    continue
                
                method_info = path_item[method]
                
                # 检查请求参数
                if "parameters" in method_info:
                    for param in method_info["parameters"]:
                        if "schema" in param and param.get("name"):
                            param_name = param["name"]
                            if param_name not in components:
                                components[param_name] = param["schema"]
                                logger.debug(f"添加请求参数Schema: {param_name}")
                
                # 检查请求体schema
                if "requestBody" in method_info and "content" in method_info["requestBody"]:
                    for content_type, content in method_info["requestBody"]["content"].items():
                        if "schema" in content and "properties" in content["schema"]:
                            schema = content["schema"]
                            for prop_name, prop_schema in schema["properties"].items():
                                if is_empty_schema(prop_schema):
                                    continue
                                if prop_name not in components and "type" in prop_schema and prop_schema["type"] == "object":
                                    components[prop_name] = prop_schema
                                    logger.debug(f"添加请求体属性Schema: {prop_name}")
    
    return components


def process_request_schema(
    path_schema: dict[str, Any], 
    model_name: str, 
    imports: set[str]
) -> str:
    """
    处理API请求Schema，生成请求模型代码
    
    Args:
        path_schema: 路径Schema
        model_name: 模型名称
        imports: 导入语句集合，会被修改
        
    Returns:
        生成的请求模型代码
    """
    logger.debug(f"处理请求模型: {model_name}")
    
    # 获取请求体Schema
    request_schema = None
    description = ""
    
    # 查找POST或GET方法
    for method in ["post", "get"]:
        if method in path_schema:
            method_info = path_schema[method]
            description = method_info.get("summary", "") or method_info.get("description", "")
            
            # 检查请求体
            if "requestBody" in method_info and "content" in method_info["requestBody"]:
                for content_type, content in method_info["requestBody"]["content"].items():
                    if "schema" in content:
                        request_schema = content["schema"]
                        logger.debug(f"找到{method.upper()}请求体Schema: {content_type}")
                        break
            
            # 处理参数
            if "parameters" in method_info and not request_schema:
                # 创建一个模拟schema来表示所有参数
                request_schema = {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
                
                for param in method_info["parameters"]:
                    if "name" in param and "schema" in param:
                        param_name = param["name"]
                        param_schema = param["schema"]
                        request_schema["properties"][param_name] = param_schema
                        
                        if param.get("required", False):
                            request_schema["required"].append(param_name)
                
                logger.debug(f"从{len(method_info['parameters'])}个参数创建了请求Schema")
            
            break
    
    # 如果没有找到请求Schema，创建一个空的
    if not request_schema:
        logger.debug(f"未找到请求Schema，使用空对象")
        request_schema = {"type": "object", "properties": {}}
    
    # 增加导入
    imports.add("from pydantic import BaseModel, Field")
    
    # 创建请求模型代码
    req_code = [f"class {{{{EndPointReq}}}}(BaseModel):"]
    
    # 添加注释
    if description:
        req_code.append(f'    """{description.strip()}"""')
    
    # 处理请求体属性
    properties = request_schema.get("properties", {})
    required_fields = request_schema.get("required", [])
    
    if not properties:
        req_code.append("    pass  # 没有请求参数")
    else:
        for prop_name, prop_schema in properties.items():
            # 清理字段名
            clean_prop_name = sanitize_field_name(prop_name)
            
            # 获取字段类型和额外导入
            type_str, type_imports = parse_property_type(prop_schema, prop_name)
            if type_imports:
                for imp in type_imports.split("\n"):
                    if imp.strip():
                        imports.add(imp.strip())
            
            # 确定是否为必填字段
            is_required = prop_name in required_fields
            
            # 获取字段描述
            field_doc = prop_schema.get("description", "").strip() if "description" in prop_schema else ""
            
            # 生成字段代码 - 始终使用Field处理所有属性
            field_params = []
            
            # 添加别名
            if clean_prop_name != prop_name:
                field_params.append(f'alias="{prop_name}"')
            
            # 添加描述
            if field_doc:
                field_params.append(f'description="{field_doc}"')
            
            # 处理默认值和必填状态
            if is_required:
                field_line = f"    {clean_prop_name}: {type_str}"
                if field_params:
                    field_line += f" = Field({', '.join(field_params)})"
            else:
                field_line = f"    {clean_prop_name}: {type_str} | None"
                field_params.insert(0, "None")  # 添加默认值为None
                field_line += f" = Field({', '.join(field_params)})"
            
            req_code.append(field_line)
    
    # 添加模型配置
    req_code.append("")
    req_code.append("    model_config = {")
    req_code.append('        "extra": "allow",')
    
    # 添加别名映射 - 这部分可以移除，因为现在使用Field处理别名
    field_aliases = []
    for prop_name in properties:
        clean_name = sanitize_field_name(prop_name)
        if clean_name != prop_name:
            field_aliases.append(f'            "{clean_name}": "{prop_name}"')
    
    if field_aliases:
        req_code.append('        "aliases": {')
        req_code.append(",\n".join(field_aliases))
        req_code.append("        },")
    
    req_code.append("    }")
    
    return "\n".join(req_code)


def process_response_schema(
    path_schema: dict[str, Any], 
    model_name: str, 
    imports: set[str]
) -> str:
    """
    处理API响应Schema，生成响应模型代码
    
    Args:
        path_schema: 路径Schema
        model_name: 模型名称
        imports: 导入语句集合，会被修改
        
    Returns:
        生成的响应模型代码
    """
    logger.debug(f"处理响应模型: {model_name}")
    
    # 用于收集嵌套对象 - 使用字典以避免重复
    nested_objects: dict[str, dict[str, Any]] = {}
    
    # 获取响应体Schema
    response_schema = None
    description = ""
    
    # 查找POST或GET方法
    for method in ["post", "get"]:
        if method in path_schema:
            method_info = path_schema[method]
            description = method_info.get("summary", "") or method_info.get("description", "")
            
            # 检查响应体
            if "responses" in method_info:
                for status_code, response in method_info["responses"].items():
                    if status_code.startswith("2") and "content" in response:
                        for content_type, content in response["content"].items():
                            if "schema" in content:
                                response_schema = content["schema"]
                                logger.debug(f"找到{status_code} {method.upper()}响应体Schema: {content_type}")
                                break
                        if response_schema:
                            break
            
            # 检查请求体，也可能包含需要处理的嵌套类型
            if "requestBody" in method_info and "content" in method_info["requestBody"]:
                for content_type, content in method_info["requestBody"]["content"].items():
                    if "schema" in content and "properties" in content["schema"]:
                        req_schema = content["schema"]
                        for prop_name, prop_schema in req_schema.get("properties", {}).items():
                            # 处理请求体中的数组类型，可能包含嵌套对象
                            if prop_schema.get("type") == "array" and "items" in prop_schema:
                                items_schema = prop_schema["items"]
                                if items_schema.get("type") == "object":
                                    item_class_name = f"{prop_name.capitalize()}Item"
                                    nested_objects[item_class_name] = items_schema
                                    
                            # 处理复杂对象类型
                            if (prop_schema.get("type") == "object" and "properties" in prop_schema):
                                class_name = create_class_name(prop_name)
                                nested_objects[class_name] = prop_schema
            
            break
    
    # 如果没有找到响应Schema，创建一个默认的
    if not response_schema:
        logger.debug(f"未找到响应Schema，使用默认响应结构")
        response_schema = {
            "type": "object",
            "properties": {
                "status": {"type": "string", "description": "状态，如 'ok'"},
                "retcode": {"type": "number", "description": "返回码，0表示成功"},
                "data": {"type": "object", "description": "响应数据"},
                "message": {"type": "string", "description": "消息"},
                "wording": {"type": "string", "description": "文字描述"},
                "echo": {"type": "string", "description": "回显内容"}
            }
        }
    
    # 增加导入
    imports.add("from pydantic import BaseModel, Field")
    
    # 创建响应模型代码
    res_code = []
    
    # 添加主响应模型
    res_code.append(f"class {{{{EndPointRes}}}}(BaseModel):")
    
    # 添加注释
    if description:
        res_code.append(f'    """{description.strip()}"""')
    else:
        res_code.append(f'    """响应模型"""')
        
    # 始终定义Data作为内部类，即使没有data字段也默认创建
    # 这样可以避免外部引用找不到Data类型的问题
    data_schema = None
    if "properties" in response_schema and "data" in response_schema["properties"]:
        data_schema = response_schema["properties"]["data"]
    
    # 定义Data类
    res_code.append("    class Data(BaseModel):")
    res_code.append('        """响应数据类型"""')
    
    # 处理Data属性
    if data_schema and data_schema.get("type") == "object" and "properties" in data_schema:
        for prop_name, prop_schema in data_schema["properties"].items():
            # 获取字段描述
            field_doc = prop_schema.get("description", "").strip() if "description" in prop_schema else ""
            if not field_doc:
                field_doc = f"{prop_name}字段"
            
            # 获取类型
            type_str, _ = parse_property_type(prop_schema, prop_name)
            
            # 生成字段定义
            res_code.append(f"        {prop_name}: {type_str} = Field(default=None, description=\"{field_doc}\")")
    else:
        # 默认属性 - 确保至少有一些合理的属性
        res_code.append("        yes: bool = Field(default=True, description=\"是否可用\")")
        res_code.append("        reason: str | None = Field(default=None, description=\"原因\")")
    
    # 添加Data模型配置
    res_code.append("")
    res_code.append("        model_config = {")
    res_code.append('            "extra": "allow",')
    res_code.append("        }")
    res_code.append("")
    
    # 处理其他嵌套对象，将它们定义为内部类
    nested_classes_code = []
    for class_name, obj_schema in nested_objects.items():
        # 跳过Data，因为已单独处理
        if class_name == "Data":
            continue
            
        nested_class_code = []
        # 添加类定义
        nested_class_code.append(f"    class {class_name}(BaseModel):")
        
        # 添加类文档
        if "description" in obj_schema and obj_schema["description"]:
            obj_description = obj_schema["description"].strip().replace("\n", " ")
            nested_class_code.append(f'        """{obj_description}"""')
        else:
            nested_class_code.append(f'        """{class_name}类型"""')
        
        # 处理对象属性
        properties = obj_schema.get("properties", {})
        required_fields = obj_schema.get("required", [])
        
        if not properties:
            nested_class_code.append("        pass")
        else:
            for prop_name, prop_schema in properties.items():
                # 清理字段名
                clean_prop_name = sanitize_field_name(prop_name)
                
                # 获取字段类型和额外导入
                type_str, type_imports = parse_property_type(prop_schema, prop_name)
                if type_imports:
                    for imp in type_imports.split("\n"):
                        if imp.strip():
                            imports.add(imp.strip())
                
                # 确定是否为必填字段
                is_required = prop_name in required_fields
                
                # 获取字段描述
                field_doc = prop_schema.get("description", "").strip() if "description" in prop_schema else ""
                if not field_doc:
                    field_doc = f"{clean_prop_name}字段"
                
                # 生成字段代码 - 始终使用Field添加描述和默认值
                field_params = []
                
                # 添加默认值
                field_params.append("default=None")
                
                # 添加别名
                if clean_prop_name != prop_name:
                    field_params.append(f'alias="{prop_name}"')
                
                # 添加描述
                field_params.append(f'description="{field_doc}"')
                
                # 处理字段类型和默认值
                if is_required:
                    field_line = f"        {clean_prop_name}: {type_str}"
                else:
                    field_line = f"        {clean_prop_name}: {type_str} | None"
                
                field_line += f" = Field({', '.join(field_params)})"
                nested_class_code.append(field_line)
        
        # 添加模型配置
        nested_class_code.append("")
        nested_class_code.append("        model_config = {")
        nested_class_code.append('            "extra": "allow",')
        nested_class_code.append("        }")
        nested_class_code.append("")
        
        # 添加到嵌套类定义集合
        nested_classes_code.extend(nested_class_code)
    
    # 添加其他嵌套类
    if nested_classes_code:
        res_code.extend(nested_classes_code)
    
    # 处理响应体属性
    properties = response_schema.get("properties", {})
    required_fields = response_schema.get("required", [])
    
    if not properties:
        # 使用Field定义标准字段
        res_code.append("    status: str = Field(default=\"ok\", description=\"状态，如 'ok'\")")
        res_code.append("    retcode: float = Field(default=0, description=\"返回码，0表示成功\")")
        res_code.append("    data: Data = Field(default_factory=lambda: Data(), description=\"响应数据\")")
        res_code.append("    message: str = Field(default=\"\", description=\"消息\")")
        res_code.append("    wording: str = Field(default=\"\", description=\"文字描述\")")
        res_code.append("    echo: str | None = Field(default=None, description=\"回显内容\")")
    else:
        for prop_name, prop_schema in properties.items():
            # 清理字段名
            clean_prop_name = sanitize_field_name(prop_name)
            
            # 获取字段类型和额外导入
            type_str, type_imports = parse_property_type(prop_schema, prop_name)
            if type_imports:
                for imp in type_imports.split("\n"):
                    if imp.strip():
                        imports.add(imp.strip())
            
            # 如果是data字段，使用Data类型
            if prop_name == "data":
                type_str = "Data"
            
            # 确定是否为必填字段
            is_required = prop_name in required_fields
            
            # 获取字段描述
            field_doc = prop_schema.get("description", "").strip() if "description" in prop_schema else ""
            if not field_doc:
                field_doc = f"{clean_prop_name}字段"
            
            # 生成字段代码 - 始终使用Field处理所有属性
            field_params = []
            
            # 添加默认值
            if prop_name == "status":
                field_params.append("default=\"ok\"")
            elif prop_name == "retcode":
                field_params.append("default=0")
            elif prop_name == "data":
                field_params.append("default_factory=lambda: Data()")
            elif prop_name == "message" or prop_name == "wording":
                field_params.append("default=\"\"")
            else:
                field_params.append("default=None")
            
            # 添加别名
            if clean_prop_name != prop_name:
                field_params.append(f'alias="{prop_name}"')
            
            # 添加描述
            field_params.append(f'description="{field_doc}"')
            
            # 处理字段类型
            if is_required and prop_name not in ["echo"]:
                field_line = f"    {clean_prop_name}: {type_str}"
            else:
                # 对于可能为空的字段，添加None类型
                if not type_str.endswith(" | None") and prop_name in ["echo"]:
                    field_line = f"    {clean_prop_name}: {type_str} | None"
                else:
                    field_line = f"    {clean_prop_name}: {type_str}"
            
            field_line += f" = Field({', '.join(field_params)})"
            res_code.append(field_line)
    
    # 添加模型配置
    res_code.append("")
    res_code.append("    model_config = {")
    res_code.append('        "extra": "allow",')
    res_code.append("    }")
    
    return "\n".join(res_code)


def process_api_class(
    path: str, 
    method_info: dict[str, Any], 
    imports: set[str]
) -> str:
    """
    生成API类代码，从模板文件中提取API类模板，并添加对请求和响应类的引用
    
    Args:
        path: API路径
        method_info: 方法信息
        imports: 导入语句集合，会被修改
        
    Returns:
        生成的API类代码
        
    Raises:
        ValueError: 当无法从模板文件获取API区域时抛出
    """
    from pathlib import Path
    from build.utils import get_template, get_region
    
    logger.debug(f"处理API类: {path}")
    
    # 添加常用导入
    imports.add("from pydantic import BaseModel")
    imports.add("import logging")
    
    # 获取API描述
    description = method_info.get("summary", "") or method_info.get("description", "")
    
    # 获取HTTP方法
    http_method = "POST"  # 默认值
    for method in ["post", "get"]:
        if method in method_info:
            http_method = method.upper()
            break
    
    # 从模板文件获取API类模板
    try:
        template = get_template()
        # 提取API类区域作为模板
        api_template = get_region(template, "api")
        
        if not api_template:
            # 如果无法获取API模板区域，直接抛出错误
            error_msg = "从模板中获取API区域失败，请确保api.py模板文件中包含正确的'# region api'和'# region api/'区域标记"
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        logger.debug(f"使用API类模板: {api_template[:100]}...")
        
        # 替换路径和HTTP方法
        api_code = api_template.replace("{{endpoint}}", path.lstrip("/"))
        api_code = api_code.replace("{{method}}", http_method)
        
        return api_code
    except Exception as e:
        # 出现错误时，记录错误并抛出，不使用默认模板
        error_msg = f"读取API类模板失败: {e}"
        logger.error(error_msg)
        raise ValueError(error_msg)


def generate_pydantic_models(api_data: dict[str, Any]) -> ModelParts:
    """
    从API JSON数据中生成Pydantic模型代码
    
    Args:
        api_data: API JSON数据
        
    Returns:
        ModelParts对象，包含生成的所有代码部分
    """
    logger.debug("开始生成Pydantic模型")
    
    # 初始化结果
    model_parts = ModelParts()
    
    # 首先解析组件，以便生成引用模型
    components = get_components_from_openapi(api_data)
    processed_components = set()
    valid_component_models = []
    
    # 处理路径
    if "paths" in api_data:
        for path, path_item in api_data["paths"].items():
            # 处理请求模型
            req_code = process_request_schema(path_item, "EndPointReq", model_parts.imports)
            model_parts.req = req_code
            
            # 处理响应模型
            res_code = process_response_schema(path_item, "EndPointRes", model_parts.imports)
            model_parts.res = res_code
            
            # 处理API类
            for method in ["post", "get"]:
                if method in path_item:
                    api_code = process_api_class(path, path_item, model_parts.imports)
                    model_parts.api = api_code
                    break
            
            # 通常只处理第一个路径，因为我们通常一个文件只处理一个API
            break
    else:
        logger.warning("API数据中没有paths字段")
        model_parts.req = "class {{EndPointReq}}(BaseModel):\n    pass  # 没有请求参数"
        model_parts.res = "class {{EndPointRes}}(BaseModel):\n    status: str\n    retcode: float\n    data: dict[str, Any]\n    message: str\n    wording: str\n    echo: str | None = None"
        model_parts.api = "class {{EndPointAPI}}(BaseModel):\n    endpoint = \"unknown\"\n    method = \"POST\"\n\n    def __init__(self) -> None:\n        super().__init__()\n\n    def __call__(self, req: {{EndPointReq}}) -> {{EndPointRes}}:\n        return {{EndPointRes}}.model_validate(response)"
    
    # 处理组件模型
    for component_name, component_schema in components.items():
        if component_name not in processed_components:
            # 生成组件模型代码
            component_code = process_schema_component(
                component_schema, component_name, model_parts.imports
            )
            # 只添加非空组件
            if component_code:
                valid_component_models.append(component_code)
            processed_components.add(component_name)
    
    # 保存有效的组件模型
    model_parts.component_models = valid_component_models
    logger.debug(f"成功生成 {len(valid_component_models)} 个有效组件模型")
    
    return model_parts