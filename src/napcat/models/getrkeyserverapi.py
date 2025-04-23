# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136236e0
@llms.txt: https://napcat.apifox.cn/283136236e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取rkey服务

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_rkey_server"
__id__ = "283136236e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetRkeyServerReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetRkeyServerRes(BaseModel):
    """
    响应参数
    """

    private_rkey: str = Field(..., description="")
    group_rkey: str = Field(..., description="")
    expired_time: float = Field(..., description="")
    name: str = Field(..., description="")
# region res/

# region api
class GetRkeyServerAPI(BaseModel):
    
    Request : type[GetRkeyServerReq] = GetRkeyServerReq
    Response  : type[GetRkeyServerRes] = GetRkeyServerRes


# region api/
# region code/

