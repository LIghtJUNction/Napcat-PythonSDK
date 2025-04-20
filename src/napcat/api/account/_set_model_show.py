# -*- coding: utf-8 -*-
"""
设置在线机型 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置在线机型请求参数
    """
    model: str = Field(description="要设置的机型名称")
    model_show: str | None = Field(default=None, description="机型显示信息(可选)")


class ResponseData(BaseModel):
    """
    设置在线机型响应数据模型
    """
    success: bool = Field(default=False, description="是否设置成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    设置在线机型响应参数
    """
    pass


class SetModelShowAPI(BaseHttpAPI):
    """
    设置在线机型 API
    用于设置当前账号的在线机型信息
    接口地址: https://napcat.apifox.cn/227233983e0.md

    参数：
    {
      "model": "iPhone 13",
      "model_show": "iOS 17.1"  // 可选
    }

    返回：
    - 设置在线机型的结果状态，包含是否成功和相关消息
    """

    api: str = "/_set_model_show"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account._set_model_show
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)
