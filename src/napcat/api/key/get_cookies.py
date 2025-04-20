# -*- coding: utf-8 -*-
"""
获取Cookies API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal, Any

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取Cookies请求参数
    """
    domain: str = Field(default="", description="要获取cookie的域名，默认为空表示获取所有域名的cookie")


class CookieItem(BaseModel):
    """
    Cookie项数据模型
    """
    name: str = Field(default="", description="Cookie名称")
    value: str = Field(default="", description="Cookie值")
    domain: str = Field(default="", description="Cookie所属域名")
    path: str = Field(default="/", description="Cookie路径")
    expires: int = Field(default=0, description="过期时间戳")
    size: int = Field(default=0, description="Cookie大小")
    httponly: bool = Field(default=False, description="是否仅HTTP访问")
    secure: bool = Field(default=False, description="是否安全Cookie")
    session: bool = Field(default=True, description="是否会话Cookie")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class ResponseData(BaseModel):
    """
    获取Cookies响应数据模型
    """
    cookies: list[CookieItem] = Field(default_factory=list, description="Cookie列表")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取Cookies响应参数
    """
    pass


class GetCookiesAPI(BaseHttpAPI):
    """
    获取Cookies API
    用于获取登录QQ的相关Cookie信息
    接口地址: https://napcat.apifox.cn/250286964e0.md

    参数：
    {
      "domain": "qun.qq.com"  # 可选，要获取cookie的域名，默认为空表示获取所有域名的cookie
    }

    返回：
    - Cookie信息列表，包含名称、值、域名、过期时间等详细信息
    """

    api: str = "/get_cookies"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.key.get_cookies
    test_model(Request)
    test_model(CookieItem)
    test_model(ResponseData)
    test_model(Response)