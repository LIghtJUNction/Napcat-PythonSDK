# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657389e0
@llms.txt: https://napcat.apifox.cn/226657389e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置消息已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_msg_as_read"
__id__ = "226657389e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class MarkMsgAsReadReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str | None = Field(None, description="与user_id二选一")
    user_id: float | str | None = Field(None, description="与group_id二选一")
# region req/


# region res
class MarkMsgAsReadRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class MarkMsgAsReadAPI(BaseModel):
    
    Request : type[MarkMsgAsReadReq] = MarkMsgAsReadReq
    Response  : type[MarkMsgAsReadRes] = MarkMsgAsReadRes


# region api/
# region code/

