#!/usr/bin/env python

import datetime
import os
from pathlib import Path
import sys
import requests
import re

def extract_version(version_string): # type: ignore
    """
    从字符串中提取版本号
    
    Args:
        version_string: 可能包含版本号的字符串
        
    Returns:
        str: 提取的版本号，如果未找到则返回原字符串
    """
    # 匹配常见版本号格式，如 v1.0.0、1.0.0、1.0、v1.2.3-alpha 等
    pattern = r'v?(\d+(\.\d+)+(-\w+)?)'
    match = re.search(pattern, version_string) # type: ignore
    if match:
        return match.group(0)
    return version_string  # 如果没有找到匹配的版本号，返回原字符串 # type: ignore

def check_for_update():
    """
    检查是否有新版本。
    比较远程版本号与本地版本号，如果不一致或本地版本文件不存在，则返回1并更新本地文件。
    
    Returns:
        int: 退出状态码。0表示版本一致，1表示版本不一致或需要更新。
    """
    # 远程版本文件URL
    url = "https://napcat.apifox.cn/5430207m0.md"

    root = Path(__file__).parent.parent
    
    # 本地版本文件路径
    version_file = root / ".version"
    
    try:
        # 获取远程版本
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 提取远程文件最后一行作为版本号
        content = response.text.strip()
        remote_version = content.splitlines()[-1].strip()
        
        # 检查本地版本文件是否存在
        if not os.path.exists(version_file):
            # 本地版本文件不存在，写入新版本并返回1
            with open(version_file, 'w', encoding='utf-8') as f:
                f.write(remote_version)
            return 1
        
        # 读取本地版本
        with open(version_file, encoding='utf-8') as f:
            local_version = f.read().strip()
        
        # 比较版本
        if local_version != remote_version[3:]:
            # 版本不一致，更新本地版本并返回1
            remote_version_clean = extract_version(remote_version)
            local_version_clean = extract_version(local_version)
            
            print(f"检测到新版本: {remote_version_clean}")
            print(f"当前版本: {local_version_clean}")
            
            note = f"* [] [更新日志/{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-{local_version_clean} -> {remote_version_clean}]({url})"

            update_log_file = root / "update_log.md"

            with open(update_log_file, 'a', encoding='utf-8') as f:
                f.write(note + "\n")

            print(f"更新日志已记录到 {update_log_file}")

            with open(version_file, 'w', encoding='utf-8') as f:
                f.write(remote_version[3:])


            return 1
            
        # 版本一致，返回0
        return 0
    
    except Exception as e:
        print(f"检查更新时发生错误: {e}", file=sys.stderr)
        return 0  # 出错时不影响程序运行，返回0

if __name__ == "__main__":
    exit_code = check_for_update()
    sys.exit(exit_code)