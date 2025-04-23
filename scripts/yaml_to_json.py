#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
import logging
import urllib.parse
from pathlib import Path
import yaml
from typing import Any, TypeVar

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("yaml_to_json_conversion.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 定义类型变量用于递归类型注解
T = TypeVar('T', bound=dict[str, Any] | list[Any] | str | int | float | bool | None)

def yaml_to_json(input_dir: str | Path, output_dir: str | Path | None = None) -> None:
    """
    将YAML文件转换为JSON格式，特别处理URL编码内容
    
    Args:
        input_dir: YAML文件所在目录
        output_dir: 输出JSON文件目录，如果不指定则创建一个新目录
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir) if output_dir else input_path.parent / "api_json"
    output_path.mkdir(exist_ok=True, parents=True)
    
    logger.info(f"开始转换YAML到JSON: 输入目录 {input_path}, 输出目录 {output_path}")
    
    # 获取所有YAML文件
    yaml_files = list(input_path.glob("*.yaml"))
    yaml_files.extend(list(input_path.glob("*.yml")))
    
    logger.info(f"找到 {len(yaml_files)} 个YAML文件")
    
    # 转换每个文件
    for yaml_file in yaml_files:
        try:
            # 读取YAML文件
            logger.debug(f"处理文件: {yaml_file.name}")
            with open(yaml_file, 'r', encoding='utf-8') as f:
                yaml_content = f.read()
            
            # 预处理YAML内容，处理URL编码内容
            yaml_content = process_yaml_special_content(yaml_content)
            
            # 解析YAML
            try:
                yaml_data = yaml.safe_load(yaml_content)
                logger.debug(f"成功解析YAML: {yaml_file.name}")
            except yaml.YAMLError as e:
                logger.error(f"YAML解析错误: {yaml_file.name}, 错误: {str(e)}")
                continue
            
            # 处理YAML数据
            processed_data = process_yaml_data(yaml_data)
            
            # 保存为JSON文件
            json_file = output_path / f"{yaml_file.stem}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, ensure_ascii=False, indent=2)
            
            logger.info(f"成功转换: {yaml_file.name} -> {json_file.name}")
            
        except Exception as e:
            logger.error(f"处理文件 {yaml_file} 时出错: {e}", exc_info=True)
    
    logger.info(f"YAML到JSON转换完成，共处理 {len(yaml_files)} 个文件")

def process_yaml_data(data: dict[str, Any] | list[Any] | str | int | float | bool | None) -> dict[str, Any] | list[Any] | str | int | float | bool | None:
    """
    递归处理YAML数据，处理特殊字符和结构
    
    Args:
        data: 需要处理的YAML数据
        
    Returns:
        处理后的数据
    """
    if isinstance(data, dict):
        result: dict[str, Any] = {}
        for key, value in data.items():
            # 处理键名
            processed_key: str = key
            
            # 处理值
            processed_value = process_yaml_data(value)
            result[processed_key] = processed_value
        return result
    elif isinstance(data, list):
        return [process_yaml_data(item) for item in data]
    elif isinstance(data, str):
        # 处理字符串，检查是否有URL编码内容
        return decode_url_encoded_content(data)
    else:
        # 数字、布尔值等原样返回
        return data

def process_yaml_special_content(yaml_content: str) -> str:
    """
    预处理YAML内容，处理特殊格式和字符
    
    Args:
        yaml_content: YAML内容字符串
        
    Returns:
        处理后的YAML内容
    """
    logger.debug("正在预处理YAML内容...")
    
    # 处理description中的多行内容，确保正确缩进
    lines = yaml_content.split('\n')
    processed_lines: list[str] = []
    in_description = False
    description_indent = 0
    
    for line in lines:
        # 检测是否进入description字段
        if re.match(r'\s*description:\s*\|', line):
            in_description = True
            description_indent = line.find('description:')
            processed_lines.append(line)
            continue
            
        # 处理description内的内容
        if in_description:
            # 检测是否离开description（缩进减少或空行后有其他内容）
            if line.strip() and not line.startswith(' ' * (description_indent + 2)):
                in_description = False
            else:
                # 确保description内容正确缩进
                processed_lines.append(line)
                continue
                
        # 非description内容
        processed_lines.append(line)
    
    processed_yaml = '\n'.join(processed_lines)
    
    # 处理YAML中的URL编码内容
    processed_yaml = handle_url_encoded_content(processed_yaml)
    
    return processed_yaml

def handle_url_encoded_content(content: str) -> str:
    """
    处理YAML内容中的URL编码部分
    
    Args:
        content: YAML内容
        
    Returns:
        处理后的内容
    """
    # 查找可能包含URL编码的模式
    url_patterns = [
        # URL路径参数
        r'(/[^/\s]+)(%[0-9A-Fa-f]{2})+([^/\s]*)',
        # 其他可能的URL编码模式
        r'(\b)(%[0-9A-Fa-f]{2})+(\b)'
    ]
    
    for pattern in url_patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            encoded_part = match.group(0)
            try:
                decoded_part = urllib.parse.unquote(encoded_part)
                logger.debug(f"URL解码: {encoded_part} -> {decoded_part}")
                content = content.replace(encoded_part, decoded_part)
            except Exception as e:
                logger.warning(f"URL解码失败: {encoded_part}, 错误: {str(e)}")
    
    return content

def decode_url_encoded_content(text: str) -> str:
    """
    解码字符串中的URL编码内容
    
    Args:
        text: 可能包含URL编码的字符串
        
    Returns:
        解码后的字符串
    """
    # 检查字符串是否包含URL编码的字符
    if not text or '%' not in text:
        return text
    
    # 识别常见的URL编码模式
    # 1. 完整URL中的编码部分
    url_pattern = r'https?://[^\s]+'
    urls = re.finditer(url_pattern, text)
    
    for url_match in urls:
        url = url_match.group(0)
        try:
            decoded_url = urllib.parse.unquote(url)
            if decoded_url != url:
                logger.debug(f"解码URL: {url} -> {decoded_url}")
                text = text.replace(url, decoded_url)
        except Exception:
            pass
    
    # 2. 独立的编码序列
    encoded_pattern = r'(%[0-9A-Fa-f]{2})+'
    encoded_parts = re.finditer(encoded_pattern, text)
    
    for encoded_match in encoded_parts:
        encoded_part = encoded_match.group(0)
        try:
            decoded_part = urllib.parse.unquote(encoded_part)
            if decoded_part != encoded_part:
                logger.debug(f"解码内容: {encoded_part} -> {decoded_part}")
                text = text.replace(encoded_part, decoded_part)
        except Exception:
            pass
    
    return text

def main() -> None:
    """主函数"""
    # 获取当前脚本所在目录
    script_dir = Path(__file__).parent
    
    # API YAML文件目录
    api_yaml_dir = script_dir.parent / "data" / "api_yaml_raw"
    
    # 输出目录
    output_dir = script_dir.parent / "data" / "api_json"
    
    # 检查目录是否存在
    if not api_yaml_dir.exists():
        logger.error(f"API YAML目录不存在: {api_yaml_dir}")
        return
    
    # 转换YAML到JSON
    yaml_to_json(api_yaml_dir, output_dir)
    
    logger.info("转换完成!")

if __name__ == "__main__":
    main()