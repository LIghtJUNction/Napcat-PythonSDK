# -*- coding: utf-8 -*-
"""
撤回消息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    撤回消息请求参数
    """
    message_id: str = Field(description="要撤回的消息ID")


class ResponseData(BaseModel):
    """
    撤回消息响应数据模型
    """
    success: bool = Field(default=False, description="是否撤回成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    撤回消息响应参数
    """
    pass


class RecallMsgAPI(BaseHttpAPI):
    """
    撤回消息 API
    用于撤回已发送的消息
    接口地址: https://napcat.apifox.cn/226659151e0.md

    参数：
    {
      "message_id": "abcd-1234-efgh-5678"
    }

    返回：
    - 撤回消息的结果状态，包含是否成功和相关消息
    """

    api: str = "/delete_msg"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.messages.recall_msg
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)