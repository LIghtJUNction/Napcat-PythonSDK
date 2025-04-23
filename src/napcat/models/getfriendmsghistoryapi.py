# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659174e0
@llms.txt: https://napcat.apifox.cn/226659174e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取好友历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friend_msg_history"
__id__ = "226659174e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetFriendMsgHistoryReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
    message_seq: float | str | None = Field(None, description="0为最新")
    count: float | None = Field(None, description="数量")
    reverseOrder: bool | None = Field(False, description="倒序")
# region req/


# region res
class GetFriendMsgHistoryRes(BaseModel):
    """
    响应参数
    """

    messages: list[消息详情] = Field(..., description="")
# region res/

# region api
class GetFriendMsgHistoryAPI(BaseModel):
    
    Request : type[GetFriendMsgHistoryReq] = GetFriendMsgHistoryReq
    Response  : type[GetFriendMsgHistoryRes] = GetFriendMsgHistoryRes


# region api/
# region code/

