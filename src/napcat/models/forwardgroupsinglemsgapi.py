# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659074e0
@llms.txt: https://napcat.apifox.cn/226659074e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:消息转发到群

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "forward_group_single_msg"
__id__ = "226659074e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class ForwardGroupSingleMsgReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    message_id: float | str = Field(..., description="")
# region req/


# region res
class ForwardGroupSingleMsgRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class ForwardGroupSingleMsgAPI(BaseModel):
    
    Request : type[ForwardGroupSingleMsgReq] = ForwardGroupSingleMsgReq
    Response  : type[ForwardGroupSingleMsgRes] = ForwardGroupSingleMsgRes


# region api/
# region code/

