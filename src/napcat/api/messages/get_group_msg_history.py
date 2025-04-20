# -*- coding: utf-8 -*-
"""
获取群历史消息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal, Any

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取群历史消息请求参数
    """
    group_id: int = Field(description="群号")
    message_seq: int | None = Field(default=None, description="起始消息序号，不提供则从最新消息开始")
    count: int = Field(default=20, description="获取的消息数量，默认为20")


class MessageSender(BaseModel):
    """
    消息发送者信息
    """
    user_id: int = Field(default=0, description="发送者QQ号")
    nickname: str = Field(default="", description="发送者昵称")
    card: str = Field(default="", description="群名片")
    
    model_config = ConfigDict(
        extra="allow",
        frozen=False,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class MessageDetail(BaseModel):
    """
    消息详情数据模型
    """
    message_id: str = Field(default="", description="消息ID")
    real_id: int = Field(default=0, description="消息真实ID")
    sender: MessageSender = Field(default_factory=MessageSender, description="发送者信息")
    time: int = Field(default=0, description="发送时间")
    message: str = Field(default="", description="消息内容")
    raw_message: str = Field(default="", description="原始消息内容")
    message_seq: int = Field(default=0, description="消息序号")
    anonymous: dict[str, Any] | None = Field(default=None, description="匿名信息，如果不是匿名消息则为null")
    
    model_config = ConfigDict(
        extra="allow",
        frozen=False,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class ResponseData(BaseModel):
    """
    获取群历史消息响应数据模型
    """
    messages: list[MessageDetail] = Field(default_factory=list, description="消息列表")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取群历史消息响应参数
    """
    pass


class GetGroupMsgHistoryAPI(BaseHttpAPI):
    """
    获取群历史消息 API
    用于获取指定群的历史消息记录
    接口地址: https://napcat.apifox.cn/226659123e0.md

    参数：
    {
      "group_id": 123456789,  // 群号
      "message_seq": 5000,    // 起始消息序号，不提供则从最新消息开始
      "count": 20             // 获取的消息数量，默认为20
    }

    返回：
    - 群历史消息的列表，包含消息内容、发送者信息和时间等详情
    """

    api: str = "/get_group_msg_history"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.messages.get_group_msg_history
    test_model(Request)
    test_model(MessageSender)
    test_model(MessageDetail)
    test_model(ResponseData)
    test_model(Response)