# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227233981e0
@llms.txt: https://napcat.apifox.cn/227233981e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:_获取在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_get_model_show"
__id__ = "227233981e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetModelShowReq(BaseModel):
    """
    请求参数
    """

    model: str = Field(..., description="")
# region req/


# region res
class GetModelShowRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetModelShowAPI(BaseModel):
    
    Request : type[GetModelShowReq] = GetModelShowReq
    Response  : type[GetModelShowRes] = GetModelShowRes


# region api/
# region code/

