# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659165e0
@llms.txt: https://napcat.apifox.cn/226659165e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置私聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_private_msg_as_read"
__id__ = "226659165e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class MarkPrivateMsgAsReadReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
# region req/


# region res
class MarkPrivateMsgAsReadRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class MarkPrivateMsgAsReadAPI(BaseModel):
    
    Request : type[MarkPrivateMsgAsReadReq] = MarkPrivateMsgAsReadReq
    Response  : type[MarkPrivateMsgAsReadRes] = MarkPrivateMsgAsReadRes


# region api/
# region code/

