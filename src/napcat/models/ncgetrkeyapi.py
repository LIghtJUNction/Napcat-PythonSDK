# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659297e0
@llms.txt: https://napcat.apifox.cn/226659297e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:nc获取rkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_rkey"
__id__ = "226659297e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class NcGetRkeyReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class NcGetRkeyRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class NcGetRkeyAPI(BaseModel):
    
    Request : type[NcGetRkeyReq] = NcGetRkeyReq
    Response  : type[NcGetRkeyRes] = NcGetRkeyRes


# region api/
# region code/

