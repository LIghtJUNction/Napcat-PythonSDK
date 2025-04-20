"""
获取群信息 API
用于获取群详细信息
接口地址: https://napcat.apifox.cn/227425506e0.md

参数：
- group_id: 群号
- no_cache: 是否不使用缓存（使用缓存可能更新不及时，但响应更快）

返回：
- 群详细信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class GetGroupInfoReq(TypedDict):
    """
    获取群信息 API 请求参数
    """
    group_id: int   # 群号
    no_cache: bool  # 是否不使用缓存

class GroupInfo(TypedDict):
    """
    群信息
    """
    group_id: int           # 群号
    group_name: str         # 群名称
    group_memo: str         # 群备注
    group_create_time: int  # 群创建时间
    group_level: int        # 群等级
    member_count: int       # 成员数
    max_member_count: int   # 最大成员数
    owner_id: int           # 群主QQ号

class GetGroupInfoRes(BaseHttpResponse[GroupInfo]):
    """
    获取群信息 API 响应参数
    """
    pass