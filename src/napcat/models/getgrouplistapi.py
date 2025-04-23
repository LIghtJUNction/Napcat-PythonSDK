# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656992e0
@llms.txt: https://napcat.apifox.cn/226656992e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_list"
__id__ = "226656992e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetGroupListReq(BaseModel):
    """
    请求参数
    """

    no_cache: bool = Field(False, description="不缓存")
# region req/


# region res
class GetGroupListRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetGroupListAPI(BaseModel):
    
    Request : type[GetGroupListReq] = GetGroupListReq
    Response  : type[GetGroupListRes] = GetGroupListRes


# region api/
# region code/

