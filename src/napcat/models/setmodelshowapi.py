# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227233993e0
@llms.txt: https://napcat.apifox.cn/227233993e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:_设置在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_set_model_show"
__id__ = "227233993e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SetModelShowReq(BaseModel):
    """
    请求参数
    """

    model: str = Field(..., description="")
    model_show: str = Field(..., description="")
# region req/


# region res
class SetModelShowRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetModelShowAPI(BaseModel):
    
    Request : type[SetModelShowReq] = SetModelShowReq
    Response  : type[SetModelShowRes] = SetModelShowRes


# region api/
# region code/

