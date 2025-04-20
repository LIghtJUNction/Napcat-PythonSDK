"""
发送群消息 API (预留)
用于向指定群发送消息的预留接口
接口地址: https://napcat.apifox.cn/227493150e0.md

参数：
- group_id: 群号
- message: 要发送的内容
- auto_escape: 消息内容是否作为纯文本发送（即不解析CQ码）

返回：
- 消息ID

# NapCat 开发中
"""

from napcat.api.base.models import BaseHttpResponse
from pydantic import BaseModel

class SendGroupMsgReq(BaseModel):
    """
    发送群消息 API (预留) 请求参数
    """
    group_id: int    # 群号
    message: str     # 要发送的内容
    auto_escape: bool  # 消息内容是否作为纯文本发送

class MessageInfo(BaseModel):
    """
    消息发送结果
    """
    message_id: int  # 消息ID

class SendGroupMsgRes(BaseHttpResponse[MessageInfo]):
    """
    发送群消息 API (预留) 响应参数
    """
    pass