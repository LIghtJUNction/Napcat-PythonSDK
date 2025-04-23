# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657054e0
@llms.txt: https://napcat.apifox.cn/226657054e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取 QQ 相关接口凭证

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_credentials"
__id__ = "226657054e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetCredentialsReq(BaseModel):
    """
    请求参数
    """

    domain: str = Field(..., description="")
# region req/


# region res
class GetCredentialsRes(BaseModel):
    """
    响应参数
    """

    cookies: str = Field(..., description="")
    token: float = Field(..., description="")
# region res/

# region api
class GetCredentialsAPI(BaseModel):
    
    Request : type[GetCredentialsReq] = GetCredentialsReq
    Response  : type[GetCredentialsRes] = GetCredentialsRes


# region api/
# region code/

