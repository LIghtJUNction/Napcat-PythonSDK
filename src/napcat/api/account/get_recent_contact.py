"""
最近消息列表 API
用于获取最近的会话消息列表，每个会话返回最新的一条消息
接口地址: https://napcat.apifox.cn/226659190e0.md

参数：
- count: 要获取的最近消息数量(可选)

返回：
- 最近会话的消息列表，每个会话包含最新的一条消息内容
- 会话可能是私聊或群聊，包含会话ID、最后消息时间等信息

# NapCat 开发中
"""

from typing import Literal
from datetime import datetime
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetRecentContactReq(BaseModel):
    """
    最近消息列表 API 请求参数
    """
    count: int | None = None  # 要获取的最近消息数量(可选)

class MessageContent(BaseModel):
    """
    消息内容
    """
    type: str             # 消息类型
    text: str | None = None   # 文本内容(如果是文本消息)
    data: dict | None = None  # 其他类型消息的数据

class SessionInfo(BaseModel):
    """
    会话信息
    """
    session_type: Literal["private", "group"]  # 会话类型：私聊或群聊
    session_id: int                            # 会话ID(用户QQ号或群号)
    last_message: MessageContent               # 最后一条消息内容
    unread_count: int                          # 未读消息数量
    last_time: datetime                        # 最后消息时间
    name: str                                  # 会话名称(好友昵称/备注或群名称)

class RecentContactResult(BaseModel):
    """
    最近会话列表结果
    """
    sessions: list[SessionInfo]  # 会话列表

class GetRecentContactRes(BaseHttpResponse[RecentContactResult]):
    """
    最近消息列表 API 响应参数
    """
    pass