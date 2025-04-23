# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656947e0
@llms.txt: https://napcat.apifox.cn/226656947e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:处理加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_add_request"
__id__ = "226656947e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupAddRequestReq(BaseModel):
    """
    请求参数
    """

    flag: str = Field(..., description="请求id")
    approve: bool = Field(..., description="是否同意")
    reason: str | None = Field(None, description="拒绝理由")
# region req/


# region res
class SetGroupAddRequestRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupAddRequestAPI(BaseModel):
    
    Request : type[SetGroupAddRequestReq] = SetGroupAddRequestReq
    Response  : type[SetGroupAddRequestRes] = SetGroupAddRequestRes


# region api/
# region code/

