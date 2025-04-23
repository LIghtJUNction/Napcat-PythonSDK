# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226658742e0
@endpoint: _get_group_notice
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658742e0
@llms.txt: https://napcat.apifox.cn/226658742e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:_获取群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_get_group_notice"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class GetGroupNoticeReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class GetGroupNoticeRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupNoticeAPI(BaseModel):
    
    Request : type[GetGroupNoticeReq] = GetGroupNoticeReq
    Response  : type[GetGroupNoticeRes] = GetGroupNoticeRes


# region api/




# region code/

