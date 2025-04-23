# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659136e0
@llms.txt: https://napcat.apifox.cn/226659136e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:发送合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_forward_msg"
__id__ = "226659136e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendForwardMsgReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str | None = Field(None, description="")
    user_id: float | str | None = Field(None, description="")
    messages: list[一级合并转发消息] = Field(..., description="")
    news: list[dict] = Field(..., description="")
    prompt: str = Field(..., description="外显")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="内容")
# region req/


# region res
class SendForwardMsgRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SendForwardMsgAPI(BaseModel):
    
    Request : type[SendForwardMsgReq] = SendForwardMsgReq
    Response  : type[SendForwardMsgRes] = SendForwardMsgRes


# region api/
# region code/

