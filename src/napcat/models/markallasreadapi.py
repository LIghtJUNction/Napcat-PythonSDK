# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659194e0
@llms.txt: https://napcat.apifox.cn/226659194e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:_设置所有消息已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_mark_all_as_read"
__id__ = "226659194e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class MarkAllAsReadReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class MarkAllAsReadRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class MarkAllAsReadAPI(BaseModel):
    
    Request : type[MarkAllAsReadReq] = MarkAllAsReadReq
    Response  : type[MarkAllAsReadRes] = MarkAllAsReadRes


# region api/
# region code/

