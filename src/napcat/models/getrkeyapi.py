# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136230e0
@llms.txt: https://napcat.apifox.cn/283136230e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取rkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_rkey"
__id__ = "283136230e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetRkeyReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetRkeyRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetRkeyAPI(BaseModel):
    
    Request : type[GetRkeyReq] = GetRkeyReq
    Response  : type[GetRkeyRes] = GetRkeyRes


# region api/
# region code/

