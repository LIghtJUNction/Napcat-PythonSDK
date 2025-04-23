# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657379e0
@llms.txt: https://napcat.apifox.cn/226657379e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取当前账号在线客户端列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_online_clients"
__id__ = "226657379e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetOnlineClientsReq(BaseModel):
    """
    请求参数
    """

    no_cache: bool = Field(False, description="")
# region req/


# region res
class GetOnlineClientsRes(BaseModel):
    """
    响应参数
    """

    clients: dict | None = Field(None, description="")
# region res/

# region api
class GetOnlineClientsAPI(BaseModel):
    
    Request : type[GetOnlineClientsReq] = GetOnlineClientsReq
    Response  : type[GetOnlineClientsRes] = GetOnlineClientsRes


# region api/
# region code/

