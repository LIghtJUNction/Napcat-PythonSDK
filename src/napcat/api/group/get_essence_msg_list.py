# -*- coding: utf-8 -*-
"""
获取群精华消息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal, Any

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取群精华消息请求参数
    """
    group_id: int = Field(description="群号")


class EssenceMessage(BaseModel):
    """
    精华消息数据模型
    """
    sender_id: int = Field(default=0, description="发送者QQ号")
    sender_nick: str = Field(default="", description="发送者昵称")
    sender_time: int = Field(default=0, description="消息发送时间")
    operator_id: int = Field(default=0, description="操作者QQ号")
    operator_nick: str = Field(default="", description="操作者昵称")
    operator_time: int = Field(default=0, description="设为精华消息的时间")
    message_id: str = Field(default="", description="消息ID")
    content: str = Field(default="", description="消息内容")
    
    model_config = ConfigDict(
        extra="allow",
        frozen=False,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class ResponseData(BaseModel):
    """
    获取群精华消息响应数据模型
    """
    messages: list[EssenceMessage] = Field(default_factory=list, description="精华消息列表")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取群精华消息响应参数
    """
    pass


class GetEssenceMsgListAPI(BaseHttpAPI):
    """
    获取群精华消息 API
    用于获取群聊中设置的精华消息列表
    接口地址: https://napcat.apifox.cn/226659164e0.md

    参数：
    {
      "group_id": 123456789
    }

    返回：
    - 群精华消息的列表，包含消息内容和相关信息
    """

    api: str = "/get_essence_msg_list"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.get_essence_msg_list
    test_model(Request)
    test_model(EssenceMessage)
    test_model(ResponseData)
    test_model(Response)