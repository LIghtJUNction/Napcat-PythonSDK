# -*- coding: utf-8 -*-
"""
账号退出 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    账号退出请求参数
    """
    # 无需请求参数
    pass


class ResponseData(BaseModel):
    """
    账号退出响应数据模型
    """
    success: bool = Field(default=False, description="是否退出成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    账号退出响应参数
    """
    pass


class AccountLogoutAPI(BaseHttpAPI):
    """
    账号退出 API
    用于退出当前登录的账号
    接口地址: https://napcat.apifox.cn/226659194e0.md

    参数：
    {} // 无参数

    返回：
    - 账号退出的结果状态，包含是否成功和相关消息
    """

    api: str = "/logout"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.system.account_logout
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)