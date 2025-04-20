"""
获取群信息ex API
用于获取群组的扩展信息
接口地址: https://napcat.apifox.cn/226659229e0.md

参数:
- group_id: int - 群号

返回:
- 群组扩展信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupInfoExReq(BaseModel):
    """
    获取群信息ex API 请求参数
    """
    group_id: int  # 群号

class GroupInfoExData(BaseModel):
    """
    群组扩展信息
    """
    group_id: int           # 群号
    group_name: str         # 群名称
    group_memo: str         # 群备注
    group_create_time: int  # 群创建时间
    group_level: int        # 群等级
    member_count: int       # 成员数
    max_member_count: int   # 最大成员数
    owner_id: int           # 群主QQ号
    admin_flag: bool        # 是否为管理员
    last_join_time: int     # 最后加入时间
    last_sent_time: int     # 最后发言时间
    shutup_time_whole: int  # 全员禁言到期时间
    shutup_time_me: int     # 个人禁言到期时间

class GetGroupInfoExRes(BaseHttpResponse[GroupInfoExData]):
    """
    获取群信息ex API 响应参数
    """
    pass