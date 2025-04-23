# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656712e0
@llms.txt: https://napcat.apifox.cn/226656712e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_forward_msg"
__id__ = "226656712e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetForwardMsgReq(BaseModel):
    """
    请求参数
    """

    message_id: str = Field(..., description="")
# region req/


# region res
class GetForwardMsgRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetForwardMsgAPI(BaseModel):
    
    Request : type[GetForwardMsgReq] = GetForwardMsgReq
    Response  : type[GetForwardMsgRes] = GetForwardMsgRes


# region api/
# region code/

