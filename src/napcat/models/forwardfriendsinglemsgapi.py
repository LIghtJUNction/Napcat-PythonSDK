# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659051e0
@llms.txt: https://napcat.apifox.cn/226659051e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:消息转发到私聊

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "forward_friend_single_msg"
__id__ = "226659051e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class ForwardFriendSingleMsgReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
    message_id: float | str = Field(..., description="")
# region req/


# region res
class ForwardFriendSingleMsgRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class ForwardFriendSingleMsgAPI(BaseModel):
    
    Request : type[ForwardFriendSingleMsgReq] = ForwardFriendSingleMsgReq
    Response  : type[ForwardFriendSingleMsgRes] = ForwardFriendSingleMsgRes


# region api/
# region code/

