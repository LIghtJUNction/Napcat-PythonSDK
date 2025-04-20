"""
发送私聊消息 API (预留)
用于向指定好友或陌生人发送私聊消息的预留接口
接口地址: https://napcat.apifox.cn/227493168e0.md

参数：
- user_id: 对方QQ号
- message: 要发送的内容
- auto_escape: 消息内容是否作为纯文本发送（即不解析CQ码）

返回：
- 消息ID

# NapCat 开发中
"""

from napcat.api.base.models import BaseHttpResponse
from pydantic import BaseModel

class SendPrivateMsgReq(BaseModel):
    """
    发送私聊消息 API (预留) 请求参数
    """
    user_id: int     # 对方QQ号
    message: str     # 要发送的内容
    auto_escape: bool  # 消息内容是否作为纯文本发送

class MessageInfo(BaseModel):
    """
    消息发送结果
    """
    message_id: int  # 消息ID

class SendPrivateMsgRes(BaseHttpResponse[MessageInfo]):
    """
    发送私聊消息 API (预留) 响应参数
    """
    pass