# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227237873e0
@llms.txt: https://napcat.apifox.cn/227237873e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:删除好友

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_friend"
__id__ = "227237873e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class DeleteFriendReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str | None = Field(None, description="")
    friend_id: float | str | None = Field(None, description="")
    temp_block: bool = Field(..., description="拉黑")
    temp_both_del: bool = Field(..., description="双向删除")
# region req/


# region res
class DeleteFriendRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class DeleteFriendAPI(BaseModel):
    
    Request : type[DeleteFriendReq] = DeleteFriendReq
    Response  : type[DeleteFriendRes] = DeleteFriendRes


# region api/
# region code/

