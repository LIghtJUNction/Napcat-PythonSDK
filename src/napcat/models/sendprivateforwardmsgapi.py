# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657399e0
@llms.txt: https://napcat.apifox.cn/226657399e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:发送私聊合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_forward_msg"
__id__ = "226657399e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendPrivateForwardMsgReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
    messages: list[dict] = Field(..., description="")
# region req/


# region res
class SendPrivateForwardMsgRes(BaseModel):
    """
    响应参数
    """

    message_id: float = Field(..., description="")
    res_id: str = Field(..., description="")
# region res/

# region api
class SendPrivateForwardMsgAPI(BaseModel):
    
    Request : type[SendPrivateForwardMsgReq] = SendPrivateForwardMsgReq
    Response  : type[SendPrivateForwardMsgRes] = SendPrivateForwardMsgRes


# region api/
# region code/

