# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658742e0
@llms.txt: https://napcat.apifox.cn/226658742e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:_获取群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_get_group_notice"
__id__ = "226658742e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupNoticeReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupNoticeRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetGroupNoticeAPI(BaseModel):
    
    Request : type[GetGroupNoticeReq] = GetGroupNoticeReq
    Response  : type[GetGroupNoticeRes] = GetGroupNoticeRes


# region api/
# region code/

