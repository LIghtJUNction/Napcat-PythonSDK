# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657083e0
@llms.txt: https://napcat.apifox.cn/226657083e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_status"
__id__ = "226657083e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetStatusReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetStatusRes(BaseModel):
    """
    响应参数
    """

    online: bool = Field(..., description="")
    good: bool = Field(..., description="")
    stat: dict = Field(..., description="")
# region res/

# region api
class GetStatusAPI(BaseModel):
    
    Request : type[GetStatusReq] = GetStatusReq
    Response  : type[GetStatusRes] = GetStatusRes


# region api/
# region code/

