"""
获取群列表 API
用于获取机器人所加入的群列表
接口地址: https://napcat.apifox.cn/227425528e0.md

参数：
无需参数

返回：
- 群列表信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class GetGroupListReq(TypedDict):
    """
    获取群列表 API 请求参数
    """
    pass  # 无需参数

class GroupListItem(TypedDict):
    """
    群列表项
    """
    group_id: int      # 群号
    group_name: str    # 群名称
    group_memo: str    # 群备注
    member_count: int  # 成员数
    max_member_count: int  # 最大成员数

class GetGroupListRes(BaseHttpResponse[list[GroupListItem]]):
    """
    获取群列表 API 响应参数
    """
    pass