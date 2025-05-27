"""
Schema解析模块

提供将JSON Schema转换为Python类型的功能，处理类型推断 and 解析，支持嵌套对象类型
"""
import json
import logging
import re
from pathlib import Path
from typing import Any, TypedDict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 加载中英文映射表
try:
    root = Path(__file__).parent.parent
    zh2en_path = root / "data" / "zh2en.json"
    if (zh2en_path.exists()):
        with open(zh2en_path, "r", encoding="utf-8") as f:
            ZH2EN_MAP = json.load(f)
        logger.debug(f"成功加载中文映射文件，包含 {len(ZH2EN_MAP)} 条映射")
    else:
        logger.warning(f"未找到中文映射文件: {zh2en_path}")
        ZH2EN_MAP = {}
except Exception as e:
    logger.error(f"加载中文映射文件失败: {e}")
    ZH2EN_MAP = {}


# 用于跟踪嵌套对象类型的数据结构
class NestedObjectInfo(TypedDict):
    """存储嵌套对象信息的类型"""
    name: str
    schema: dict[str, Any]


def sanitize_field_name(name: str) -> str:
    """
    清理字段名，确保它是有效的Python标识符
    
    Args:
        name: 原始字段名
        
    Returns:
        清理后的字段名
    """
    # 如果字段名是Python关键字，添加下划线后缀
    python_keywords = {"and", "as", "assert", "async", "await", "break", "class", "continue", 
                      "def", "del", "elif", "else", "except", "False", "finally", "for", 
                      "from", "global", "if", "import", "in", "is", "lambda", "None", 
                      "nonlocal", "not", "or", "pass", "raise", "return", "True", 
                      "try", "while", "with", "yield"}
    
    # 确保处理以点号 or 其他特殊字符开头的情况
    if name and (name[0] == '.' or not name[0].isalpha() and name[0] != '_'):
        logger.debug(f"字段名以特殊字符开头: '{name}'，添加前置下划线")
        name = name.lstrip('.') # 删除前导点号
        if not name:
            return "field"  # 如果只是点号，返回默认名称
    
    # 替换非法字符为下划线
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    
    # 确保字段名不以数字开头
    if sanitized and sanitized[0].isdigit():
        sanitized = f"_{sanitized}"
    
    # 如果是空字符串 or 只有下划线，使用默认名称
    if not sanitized or sanitized.strip('_') == '':
        sanitized = "field"
    
    # 如果是Python关键字，添加下划线后缀
    if sanitized in python_keywords:
        sanitized += "_"
    
    return sanitized


def create_class_name(base_name: str) -> str:
    """
    从基础名称创建有效的类名，将中文名称转换为英文类名
    
    Args:
        base_name: 基础名称
        
    Returns:
        规范化的英文类名
    """
    # 处理中文类名 - 先查找完整匹配
    if base_name in ZH2EN_MAP:
        en_name = ZH2EN_MAP[base_name]
        # 如果映射值是首字母大写的类名形式，直接使用
        if en_name and en_name[0].isupper():
            logger.debug(f"将中文类名 '{base_name}' 映射为英文 '{en_name}'")
            return en_name
        # 否则转为驼峰命名
        else:
            words = en_name.split('_')
            class_name = ''.join(word.capitalize() for word in words)
            logger.debug(f"将中文类名 '{base_name}' 映射并转换为驼峰式 '{class_name}'")
            return class_name
    
    # 检查是否包含中文字符
    if any('\u4e00' <= c <= '\u9fff' for c in base_name):
        # 如果包含中文但不in 映射表中，尝试部分匹配
        for zh, en in ZH2EN_MAP.items():
            if zh in base_name and zh != "// 数据类型映射":  # 忽略注释项
                # 使用对应的英文名称
                if en and en[0].isupper():
                    logger.debug(f"部分匹配中文名 '{base_name}' 中的 '{zh}' 转换为 '{en}'")
                    return en
        
        # 如果仍未找到映射，使用通用名称，并记录为未映射的中文类名
        logger.warning( f"发现未映射的中文类名: {base_name}")
        
        # 基于中文名称猜测合适的英文名
        if "数据" in base_name:
            return "DataItem"
        elif "列表" in base_name:
            return "ListItem" 
        elif "信息" in base_name or "详情" in base_name:
            return "InfoItem"
        elif "分组" in base_name or "分类" in base_name:
            return "Category"
        elif "配置" in base_name or "设置" in base_name:
            return "Config"
        elif "结果" in base_name:
            return "Result"
        elif "项" in base_name:
            return "Item"
        else:
            return "GenericItem"
    
    # 如果不是中文名称，将名称转换为驼峰式命名
    words = re.split(r'[-_\s]', base_name)
    class_name = ''.join(word.capitalize() for word in words if word)
    
    # 确保类名以字母开头且不为空
    if not class_name or not class_name[0].isalpha():
        class_name = "Model" + class_name
    
    # 特殊处理常见的类名
    if class_name.lower() == "data":
        class_name = "ResponseData"
    elif class_name.lower() == "item" or class_name.lower() == "items":
        class_name = "DataItem"
    elif class_name.lower() == "list":
        class_name = "DataList"
    
    return class_name


