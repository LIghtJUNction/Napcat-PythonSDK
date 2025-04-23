# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658978e0
@llms.txt: https://napcat.apifox.cn/226658978e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取好友分组列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friends_with_category"
__id__ = "226658978e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetFriendsWithCategoryReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetFriendsWithCategoryRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetFriendsWithCategoryAPI(BaseModel):
    
    Request : type[GetFriendsWithCategoryReq] = GetFriendsWithCategoryReq
    Response  : type[GetFriendsWithCategoryRes] = GetFriendsWithCategoryRes


# region api/
# region code/

