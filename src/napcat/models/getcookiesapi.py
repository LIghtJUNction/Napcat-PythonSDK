# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657041e0
@llms.txt: https://napcat.apifox.cn/226657041e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取cookies

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_cookies"
__id__ = "226657041e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetCookiesReq(BaseModel):
    """
    请求参数
    """

    domain: str = Field(..., description="")
# region req/


# region res
class GetCookiesRes(BaseModel):
    """
    响应参数
    """

    cookies: str = Field(..., description="")
    bkn: str = Field(..., description="")
# region res/

# region api
class GetCookiesAPI(BaseModel):
    
    Request : type[GetCookiesReq] = GetCookiesReq
    Response  : type[GetCookiesRes] = GetCookiesRes


# region api/
# region code/

