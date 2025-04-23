# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657044e0
@llms.txt: https://napcat.apifox.cn/226657044e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取 CSRF Token

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_csrf_token"
__id__ = "226657044e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetCsrfTokenReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetCsrfTokenRes(BaseModel):
    """
    响应参数
    """

    token: float = Field(..., description="")
# region res/

# region api
class GetCsrfTokenAPI(BaseModel):
    
    Request : type[GetCsrfTokenReq] = GetCsrfTokenReq
    Response  : type[GetCsrfTokenRes] = GetCsrfTokenRes


# region api/
# region code/

