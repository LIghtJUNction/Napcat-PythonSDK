# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659292e0
@llms.txt: https://napcat.apifox.cn/226659292e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取用户状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_user_status"
__id__ = "226659292e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class NcGetUserStatusReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
# region req/


# region res
class NcGetUserStatusRes(BaseModel):
    """
    响应参数
    """

    status: float = Field(..., description="")
    ext_status: float = Field(..., description="")
# region res/

# region api
class NcGetUserStatusAPI(BaseModel):
    
    Request : type[NcGetUserStatusReq] = NcGetUserStatusReq
    Response  : type[NcGetUserStatusRes] = NcGetUserStatusRes


# region api/
# region code/

