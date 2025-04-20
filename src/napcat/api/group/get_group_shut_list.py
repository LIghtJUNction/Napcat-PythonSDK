"""
获取群禁言列表 API
用于获取群组中被禁言的成员列表
接口地址: https://napcat.apifox.cn/226659300e0.md

参数:
- group_id: int - 群号

返回:
- 被禁言群成员列表

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupShutListReq(BaseModel):
    """
    获取群禁言列表 API 请求参数
    """
    group_id: int  # 群号

class ShutMember(BaseModel):
    """
    被禁言成员信息
    """
    user_id: int    # 成员QQ号
    nickname: str   # 成员昵称
    shut_time: int  # 禁言剩余时间(秒)
    shut_up_timestamp: int  # 禁言开始时间戳

class GroupShutListResult(BaseModel):
    """
    群禁言列表结果
    """
    shut_members: list[ShutMember]  # 被禁言成员列表

class GetGroupShutListRes(BaseHttpResponse[GroupShutListResult]):
    """
    获取群禁言列表 API 响应参数
    """
    pass