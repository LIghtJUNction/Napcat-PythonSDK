# -*- coding: utf-8 -*-
"""
获取登录号信息 API
开发完毕
@作者：GitHub Copilot LIghtJUNction 已复查
@日期：2025/04/20
"""

from typing import Literal

from pydantic import Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel

class Request(BaseHttpRequest):
    """
    获取登录号信息请求参数
    """
    # 此API不需要请求参数
    pass

class ResponseData(BaseModel):
    """
    登录号信息数据模型
    """
    uuser_id : int = Field( default= 0 , description="用户ID")
    nickname : str = Field( default= "" , description="昵称")


class Response(BaseHttpResponse[ResponseData]):
    """
    获取登录号信息响应参数
    """
    pass

class GetLoginInfoAPI(BaseHttpAPI):
    """
    获取登录号信息 API
    用于获取当前登录的QQ账号基本信息
    接口地址: https://napcat.apifox.cn/226659175e0.md

    参数：
    {} // 无参数

    返回：
    - 当前登录账号的基本信息，包括QQ号、昵称、个性签名等
    """

    api: str = "/get_login_info"
    method: Literal['POST', 'GET'] = "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.get_login_info
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)
