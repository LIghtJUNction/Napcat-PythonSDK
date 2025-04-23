# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657087e0
@llms.txt: https://napcat.apifox.cn/226657087e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取版本信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_version_info"
__id__ = "226657087e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetVersionInfoReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class GetVersionInfoRes(BaseModel):
    """
    响应参数
    """

    app_name: str = Field(..., description="")
    protocol_version: str = Field(..., description="")
    app_version: str = Field(..., description="")
# region res/

# region api
class GetVersionInfoAPI(BaseModel):
    
    Request : type[GetVersionInfoReq] = GetVersionInfoReq
    Response  : type[GetVersionInfoRes] = GetVersionInfoRes


# region api/
# region code/

