# -*- coding: utf-8 -*-
"""
获取消息详情 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal, Any

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取消息详情请求参数
    """
    message_id: int | str = Field(description="消息ID")


class MessageSender(BaseModel):
    """
    消息发送者信息
    """
    user_id: int = Field(default=0, description="发送者QQ号")
    nickname: str = Field(default="", description="发送者昵称")
    card: str | None = Field(default=None, description="群名片，私聊消息中此字段为null")
    
    model_config = ConfigDict(
        extra="allow",
        frozen=False,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class ResponseData(BaseModel):
    """
    获取消息详情响应数据模型
    """
    time: int = Field(default=0, description="发送时间")
    message_type: str = Field(default="", description="消息类型，private或group")
    message_id: int | str = Field(default=0, description="消息ID")
    real_id: int = Field(default=0, description="消息真实ID")
    sender: MessageSender = Field(default_factory=MessageSender, description="发送者信息")
    message: str = Field(default="", description="消息内容")
    raw_message: str = Field(default="", description="原始消息内容")
    target_id: int | None = Field(default=None, description="私聊消息的对方ID，群消息中此字段为null")
    group_id: int | None = Field(default=None, description="群ID，私聊消息中此字段为null")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取消息详情响应参数
    """
    pass


class GetMsgAPI(BaseHttpAPI):
    """
    获取消息详情 API
    用于根据消息ID获取消息的详细内容和相关信息
    接口地址: https://napcat.apifox.cn/226659106e0.md

    参数：
    {
      "message_id": "123456"  // 消息ID
    }

    返回：
    - 消息详情，包含消息内容、发送者信息、时间和类型等
    """

    api: str = "/get_msg"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.messages.get_msg
    test_model(Request)
    test_model(MessageSender)
    test_model(ResponseData)
    test_model(Response)