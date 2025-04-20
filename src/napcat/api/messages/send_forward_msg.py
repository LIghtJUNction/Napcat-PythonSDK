"""
发送合并转发消息 API
用于发送合并转发消息
接口地址: https://napcat.apifox.cn/227228955e0.md

参数：
- group_id: 群号(群消息)
- user_id: 对方QQ号(私聊消息)
- messages: 自定义转发消息节点列表

返回：
- 合并转发消息ID

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class ForwardNode(BaseModel):
    """
    转发消息节点
    """
    type: str       # 类型，目前固定值为node
    data: dict      # 节点数据

class SendForwardMsgReq(BaseModel):
    """
    发送合并转发消息 API 请求参数
    """
    group_id: int | None = None  # 群号(群消息)
    user_id: int | None = None   # 对方QQ号(私聊消息)
    messages: list[ForwardNode]  # 自定义转发消息节点列表

class ForwardMsgInfo(BaseModel):
    """
    合并转发消息信息
    """
    forward_id: str  # 合并转发ID

class SendForwardMsgRes(BaseHttpResponse[ForwardMsgInfo]):
    """
    发送合并转发消息 API 响应参数
    """
    pass