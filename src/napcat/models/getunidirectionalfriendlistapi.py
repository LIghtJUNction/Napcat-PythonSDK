# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151878e0
@llms.txt: https://napcat.apifox.cn/266151878e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取单向好友列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_unidirectional_friend_list"
__id__ = "266151878e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetUnidirectionalFriendListReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetUnidirectionalFriendListRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetUnidirectionalFriendListAPI(BaseModel):
    
    Request : type[GetUnidirectionalFriendListReq] = GetUnidirectionalFriendListReq
    Response  : type[GetUnidirectionalFriendListRes] = GetUnidirectionalFriendListRes


# region api/
# region code/

