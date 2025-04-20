"""
移动群文件 API
用于在群文件系统中移动文件位置
接口地址: https://napcat.apifox.cn/227450124e0.md

参数：
- group_id: 群号
- file_id: 文件ID
- busid: 文件类型
- folder_id: 目标文件夹ID，空字符串表示根目录

返回：
- 移动操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class MoveGroupFileReq(TypedDict):
    """
    移动群文件 API 请求参数
    """
    group_id: int  # 群号
    file_id: str   # 文件ID
    busid: int     # 文件类型
    folder_id: str # 目标文件夹ID，空字符串表示根目录

class MoveGroupFileRes(BaseHttpResponse[dict[str, bool]]):
    """
    移动群文件 API 响应参数
    """
    pass