# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659254e0
@llms.txt: https://napcat.apifox.cn/226659254e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:fetch_user_profile_like

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_user_profile_like"
__id__ = "226659254e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class FetchUserProfileLikeReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
# region req/


# region res
class FetchUserProfileLikeRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class FetchUserProfileLikeAPI(BaseModel):
    
    Request : type[FetchUserProfileLikeReq] = FetchUserProfileLikeReq
    Response  : type[FetchUserProfileLikeRes] = FetchUserProfileLikeRes


# region api/
# region code/

