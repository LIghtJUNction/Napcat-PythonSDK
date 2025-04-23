# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659178e0
@llms.txt: https://napcat.apifox.cn/226659178e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:创建收藏

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "create_collection"
__id__ = "226659178e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class CreateCollectionReq(BaseModel):
    """
    请求参数
    """

    rawData: str = Field(..., description="内容")
    brief: str = Field(..., description="标题")
# region req/


# region res
class CreateCollectionRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class CreateCollectionAPI(BaseModel):
    
    Request : type[CreateCollectionReq] = CreateCollectionReq
    Response  : type[CreateCollectionRes] = CreateCollectionRes


# region api/
# region code/