def is_empty_schema(schema: dict[str, Any]) -> bool:
    """
    检查Schema是否为空（没有有效的类型定义）
    
    Args:
        schema: JSON Schema对象
        
    Returns:
        如果Schema为空则为True
    """
    # 检查是否缺少类型定义 and 属性
    if not schema:
        return True
    
    # 检查常见的类型定义字段是否存in 
    type_fields = ["type", "properties", "items", "$ref", "oneOf", "anyOf", "allOf"]
    has_type_def = any(field in schema for field in type_fields)
    
    # 如果Schema只有描述 or 标题等元数据字段，也认为是空的
    metadata_only = all(k in ["description", "title", "example"] for k in schema.keys())
    
    return not has_type_def or metadata_only


def infer_type_from_schema(
    schema: dict[str, Any], 
    field_name: str = "", 
    nested_objects: list[NestedObjectInfo] | None = None
) -> tuple[str, str]:
    """
    从JSON Schema推断Python类型，同时收集嵌套对象信息
    
    Args:
        schema: JSON Schema对象
        field_name: 字段名，用于生成更好的类名
        nested_objects: 收集嵌套对象的列表，如果为None则不收集
        
    Returns:
        元组 (类型字符串, 附加导入语句)
    """
    # 初始化返回值
    python_type = "Any"
    imports = ""
    
    logger.debug(f"开始推断字段 {field_name} 的类型: {schema.get('type', '未指定')}")
    
    # 处理空Schema
    if is_empty_schema(schema):
        logger.debug(f"字段 {field_name} 的Schema为空，使用str类型")
        return "str", ""
    
    # 处理引用
    if "$ref"in schema:
        ref = schema["$ref"]
        logger.debug(f"字段 {field_name} 包含引用: {ref}")
        
        # 提取模型名称
        model_name_match = re.search(r"#/components/schemas/(\w+)", ref)
        if (model_name_match):
            model_name = model_name_match.group(1)
            python_type = model_name
            logger.debug(f"从引用提取模型名称: {model_name}")
        else:
            # 尝试从简单路径中提取名称
            simple_name_match = re.search(r"([^/]+)$", ref)
            if (simple_name_match):
                model_name = simple_name_match.group(1)
                python_type = model_name
                logger.debug(f"从简单路径提取模型名称: {model_name}")
            else:
                logger.warning(f"无法从引用中提取模型名称: {ref}")
                python_type = "str"  # 默认为字符串
    
    # 处理联合类型 (oneOf)
    elif "oneOf"in schema:
        options = []
        for option in schema["oneOf"]:
            option_type, option_imports = infer_type_from_schema(option, field_name, nested_objects)
            options.append(option_type)
            if (option_imports):
                imports += option_imports + "\n"
        
        if (options):
            python_type = " | ".join(options)
            logger.debug(f"推断为联合类型: {python_type}")
        else:
            python_type = "str"
            logger.warning(f"oneOf中没有有效选项，使用str类型")
    
    # 处理数组类型
    elif schema.get("type") == "array":
        if "items"in schema:
            item_type, item_imports = infer_type_from_schema(schema["items"], f"{field_name}_item", nested_objects)
            python_type = f"list[{item_type}]"
            imports += item_imports
            logger.debug(f"推断为数组类型: {python_type}")
        else:
            python_type = "list[str]"  # 默认为字符串列表
            logger.debug(f"数组未指定items，使用list[str]")
    
    # 处理对象类型
    elif schema.get("type") == "object":
        # 检查是否有明确的属性定义
        if "properties"in schema and schema["properties"]:
            # 创建合适的类名 - 使用zh2en映射表
            # in 类名生成时，强制转为英文
            class_name = create_class_name(field_name)
            
            # 记录嵌套对象信息以便后续处理
            if (nested_objects is not None):
                logger.debug(f"添加嵌套对象: '{field_name}' -> '{class_name}'")
                nested_objects.append({
                    "name": class_name,
                    "schema": schema
                })
            
            python_type = class_name
            logger.debug(f"对象有属性定义，使用类名: {class_name}")
        elif "additionalProperties"in schema:
            prop_type, prop_imports = infer_type_from_schema(
                schema["additionalProperties"], f"{field_name}_value", nested_objects
            )
            python_type = f"dict[str, {prop_type}]"
            imports += prop_imports
            logger.debug(f"推断为字典类型: {python_type}")
        else:
            # 没有属性定义，使用字典类型
            python_type = "dict[str, Any]"
            logger.debug(f"对象未指定属性，使用dict[str, Any]")
    
    # 处理基本类型
    elif "type"in schema:
        schema_type = schema["type"]
        
        if schema_type == "string":
            format_type = schema.get("format", "")
            if format_type == "date-time":
                python_type = "datetime"
                imports += "from datetime import datetime\n"
            elif format_type == "date":
                python_type = "date"
                imports += "from datetime import date\n"
            elif format_type == "time":
                python_type = "time"
                imports += "from datetime import time\n"
            elif format_type == "binary":
                python_type = "bytes"
            else:
                python_type = "str"
        
        elif schema_type == "number":
            format_type = schema.get("format", "")
            if format_type == "float":
                python_type = "float"
            else:
                python_type = "float"  # 默认为float
        
        elif schema_type == "integer":
            python_type = "int"
        
        elif schema_type == "boolean":
            python_type = "bool"
        
        elif schema_type == "null":
            python_type = "None"
        
        else:
            logger.warning(f"未知类型: {schema_type}，使用str")
            python_type = "str"
        
        logger.debug(f"推断为基本类型: {python_type}")
    
    # 没有明确类型的情况
    else:
        logger.warning(f"无法推断类型，使用str: {schema}")
        python_type = "str"  # 默认使用str
    
    return python_type, imports.strip()


