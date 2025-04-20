"""
发送消息 API (预留)
用于发送消息，支持私聊和群聊
接口地址: https://napcat.apifox.cn/227493129e0.md

参数：
- message_type: 消息类型，private或group
- user_id: 用户QQ号，当私聊类型时必填
- group_id: 群号，当群聊类型时必填
- message: 要发送的内容
- auto_escape: 消息内容是否作为纯文本发送（即不解析CQ码）

返回：
- 消息ID

# NapCat 开发中
"""

from typing import Literal
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SendMsgReq(BaseModel):
    """
    发送消息 API (预留) 请求参数
    """
    message_type: Literal["private", "group"]  # 消息类型
    user_id: int | None = None  # 用户QQ号
    group_id: int | None = None  # 群号
    message: str      # 要发送的内容
    auto_escape: bool  # 消息内容是否作为纯文本发送

class MessageInfo(BaseModel):
    """
    消息发送结果
    """
    message_id: int  # 消息ID

class SendMsgRes(BaseHttpResponse[MessageInfo]):
    """
    发送消息 API (预留) 响应参数
    """
    pass