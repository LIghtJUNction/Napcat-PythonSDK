"""
获取好友消息历史记录 API
用于获取与好友的聊天记录
接口地址: https://napcat.apifox.cn/227229029e0.md

参数：
- user_id: 好友QQ号
- message_seq: 起始消息序号，可通过上次请求的结果获取，首次请求为0
- count: 获取的消息数量，默认20

返回：
- 好友消息历史记录

# NapCat 开发中
"""

from typing import Any
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetFriendMsgHistoryReq(BaseModel):
    """
    获取好友消息历史记录 API 请求参数
    """
    user_id: int      # 好友QQ号
    message_seq: int  # 起始消息序号
    count: int        # 获取的消息数量

class FriendMessage(BaseModel):
    """
    好友消息
    """
    message_id: int        # 消息ID
    real_id: int           # 消息真实ID
    time: int              # 发送时间
    message: str           # 消息内容
    sender: dict[str, Any] # 发送者信息

class FriendMsgHistory(BaseModel):
    """
    好友消息历史记录
    """
    messages: list[FriendMessage]  # 消息列表
    next_message_seq: int          # 下一条消息序号

class GetFriendMsgHistoryRes(BaseHttpResponse[FriendMsgHistory]):
    """
    获取好友消息历史记录 API 响应参数
    """
    pass