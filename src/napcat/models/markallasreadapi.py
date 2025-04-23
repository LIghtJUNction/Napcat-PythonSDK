# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226659194e0
@endpoint: _mark_all_as_read
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659194e0
@llms.txt: https://napcat.apifox.cn/226659194e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:_设置所有消息已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_mark_all_as_read"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class MarkAllAsReadReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class MarkAllAsReadRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class MarkAllAsReadAPI(BaseModel):
    
    Request : type[MarkAllAsReadReq] = MarkAllAsReadReq
    Response  : type[MarkAllAsReadRes] = MarkAllAsReadRes


# region api/




# region code/

