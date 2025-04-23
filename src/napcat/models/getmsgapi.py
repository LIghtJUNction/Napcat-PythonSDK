# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656707e0
@llms.txt: https://napcat.apifox.cn/226656707e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_msg"
__id__ = "226656707e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetMsgReq(BaseModel):
    """
    请求参数
    """

    message_id: float | str = Field(..., description="")
# region req/


# region res
class GetMsgRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetMsgAPI(BaseModel):
    
    Request : type[GetMsgReq] = GetMsgReq
    Response  : type[GetMsgRes] = GetMsgRes


# region api/
# region code/

