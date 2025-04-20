# -*- coding: utf-8 -*-
"""
发送群聊消息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal, Any

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    发送群聊消息请求参数
    """
    group_id: int = Field(description="群号")
    message: str | dict[str, Any] = Field(description="要发送的消息内容，文本或消息段")
    auto_escape: bool = Field(default=False, description="是否转义消息内容，默认false")


class ResponseData(BaseModel):
    """
    发送群聊消息响应数据模型
    """
    message_id: str = Field(default="", description="消息ID")
    time: int = Field(default=0, description="发送时间戳")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    发送群聊消息响应参数
    """
    pass


class SendGroupMsgAPI(BaseHttpAPI):
    """
    发送群聊消息 API
    用于向指定群发送消息
    接口地址: https://napcat.apifox.cn/226659146e0.md

    参数：
    {
      "group_id": 123456789,
      "message": "大家好，这是一条测试消息",
      "auto_escape": false
    }

    返回：
    - 发送群聊消息的结果，包含消息ID和发送时间
    """

    api: str = "/send_group_msg"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.messages.send_group_msg
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)