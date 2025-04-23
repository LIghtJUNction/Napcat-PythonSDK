# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658660e0
@llms.txt: https://napcat.apifox.cn/226658660e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_system_msg"
__id__ = "226658660e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupSystemMsgReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupSystemMsgRes(BaseModel):
    """
    响应参数
    """

    InvitedRequest: list[dict] = Field(..., description="")
    join_requests: list[dict] = Field(..., description="")
# region res/

# region api
class GetGroupSystemMsgAPI(BaseModel):
    
    Request : type[GetGroupSystemMsgReq] = GetGroupSystemMsgReq
    Response  : type[GetGroupSystemMsgRes] = GetGroupSystemMsgRes


# region api/
# region code/

