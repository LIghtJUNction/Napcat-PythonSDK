# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659182e0
@llms.txt: https://napcat.apifox.cn/226659182e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取收藏列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_collection_list"
__id__ = "226659182e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetCollectionListReq(BaseModel):
    """
    请求参数
    """

    category: str = Field(..., description="")
    count: str = Field(..., description="")
# region req/


# region res
class GetCollectionListRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetCollectionListAPI(BaseModel):
    
    Request : type[GetCollectionListReq] = GetCollectionListReq
    Response  : type[GetCollectionListRes] = GetCollectionListRes


# region api/
# region code/

