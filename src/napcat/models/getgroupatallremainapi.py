# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227245941e0
@llms.txt: https://napcat.apifox.cn/227245941e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群 @全体成员 剩余次数

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_at_all_remain"
__id__ = "227245941e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupAtAllRemainReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupAtAllRemainRes(BaseModel):
    """
    响应参数
    """

    can_at_all: bool = Field(..., description="")
    remain_at_all_count_for_group: float = Field(..., description="")
    remain_at_all_count_for_uin: float = Field(..., description="")
# region res/

# region api
class GetGroupAtAllRemainAPI(BaseModel):
    
    Request : type[GetGroupAtAllRemainReq] = GetGroupAtAllRemainReq
    Response  : type[GetGroupAtAllRemainRes] = GetGroupAtAllRemainRes


# region api/
# region code/

