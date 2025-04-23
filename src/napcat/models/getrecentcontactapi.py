# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659190e0
@llms.txt: https://napcat.apifox.cn/226659190e0.md
@last_update: 2025-04-23 20:23:17

@description: 获取的最新消息是每个会话最新的消息

summary:最近消息列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_recent_contact"
__id__ = "226659190e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetRecentContactReq(BaseModel):
    """
    请求参数
    """

    count: float = Field(..., description="会话数量")
# region req/


# region res
class GetRecentContactRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetRecentContactAPI(BaseModel):
    
    Request : type[GetRecentContactReq] = GetRecentContactReq
    Response  : type[GetRecentContactRes] = GetRecentContactRes


# region api/
# region code/

