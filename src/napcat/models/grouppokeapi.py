# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659265e0
@llms.txt: https://napcat.apifox.cn/226659265e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:发送群聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "group_poke"
__id__ = "226659265e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GroupPokeReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    user_id: float | str = Field(..., description="")
# region req/


# region res
class GroupPokeRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GroupPokeAPI(BaseModel):
    
    Request : type[GroupPokeReq] = GroupPokeReq
    Response  : type[GroupPokeRes] = GroupPokeRes


# region api/
# region code/

