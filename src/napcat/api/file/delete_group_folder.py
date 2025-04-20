"""
删除群文件文件夹 API
用于删除群文件系统中的文件夹
接口地址: https://napcat.apifox.cn/227450068e0.md

参数：
- group_id: 群号
- folder_id: 文件夹ID

返回：
- 删除操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class DeleteGroupFolderReq(TypedDict):
    """
    删除群文件文件夹 API 请求参数
    """
    group_id: int   # 群号
    folder_id: str  # 文件夹ID

class DeleteGroupFolderRes(BaseHttpResponse[dict[str, bool]]):
    """
    删除群文件文件夹 API 响应参数
    """
    pass