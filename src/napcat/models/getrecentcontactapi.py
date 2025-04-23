# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226659190e0
@endpoint: get_recent_contact
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659190e0
@llms.txt: https://napcat.apifox.cn/226659190e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 获取的最新消息是每个会话最新的消息

summary:最近消息列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_recent_contact"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class GetRecentContactReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class GetRecentContactRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetRecentContactAPI(BaseModel):
    
    Request : type[GetRecentContactReq] = GetRecentContactReq
    Response  : type[GetRecentContactRes] = GetRecentContactRes


# region api/




# region code/

