# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658980e0
@llms.txt: https://napcat.apifox.cn/226658980e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_qq_avatar"
__id__ = "226658980e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SetQqAvatarReq(BaseModel):
    """
    请求参数
    """

    file: str = Field(..., description="路径或链接")
# region req/


# region res
class SetQqAvatarRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetQqAvatarAPI(BaseModel):
    
    Request : type[SetQqAvatarReq] = SetQqAvatarReq
    Response  : type[SetQqAvatarRes] = SetQqAvatarRes


# region api/
# region code/

