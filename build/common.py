"""
通用工具函数模块
get_template：获取模板文本
get_api_json_files：获取API JSON文件列表
save_to_model_file：保存内容到模型文件
get_region：从源文本中提取指定区域内容
replace_region：替换源文本中特定区域的内容
replace_var：替换模板中的变量占位符
"""
from pathlib import Path
import re
import logging
from typing import Any

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_template() -> str:
    """
    获取模板文本
    
    Returns:
        模板文本
    """
    root = Path(__file__).parent.parent
    template_path = root / "api.py"

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    logger.debug(f"读取模板文件: {template_path}")
    return template



def get_api_json_files() -> list[Path]:
    """
    获取 api_json 目录下的所有文件
    
    Returns:
        api_json 目录下的所有文件路径列表
    """
    root = Path(__file__).parent.parent
    api_json_path = root / "data" / "api_json"
    
    if not api_json_path.exists():
        logger.error(f"API JSON 目录不存在: {api_json_path}")
        return []
    
    files = list(api_json_path.glob("*.json"))
    logger.debug(f"找到 {len(files)} 个 API JSON 文件")
    
    return files



def save_to_model_file(model_name: str, content: str) -> None:
    """
    将内容保存到指定的模型文件中
    
    Args:
        model_name: 模型名称，用于生成文件名
        content: 要保存的内容
    """
    # 确保模型名称不包含前导斜杠
    clean_model_name = model_name.lstrip('/').lstrip(".").lstrip("_").lower()
    
    root = Path(__file__).parent.parent
    # 确保 models 目录存在
    models_dir = root / "src" / "napcat" / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = models_dir / f"{clean_model_name}.py"
    
    logger.debug(f"正在保存内容到模型文件: {file_path}")
    
    try:
        # 创建文件并写入内容
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"成功保存内容到模型文件: {file_path}")
    except Exception as e:
        logger.error(f"保存模型文件失败: {e}")
        raise


def get_region(source_text: str, region_code: str) -> str:
    """
    从源文本中提取指定区域的内容
    
    Args:
        source_text: 源文本
        region_code: 区域代码，例如 "METADATA"
    
    Returns:
        指定区域内的内容，不包含区域标记行
    """
    logger.debug(f"正在提取区域: {region_code}")
    
    start_pattern = f"# region {region_code}"
    end_pattern = f"# endregion {region_code}"
    
    start_match = re.search(start_pattern, source_text)
    if not start_match:
        logger.warning(f"未找到区域开始标记: {start_pattern}")
        return ""
    
    end_match = re.search(end_pattern, source_text)
    if not end_match:
        logger.warning(f"未找到区域结束标记: {end_pattern}")
        return ""
    
    start_pos = start_match.end()
    end_pos = end_match.start()
    
    region_content = source_text[start_pos:end_pos].strip()
    logger.debug(f"成功提取区域内容，长度: {len(region_content)}")
    
    return region_content

def replace_region(source_text: str, region_code: str, new_content: str) -> str:
    """
    替换源文本中特定区域的内容
    
    Args:
        source_text: 源文本
        region_code: 区域代码，例如 "METADATA"
        new_content: 新的区域内容
    
    Returns:
        替换区域后的完整文本
    """
    logger.debug(f"正在替换区域: {region_code}")
    
    # 支持两种格式的结束标记: 标准格式 "# endregion xxx" 和自定义格式 "# region xxx/"
    start_pattern = f"# region {region_code}"
    end_patterns = [f"# endregion {region_code}", f"# region {region_code}/"]
    
    # 查找区域开始标记
    start_match = re.search(start_pattern, source_text)
    if not start_match:
        logger.warning(f"未找到区域开始标记: {start_pattern}")
        return source_text
    
    # 查找区域结束标记 (尝试两种格式)
    end_match = None
    end_pattern_used = None
    
    for end_pattern in end_patterns:
        match = re.search(end_pattern, source_text)
        if match:
            end_match = match
            end_pattern_used = end_pattern
            break
    
    if not end_match:
        logger.warning(f"未找到区域结束标记。尝试了以下格式: {end_patterns}")
        return source_text
    
    logger.debug(f"找到区域边界: {start_pattern} 到 {end_pattern_used}")
    
    # 构建替换后的文本
    start_pos = start_match.end()
    end_pos = end_match.start()
    
    result = (
        source_text[:start_pos] + 
        "\n" + new_content.strip() + "\n" + 
        source_text[end_pos:]
    )
    
    logger.debug(f"区域替换完成，新内容长度: {len(new_content)}")
    return result

def replace_var(template: str, variables: dict[str, Any]) -> str:
    """
    替换模板中的 {{xxx}} 格式变量
    
    Args:
        template: 包含变量占位符的模板文本
        variables: 变量名与值的映射字典
    
    Returns:
        替换变量后的文本
    """
    logger.debug(f"正在替换模板变量，变量数量: {len(variables)}")
    result = template
    
    # 查找所有变量占位符 {{xxx}}
    var_pattern = r"\{\{([^{}]+)\}\}"
    matches = re.findall(var_pattern, template)
    
    for var_name in matches:
        var_key = var_name.strip()
        if var_key in variables:
            placeholder = f"{{{{{var_key}}}}}"
            value = str(variables[var_key])
            result = result.replace(placeholder, value)
            logger.debug(f"替换变量 {var_key} -> {value[:20]}{'...' if len(value) > 20 else ''}")
        else:
            logger.warning(f"变量 {var_key} 在提供的变量字典中不存在")
    
    return result