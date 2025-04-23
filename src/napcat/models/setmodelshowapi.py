# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 227233993e0
@endpoint: _set_model_show
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227233993e0
@llms.txt: https://napcat.apifox.cn/227233993e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:_设置在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_set_model_show"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class SetModelShowReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class SetModelShowRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetModelShowAPI(BaseModel):
    
    Request : type[SetModelShowReq] = SetModelShowReq
    Response  : type[SetModelShowRes] = SetModelShowRes


# region api/




# region code/

