# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656952e0
@llms.txt: https://napcat.apifox.cn/226656952e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取登录号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_login_info"
__id__ = "226656952e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetLoginInfoReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetLoginInfoRes(BaseModel):
    """
    响应参数
    """

    user_id: float = Field(..., description="")
    nickname: str = Field(..., description="")
# region res/

# region api
class GetLoginInfoAPI(BaseModel):
    
    Request : type[GetLoginInfoReq] = GetLoginInfoReq
    Response  : type[GetLoginInfoRes] = GetLoginInfoRes


# region api/
# region code/

