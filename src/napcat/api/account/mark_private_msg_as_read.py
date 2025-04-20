# -*- coding: utf-8 -*-
"""
标记私聊消息已读 API
开发完毕
@作者：GitHub Copilot LIghtJUNction 纠正并复核
@日期：2025/04/20
"""

from typing import Literal

from pydantic import Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    标记私聊消息已读请求参数
    """
    user_id: int | str = Field(default=0, description="要标记已读消息的用户ID")

class ResponseData(BaseModel):
    """
    标记私聊消息已读响应数据模型
    """
    pass 


class Response(BaseHttpResponse[ResponseData]):
    """
    标记私聊消息已读响应参数
    """
    pass


class MarkPrivateMsgAsReadAPI(BaseHttpAPI):
    """
    标记私聊消息已读 API
    用于将与指定用户的私聊消息标记为已读状态
    接口地址: https://napcat.apifox.cn/226659165e0.md

    参数：
    {
      "user_id": 123456789,
    }

    返回：
    - 标记私聊消息已读的结果状态，包含是否成功和相关消息

    """

    api: str = "/set_private_msg_read"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.mark_private_msg_as_read
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)