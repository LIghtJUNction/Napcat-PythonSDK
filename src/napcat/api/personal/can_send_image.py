# -*- coding: utf-8 -*-
"""
检查是否可以发送图片 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    检查是否可以发送图片请求参数
    """
    pass  # 无需参数


class ResponseData(BaseModel):
    """
    发送图片检查状态数据模型
    """
    yes: bool = Field(default=False, description="是否可以发送图片")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    检查是否可以发送图片响应参数
    """
    pass


class CanSendImageAPI(BaseHttpAPI):
    """
    检查是否可以发送图片 API
    用于检查是否可以向指定目标发送图片
    接口地址: https://napcat.apifox.cn/227493677e0.md

    参数：
    无需参数

    返回：
    - 是否可以发送图片的检查结果
    """

    api: str = "/can_send_image"
    method: Literal['POST', 'GET'] = "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.personal.can_send_image
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)