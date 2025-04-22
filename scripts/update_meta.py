from pathlib import Path
import json
import re

import requests

root = Path(__file__).parent.parent

base_url = "https://napcat.apifox.cn/"

# 获取文档内容
print("正在获取API文档...")
llms_md = requests.get(base_url + "/llms.txt").text

# 创建树形字典
api_tree = {}

# 第一遍扫描：收集所有可能的目录节点元数据
print("第一遍扫描：收集目录节点元数据...")
category_metadata = {}
# 正则匹配目录节点行：- [节点名称](URL): 描述
category_regex = r'- \[([^\]]+)\]\(([^\)]+)\):(.*)'
for line in llms_md.split('\n'):
    match = re.match(category_regex, line.strip())
    if match:
        name = match.group(1).strip()
        url = match.group(2).strip()
        description = match.group(3).strip() if match.group(3) else ""
        
        # 如果是目录节点（通常URL格式不同）
        if url.endswith(".md") or url.endswith(".html"):
            category_metadata[name] = {
                "url": url,
                "id": url.split('/')[-1].split('.')[0],
                "type": url[-5:-3] if len(url) >= 5 else "",
                "description": description
            }

# 第二遍扫描：处理API条目
print("第二遍扫描：构建API树...")
api_regex = r'- ([^[\n]+) \[([^\]]+)\]\(([^\)]+)\):(.*)'

# 解析每一行
for line in llms_md.split('\n'):
    match = re.match(api_regex, line.strip())
    if match:
        # 提取分类、名称、URL和描述
        categories = match.group(1).strip()
        name = match.group(2).strip()
        url = match.group(3).strip()
        description = match.group(4).strip() if match.group(4) else ""
        
        # 处理分类路径
        path_parts = []
        
        # 处理类似 "消息相关 > 发送群聊消息" 的路径
        if '>' in categories:
            parts = categories.split('>')
            for part in parts:
                path_parts.append(part.strip()) # type: ignore
        else:
            path_parts = [categories]
            
        # 将路径和名称组合
        full_path = path_parts + [name]
        
        # 构建树结构
        current = api_tree
        for part in path_parts:
            # 检查目录节点是否有元数据
            if part not in current:
                # 使用收集到的元数据或创建空字典
                current[part] = category_metadata.get(part, {}).copy() # type: ignore
            current = current[part] # type: ignore
        
        # 添加API详情
        current[name] = {
            "url": url,
            "id": url.split('/')[-1].split('.')[0],
            "type": url[-5:-3] if len(url) >= 5 else "",
            "description": description
        }

# 添加顶级文档节点，如果存在的话
if "NapCat 接口文档" in category_metadata and "NapCat 接口文档" not in api_tree:
    api_tree = { # type: ignore
        "NapCat 接口文档": { 
            **category_metadata["NapCat 接口文档"],
            **api_tree
        }
    }

# 将树形字典保存为JSON文件
output_path = root / "data" / "api_tree.json"
output_path.parent.mkdir(exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(api_tree, f, ensure_ascii=False, indent=2)

print(f"API树已保存至 {output_path}")

