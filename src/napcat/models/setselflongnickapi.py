# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659186e0
@llms.txt: https://napcat.apifox.cn/226659186e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置个性签名

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_self_longnick"
__id__ = "226659186e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SetSelfLongnickReq(BaseModel):
    """
    请求参数
    """

    longNick: str = Field(..., description="内容")
# region req/


# region res
class SetSelfLongnickRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class SetSelfLongnickAPI(BaseModel):
    
    Request : type[SetSelfLongnickReq] = SetSelfLongnickReq
    Response  : type[SetSelfLongnickRes] = SetSelfLongnickRes


# region api/
# region code/

