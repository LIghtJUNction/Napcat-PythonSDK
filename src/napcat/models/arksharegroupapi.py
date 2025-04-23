# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658971e0
@llms.txt: https://napcat.apifox.cn/226658971e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取推荐群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "ArkShareGroup"
__id__ = "226658971e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class ArksharegroupReq(BaseModel):
    """
    请求参数
    """

    group_id: str = Field(..., description="")
# region req/


# region res
class ArksharegroupRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class ArksharegroupAPI(BaseModel):
    
    Request : type[ArksharegroupReq] = ArksharegroupReq
    Response  : type[ArksharegroupRes] = ArksharegroupRes


# region api/
# region code/

