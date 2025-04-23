# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659234e0
@llms.txt: https://napcat.apifox.cn/226659234e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取被过滤的加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_ignore_add_request"
__id__ = "226659234e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetGroupIgnoreAddRequestReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetGroupIgnoreAddRequestRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetGroupIgnoreAddRequestAPI(BaseModel):
    
    Request : type[GetGroupIgnoreAddRequestReq] = GetGroupIgnoreAddRequestReq
    Response  : type[GetGroupIgnoreAddRequestRes] = GetGroupIgnoreAddRequestRes


# region api/
# region code/

