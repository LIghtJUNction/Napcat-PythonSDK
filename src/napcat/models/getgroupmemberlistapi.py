# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657034e0
@llms.txt: https://napcat.apifox.cn/226657034e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群成员列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_member_list"
__id__ = "226657034e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupMemberListReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    no_cache: bool = Field(False, description="")
# region req/


# region res
class GetGroupMemberListRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetGroupMemberListAPI(BaseModel):
    
    Request : type[GetGroupMemberListReq] = GetGroupMemberListReq
    Response  : type[GetGroupMemberListRes] = GetGroupMemberListRes


# region api/
# region code/