def parse_property_type(
    prop_schema: dict[str, Any], 
    prop_name: str,
    nested_objects_list: list[NestedObjectInfo] | None = None,
    nested_objects_dict: dict[str, dict[str, Any]] | None = None
) -> tuple[str, str]:
    """
    解析属性类型，支持两种方式收集嵌套对象
    
    Args:
        prop_schema: 属性的JSON Schema
        prop_name: 属性名
        nested_objects_list: 收集嵌套对象的列表（旧方式），如果为None则不收集
        nested_objects_dict: 收集嵌套对象的字典（新方式），如果为None则不收集
        
    Returns:
        元组 (类型字符串, 附加导入语句)
    """
    # 针对特定字段名进行自定义处理
    if prop_name == "messages" and prop_schema.get("type") == "array":
        # 特殊处理消息类型
        logger.debug(f"特殊处理'messages'字段")
        if "items"in prop_schema and prop_schema["items"].get("type") == "object":
            # 创建MessagesItem类
            if (nested_objects_dict is not None):
                nested_objects_dict["MessagesItem"] = prop_schema["items"]
                logger.debug(f"添加MessagesItem类到嵌套对象字典")
            
            # 如果存in data属性并且包含content数组字段
            items_schema = prop_schema["items"]
            if "properties"in items_schema and "data"in items_schema["properties"]:
                data_schema = items_schema["properties"]["data"]
                if "properties"in data_schema and "content"in data_schema["properties"]:
                    content_schema = data_schema["properties"]["content"]
                    if content_schema.get("type") == "array" and "items"in content_schema:
                        # 创建MessagesData类
                        if (nested_objects_dict is not None):
                            data_class_name = "MessagesData"
                            nested_objects_dict[data_class_name] = data_schema
                            logger.debug(f"添加{data_class_name}类到嵌套对象字典")
        
        return "list[MessagesItem]", ""
    
    # 获取类型注解 and 可能的导入语句
    type_annotation, imports = infer_type_from_schema(prop_schema, prop_name, nested_objects_list)
    
    # 如果还提供了新版嵌套对象字典，也收集嵌套类型信息
    if (nested_objects_dict is not None and prop_schema.get("type") == "object" and "properties"in prop_schema):
        class_name = create_class_name(prop_name)
        nested_objects_dict[class_name] = prop_schema
        logger.debug(f"添加{class_name}类到嵌套对象字典")
        type_annotation = class_name
    
    # 处理可能的空值（nullable or required）
    is_nullable = prop_schema.get("nullable", False)
    
    # 如果可以为空，添加 | None
    if is_nullable:
        type_annotation = f"{type_annotation} | None"
        logger.debug(f"属性 {prop_name} 可为空，类型更新为: {type_annotation}")
    
    return type_annotation, imports


def is_simple_type(type_str: str) -> bool:
    """
    检查类型是否为简单类型
    
    Args:
        type_str: 类型字符串
        
    Returns:
        如果是简单类型则为True
    """
    simple_types = {"str", "int", "float", "bool", "None", "Any"}
    return simple_types