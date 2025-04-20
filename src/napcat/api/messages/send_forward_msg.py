# -*- coding: utf-8 -*-
"""
发送合并转发消息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal, Any

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class ForwardNode(BaseModel):
    """
    合并转发消息节点
    """
    type: str = Field(default="node", description="节点类型，固定为node")
    data: dict[str, Any] = Field(..., description="节点数据，可以是id或自定义内容")
    
    model_config = ConfigDict(
        extra="allow",
        frozen=False,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class Request(BaseHttpRequest):
    """
    发送合并转发消息请求参数
    """
    messages: list[ForwardNode] = Field(description="转发消息节点列表")
    target_type: str = Field(default="group", description="转发类型，group或private")
    target_id: int | str = Field(description="目标ID，群号或用户ID")


class ResponseData(BaseModel):
    """
    发送合并转发消息响应数据模型
    """
    message_id: str = Field(default="", description="转发消息ID")
    forward_id: str = Field(default="", description="转发ID")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    发送合并转发消息响应参数
    """
    pass


class SendForwardMsgAPI(BaseHttpAPI):
    """
    发送合并转发消息 API
    用于发送合并转发消息（俗称合并转发）到群聊或私聊
    接口地址: https://napcat.apifox.cn/226659156e0.md

    参数：
    {
      "messages": [
        {
          "type": "node",
          "data": {
            "id": "123456"  // 直接引用消息
          }
        },
        {
          "type": "node",
          "data": {
            "name": "张三",
            "uin": "10001",
            "content": "你好啊"  // 自定义消息
          }
        }
      ],
      "target_type": "group",  // 转发类型，可选 group、private
      "target_id": 123456789   // 目标ID，群号或QQ号
    }

    返回：
    - 发送合并转发消息的结果，包含消息ID
    """

    api: str = "/send_forward_msg"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.messages.send_forward_msg
    test_model(ForwardNode)
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)