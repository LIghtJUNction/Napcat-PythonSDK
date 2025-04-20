# -*- coding: utf-8 -*-
"""
获取在线机型 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取在线机型请求参数
    """
    model: str = Field(default="", description="机型名称")


class Variant(BaseModel):
    """
    机型变体模型
    包含机型显示信息和支付状态
    """
    model_show: str = Field(default="", description="机型显示信息")
    need_pay: bool = Field(default=False, description="是否需要付费")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class ResponseData(BaseModel):
    """
    响应数据模型
    包含当前在线机型信息
    """
    variants: list[Variant] = Field(default_factory=list, description="机型变体列表")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取在线机型响应参数
    """
    pass


class GetModelShowAPI(BaseHttpAPI):
    """
    获取在线机型 API
    用于获取当前账号设置的在线机型信息
    接口地址: https://napcat.apifox.cn/227233981e0.md

    参数：
    无需参数

    返回：
    - 当前在线机型信息，包含机型ID、机型名称和显示信息等
    """

    api: str = "/_get_model_show"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account._get_model_show
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)


