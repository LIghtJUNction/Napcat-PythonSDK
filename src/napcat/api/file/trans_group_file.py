"""
转发群文件到群 API
用于将文件从一个群转发到另一个群
接口地址: https://napcat.apifox.cn/227450223e0.md

参数：
- group_id: 源群号
- file_id: 文件ID
- busid: 文件类型
- target_group_id: 目标群号

返回：
- 转发结果信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class TransGroupFileReq(TypedDict):
    """
    转发群文件到群 API 请求参数
    """
    group_id: int       # 源群号
    file_id: str        # 文件ID
    busid: int          # 文件类型
    target_group_id: int # 目标群号

class TransFileResult(TypedDict):
    """
    文件转发结果
    """
    file_id: str     # 新文件ID
    file_name: str   # 文件名
    busid: int       # 文件类型

class TransGroupFileRes(BaseHttpResponse[TransFileResult]):
    """
    转发群文件到群 API 响应参数
    """
    pass