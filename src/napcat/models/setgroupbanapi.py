# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656791e0
@llms.txt: https://napcat.apifox.cn/226656791e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:群禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_ban"
__id__ = "226656791e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupBanReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    user_id: float | str = Field(..., description="")
    duration: float = Field(..., description="")
# region req/


# region res
class SetGroupBanRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupBanAPI(BaseModel):
    
    Request : type[SetGroupBanReq] = SetGroupBanReq
    Response  : type[SetGroupBanRes] = SetGroupBanRes


# region api/
# region code/

