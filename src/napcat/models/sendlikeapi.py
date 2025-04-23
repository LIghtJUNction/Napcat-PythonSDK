# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226656717e0
@endpoint: send_like
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656717e0
@llms.txt: https://napcat.apifox.cn/226656717e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:54

@description: 

summary:点赞

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_like"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class SendLikeReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class SendLikeRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendLikeAPI(BaseModel):
    
    Request : type[SendLikeReq] = SendLikeReq
    Response  : type[SendLikeRes] = SendLikeRes


# region api/




# region code/

