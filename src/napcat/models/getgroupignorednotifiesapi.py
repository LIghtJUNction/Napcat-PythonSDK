# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659323e0
@llms.txt: https://napcat.apifox.cn/226659323e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群过滤系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_ignored_notifies"
__id__ = "226659323e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupIgnoredNotifiesReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupIgnoredNotifiesRes(BaseModel):
    """
    响应参数
    """

    join_requests: list[dict] = Field(..., description="")
# region res/

# region api
class GetGroupIgnoredNotifiesAPI(BaseModel):
    
    Request : type[GetGroupIgnoredNotifiesReq] = GetGroupIgnoredNotifiesReq
    Response  : type[GetGroupIgnoredNotifiesRes] = GetGroupIgnoredNotifiesRes


# region api/
# region code/

