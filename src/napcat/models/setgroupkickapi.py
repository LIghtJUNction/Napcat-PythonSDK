# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656748e0
@llms.txt: https://napcat.apifox.cn/226656748e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:群踢人

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_kick"
__id__ = "226656748e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupKickReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    user_id: float | str = Field(..., description="")
    reject_add_request: bool = Field(..., description="是否群拉黑")
# region req/


# region res
class SetGroupKickRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupKickAPI(BaseModel):
    
    Request : type[SetGroupKickReq] = SetGroupKickReq
    Response  : type[SetGroupKickRes] = SetGroupKickRes


# region api/
# region code/

