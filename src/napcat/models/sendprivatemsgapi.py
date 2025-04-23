# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/244510838e0
@llms.txt: https://napcat.apifox.cn/244510838e0.md
@last_update: 2025-04-23 20:23:18

@description: 发送群消息

summary:发送私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_msg"
__id__ = "244510838e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendPrivateMsgReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
    message: list[文件消息] = Field(..., description="")
# region req/


# region res
class SendPrivateMsgRes(BaseModel):
    """
    响应参数
    """

    message_id: float = Field(..., description="消息ID")
# region res/

# region api
class SendPrivateMsgAPI(BaseModel):
    
    Request : type[SendPrivateMsgReq] = SendPrivateMsgReq
    Response  : type[SendPrivateMsgRes] = SendPrivateMsgRes


# region api/
# region code/

