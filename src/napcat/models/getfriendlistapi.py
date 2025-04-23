# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656976e0
@llms.txt: https://napcat.apifox.cn/226656976e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取好友列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friend_list"
__id__ = "226656976e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetFriendListReq(BaseModel):
    """
    请求参数
    """

    no_cache: bool = Field(False, description="不缓存")
# region req/


# region res
class GetFriendListRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetFriendListAPI(BaseModel):
    
    Request : type[GetFriendListReq] = GetFriendListReq
    Response  : type[GetFriendListRes] = GetFriendListRes


# region api/
# region code/

