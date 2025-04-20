"""
重命名群文件 API
用于重命名群文件系统中的文件
接口地址: https://napcat.apifox.cn/227450092e0.md

参数：
- group_id: 群号
- file_id: 文件ID
- busid: 文件类型
- new_name: 新文件名

返回：
- 重命名操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class RenameGroupFileReq(TypedDict):
    """
    重命名群文件 API 请求参数
    """
    group_id: int  # 群号
    file_id: str   # 文件ID
    busid: int     # 文件类型
    new_name: str  # 新文件名

class RenameGroupFileRes(BaseHttpResponse[dict[str, bool]]):
    """
    重命名群文件 API 响应参数
    """
    pass