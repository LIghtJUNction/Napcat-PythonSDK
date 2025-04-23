# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659197e0
@llms.txt: https://napcat.apifox.cn/226659197e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取点赞列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_profile_like"
__id__ = "226659197e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetProfileLikeReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetProfileLikeRes(BaseModel):
    """
    响应参数
    """

    total_count: float = Field(..., description="总点赞数")
    new_count: float = Field(..., description="新点赞数")
    new_nearby_count: float = Field(..., description="")
    last_visit_time: float = Field(..., description="")
    userInfos: list[dict] = Field(..., description="")
# region res/

# region api
class GetProfileLikeAPI(BaseModel):
    
    Request : type[GetProfileLikeReq] = GetProfileLikeReq
    Response  : type[GetProfileLikeRes] = GetProfileLikeRes


# region api/
# region code/

