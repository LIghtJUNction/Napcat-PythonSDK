# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656919e0
@llms.txt: https://napcat.apifox.cn/226656919e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置群名

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_name"
__id__ = "226656919e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupNameReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    group_name: str = Field(..., description="")
# region req/


# region res
class SetGroupNameRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupNameAPI(BaseModel):
    
    Request : type[SetGroupNameReq] = SetGroupNameReq
    Response  : type[SetGroupNameRes] = SetGroupNameRes


# region api/
# region code/

