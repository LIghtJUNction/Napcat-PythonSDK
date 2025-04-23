# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658669e0
@llms.txt: https://napcat.apifox.cn/226658669e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置群头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_portrait"
__id__ = "226658669e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupPortraitReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file: str = Field(..., description="")
# region req/


# region res
class SetGroupPortraitRes(BaseModel):
    """
    响应参数
    """

    result: str = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class SetGroupPortraitAPI(BaseModel):
    
    Request : type[SetGroupPortraitReq] = SetGroupPortraitReq
    Response  : type[SetGroupPortraitRes] = SetGroupPortraitRes


# region api/
# region code/

