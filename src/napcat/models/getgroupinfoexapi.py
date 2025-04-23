# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659229e0
@llms.txt: https://napcat.apifox.cn/226659229e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群信息ex

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_info_ex"
__id__ = "226659229e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupInfoExReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupInfoExRes(BaseModel):
    """
    响应参数
    """

    groupCode: str = Field(..., description="")
    resultCode: float = Field(..., description="")
    extInfo: dict = Field(..., description="")
# region res/

# region api
class GetGroupInfoExAPI(BaseModel):
    
    Request : type[GetGroupInfoExReq] = GetGroupInfoExReq
    Response  : type[GetGroupInfoExRes] = GetGroupInfoExRes


# region api/
# region code/

