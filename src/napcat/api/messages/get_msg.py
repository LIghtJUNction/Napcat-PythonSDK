"""
获取消息 API
用于获取消息的详细信息
接口地址: https://napcat.apifox.cn/227227981e0.md

参数：
- message_id: 消息ID

返回：
- 消息的详细信息

# NapCat 开发中
"""

from typing import Any
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetMsgReq(BaseModel):
    """
    获取消息 API 请求参数
    """
    message_id: int  # 消息ID

class MessageDetail(BaseModel):
    """
    消息详细信息
    """
    time: int          # 发送时间
    message_type: str  # 消息类型，group或private
    message_id: int    # 消息ID
    real_id: int       # 消息真实ID
    sender: dict[str, Any]  # 发送人信息
    message: str       # 消息内容

class GetMsgRes(BaseHttpResponse[MessageDetail]):
    """
    获取消息 API 响应参数
    """
    pass