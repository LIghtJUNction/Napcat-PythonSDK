"""
获取群系统消息 API
用于获取群组系统消息，如入群申请、邀请消息等
接口地址: https://napcat.apifox.cn/226658660e0.md

参数:
无需参数

返回:
- invited_requests: list - 邀请消息列表
- join_requests: list - 进群消息列表

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetGroupSystemMsgReq(TypedDict):
    """
    获取群系统消息 API 请求参数
    """
    pass  # 无请求参数

class JoinRequest(TypedDict):
    """
    入群请求信息
    """
    request_id: str         # 请求ID
    group_id: int           # 群号
    group_name: str         # 群名称
    requester_uin: int      # 请求者QQ号
    requester_nick: str     # 请求者昵称
    message: str            # 入群附加消息
    flag: str               # 请求标识，用于处理请求
    time: int               # 请求时间戳

class InvitedRequest(TypedDict):
    """
    邀请消息信息
    """
    request_id: str         # 请求ID
    group_id: int           # 群号
    group_name: str         # 群名称
    inviter_uin: int        # 邀请者QQ号
    inviter_nick: str       # 邀请者昵称
    flag: str               # 请求标识，用于处理请求
    time: int               # 请求时间戳

class GroupSystemMsgResult(TypedDict):
    """
    群系统消息结果
    """
    invited_requests: list[InvitedRequest]  # 邀请消息列表
    join_requests: list[JoinRequest]        # 进群消息列表

class GetGroupSystemMsgRes(BaseHttpResponse[GroupSystemMsgResult]):
    """
    获取群系统消息 API 响应参数
    """
    pass