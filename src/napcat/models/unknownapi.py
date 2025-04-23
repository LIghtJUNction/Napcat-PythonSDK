# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658925e0
@llms.txt: https://napcat.apifox.cn/226658925e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:unknown

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "unknown"
__id__ = "226658925e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req

# region req/


# region res
class UnknownRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class UnknownAPI(BaseModel):
    
    Request : type[UnknownReq] = UnknownReq
    Response  : type[UnknownRes] = UnknownRes


# region api/
# region code/

