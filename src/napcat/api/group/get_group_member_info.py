"""
获取群成员详细信息 API
用于获取指定群成员的详细信息
接口地址: https://napcat.apifox.cn/group-member-info

参数：
- group_id: 群号
- user_id: 成员QQ号
- no_cache: 是否不使用缓存

返回：
- 群成员详细信息
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupMemberInfoReq(BaseModel):
    """
    获取群成员信息 API 请求参数
    """
    group_id: int   # 群号
    user_id: int    # 成员QQ号
    no_cache: bool  # 是否跳过缓存

class GroupMemberInfo(BaseModel):
    """
    群成员详细信息结构
    """
    user_id: int
    nickname: str
    card: str
    role: str
    join_time: int
    last_active: int
    level: int

class GetGroupMemberInfoRes(BaseHttpResponse[GroupMemberInfo]):
    """群成员详细信息 API 响应"""
    pass
