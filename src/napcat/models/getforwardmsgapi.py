# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226656712e0
@endpoint: get_forward_msg
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656712e0
@llms.txt: https://napcat.apifox.cn/226656712e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:54

@description: 

summary:获取合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_forward_msg"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class GetForwardMsgReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class GetForwardMsgRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetForwardMsgAPI(BaseModel):
    
    Request : type[GetForwardMsgReq] = GetForwardMsgReq
    Response  : type[GetForwardMsgRes] = GetForwardMsgRes


# region api/




# region code/

