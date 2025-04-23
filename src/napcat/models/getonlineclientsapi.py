# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226657379e0
@endpoint: get_online_clients
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657379e0
@llms.txt: https://napcat.apifox.cn/226657379e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:54

@description: 

summary:获取当前账号在线客户端列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_online_clients"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class GetOnlineClientsReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class GetOnlineClientsRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetOnlineClientsAPI(BaseModel):
    
    Request : type[GetOnlineClientsReq] = GetOnlineClientsReq
    Response  : type[GetOnlineClientsRes] = GetOnlineClientsRes


# region api/




# region code/

