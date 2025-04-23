# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656717e0
@llms.txt: https://napcat.apifox.cn/226656717e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:点赞

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_like"
__id__ = "226656717e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendLikeReq(BaseModel):
    """
    请求参数
    """

    user_id: str | float = Field(..., description="")
    times: float = Field(..., description="点赞次数")
# region req/


# region res
class SendLikeRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SendLikeAPI(BaseModel):
    
    Request : type[SendLikeReq] = SendLikeReq
    Response  : type[SendLikeRes] = SendLikeRes


# region api/
# region code/

