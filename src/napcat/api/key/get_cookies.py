# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226657041e0
@endpoint: get_cookies
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/226657041e0
@llms.txt: https://napcat.apifox.cn/226657041e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_cookies API
@usage: 使用 `client.get_cookies()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_cookies"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetCookiesReq(BaseHttpRequest):
    """
    get_cookies 请求参数
    """

    pass
# region req/

# region data
class GetCookiesData(BaseModel):
    """
    get_cookies 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetCookiesRes(BaseHttpResponse[GetCookiesData]):
    """
    get_cookies 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetCookiesAPI(BaseHttpAPI[GetCookiesReq, GetCookiesRes]):
    """
    获取cookies
    """
    api: str = "/get_cookies"
    method: Literal["POST", "GET"] = "POST"

    Request = GetCookiesReq
    Response = GetCookiesRes

    request: GetCookiesReq
    response: GetCookiesRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetCookiesAPI)

# region code/

