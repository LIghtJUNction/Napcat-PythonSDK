# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656932e0
@llms.txt: https://napcat.apifox.cn/226656932e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:处理好友请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_friend_add_request"
__id__ = "226656932e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SetFriendAddRequestReq(BaseModel):
    """
    请求参数
    """

    flag: str = Field(..., description="请求id")
    approve: bool = Field(..., description="是否同意")
    remark: str = Field(..., description="好友备注")
# region req/


# region res
class SetFriendAddRequestRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetFriendAddRequestAPI(BaseModel):
    
    Request : type[SetFriendAddRequestReq] = SetFriendAddRequestReq
    Response  : type[SetFriendAddRequestRes] = SetFriendAddRequestRes


# region api/
# region code/

