# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/250286915e0
@llms.txt: https://napcat.apifox.cn/250286915e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取clientkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_clientkey"
__id__ = "250286915e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetClientkeyReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetClientkeyRes(BaseModel):
    """
    响应参数
    """

    clientkey: str = Field(..., description="")
# region res/

# region api
class GetClientkeyAPI(BaseModel):
    
    Request : type[GetClientkeyReq] = GetClientkeyReq
    Response  : type[GetClientkeyRes] = GetClientkeyRes


# region api/
# region code/

