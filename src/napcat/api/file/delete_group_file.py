"""
删除群文件 API
用于删除群文件系统中的文件
接口地址: https://napcat.apifox.cn/227450048e0.md

参数：
- group_id: 群号
- file_id: 文件ID
- busid: 文件类型

返回：
- 删除操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class DeleteGroupFileReq(TypedDict):
    """
    删除群文件 API 请求参数
    """
    group_id: int  # 群号
    file_id: str   # 文件ID
    busid: int     # 文件类型

class DeleteGroupFileRes(BaseHttpResponse[dict[str, bool]]):
    """
    删除群文件 API 响应参数
    """
    pass