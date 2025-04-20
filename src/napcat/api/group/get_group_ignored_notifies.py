"""
获取群过滤系统消息 API
用于获取经过过滤的群系统消息
接口地址: https://napcat.apifox.cn/226659323e0.md

参数:
无需参数

返回:
- 过滤后的群系统消息列表

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetGroupIgnoredNotifiesReq(TypedDict):
    """
    获取群过滤系统消息 API 请求参数
    """
    pass  # 无需参数

class IgnoredRequestInfo(TypedDict):
    """
    被过滤的请求信息
    """
    request_id: str        # 请求ID
    group_id: int          # 群号
    group_name: str        # 群名称
    requester_uin: int     # 请求者QQ号
    requester_nick: str    # 请求者昵称
    message: str           # 请求消息
    flag: str              # 请求标识，用于处理请求
    time: int              # 请求时间戳
    filter_reason: str     # 过滤原因

class GetGroupIgnoredNotifiesRes(BaseHttpResponse[list[IgnoredRequestInfo]]):
    """
    获取群过滤系统消息 API 响应参数
    """
    pass