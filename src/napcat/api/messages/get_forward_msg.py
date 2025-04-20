"""
获取合并转发消息 API
用于获取合并转发消息的内容
接口地址: https://napcat.apifox.cn/227228919e0.md

参数：
- id: 合并转发ID

返回：
- 合并转发消息的详细内容

# NapCat 开发中
"""

from typing import Any
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetForwardMsgReq(BaseModel):
    """
    获取合并转发消息 API 请求参数
    """
    id: str  # 合并转发ID

class ForwardMessage(BaseModel):
    """
    转发消息节点
    """
    content: str         # 消息内容
    sender: dict[str, Any]  # 发送人信息
    time: int           # 发送时间

class ForwardMessageData(BaseModel):
    """
    合并转发消息数据
    """
    messages: list[ForwardMessage]  # 消息列表

class GetForwardMsgRes(BaseHttpResponse[ForwardMessageData]):
    """
    获取合并转发消息 API 响应参数
    """
    pass