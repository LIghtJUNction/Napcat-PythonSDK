# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656913e0
@llms.txt: https://napcat.apifox.cn/226656913e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置群成员名片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_card"
__id__ = "226656913e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupCardReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    user_id: float | str = Field(..., description="")
    card: str = Field(..., description="为空则为取消群名片")
# region req/


# region res
class SetGroupCardRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupCardAPI(BaseModel):
    
    Request : type[SetGroupCardReq] = SetGroupCardReq
    Response  : type[SetGroupCardRes] = SetGroupCardRes


# region api/
# region code/

