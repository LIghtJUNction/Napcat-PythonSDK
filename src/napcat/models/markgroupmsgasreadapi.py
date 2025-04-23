# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659167e0
@llms.txt: https://napcat.apifox.cn/226659167e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置群聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_group_msg_as_read"
__id__ = "226659167e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class MarkGroupMsgAsReadReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class MarkGroupMsgAsReadRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class MarkGroupMsgAsReadAPI(BaseModel):
    
    Request : type[MarkGroupMsgAsReadReq] = MarkGroupMsgAsReadReq
    Response  : type[MarkGroupMsgAsReadRes] = MarkGroupMsgAsReadRes


# region api/
# region code/

