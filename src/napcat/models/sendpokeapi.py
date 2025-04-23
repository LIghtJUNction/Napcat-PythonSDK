# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/250286923e0
@llms.txt: https://napcat.apifox.cn/250286923e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:发送戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_poke"
__id__ = "250286923e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendPokeReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="必填")
    group_id: float | str | None = Field(None, description="不填则为私聊戳")
# region req/


# region res
class SendPokeRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SendPokeAPI(BaseModel):
    
    Request : type[SendPokeReq] = SendPokeReq
    Response  : type[SendPokeRes] = SendPokeRes


# region api/
# region code/

