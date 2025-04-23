# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659311e0
@llms.txt: https://napcat.apifox.cn/226659311e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:get_guild_list

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_guild_list"
__id__ = "226659311e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req

# region req/


# region res
class GetGuildListRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetGuildListAPI(BaseModel):
    
    Request : type[GetGuildListReq] = GetGuildListReq
    Response  : type[GetGuildListRes] = GetGuildListRes


# region api/
# region code/

