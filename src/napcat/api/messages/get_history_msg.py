"""
获取历史消息 API
用于获取指定目标的历史消息记录
接口地址: https://napcat.apifox.cn/227228972e0.md

参数：
- message_type: 消息类型，group或private
- user_id: 用户QQ号，当私聊类型时必填
- group_id: 群号，当群聊类型时必填
- count: 获取的消息数量，默认20

返回：
- 历史消息记录列表

# NapCat 开发中
"""

from typing import Literal, Any
from pydantic import BaseModel
from napcat.api.base.types import BaseHttpResponse

class GetHistoryMsgReq(BaseModel):
    """
    获取历史消息 API 请求参数
    """
    message_type: Literal["group", "private"]  # 消息类型，group或private
    user_id: int | None = None  # 用户QQ号，当私聊类型时必填
    group_id: int | None = None  # 群号，当群聊类型时必填
    count: int  # 获取的消息数量

class HistoryMessage(BaseModel):
    """
    历史消息
    """
    message_id: int        # 消息ID
    real_id: int           # 消息真实ID
    sender: dict[str, Any]  # 发送者信息
    time: int              # 发送时间
    message: str           # 消息内容
    message_type: str      # 消息类型

class GetHistoryMsgRes(BaseHttpResponse[list[HistoryMessage]]):
    """
    获取历史消息 API 响应参数
    """
    pass