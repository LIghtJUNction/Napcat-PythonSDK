# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657019e0
@llms.txt: https://napcat.apifox.cn/226657019e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群成员信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_member_info"
__id__ = "226657019e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupMemberInfoReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    user_id: float | str = Field(..., description="")
    no_cache: bool = Field(..., description="")
# region req/


# region res
class GetGroupMemberInfoRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetGroupMemberInfoAPI(BaseModel):
    
    Request : type[GetGroupMemberInfoReq] = GetGroupMemberInfoReq
    Response  : type[GetGroupMemberInfoRes] = GetGroupMemberInfoRes


# region api/
# region code/

