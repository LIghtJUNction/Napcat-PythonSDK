# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226657379e0
@endpoint: get_online_clients
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657379e0
@llms.txt: https://napcat.apifox.cn/226657379e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: get_online_clients API
@usage: 使用 `client.get_online_clients()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_online_clients"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetOnlineClientsReq(BaseHttpRequest):
    """
    get_online_clients 请求参数
    """

    pass
# region req/

# region data
class GetOnlineClientsData(BaseModel):
    """
    get_online_clients 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetOnlineClientsRes(BaseHttpResponse[GetOnlineClientsData]):
    """
    get_online_clients 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetOnlineClientsAPI(BaseHttpAPI[GetOnlineClientsReq, GetOnlineClientsRes]):
    """
    获取当前账号在线客户端列表
    """
    api: str = "/get_online_clients"
    method: Literal["POST", "GET"] = "POST"

    Request = GetOnlineClientsReq
    Response = GetOnlineClientsRes

    request: GetOnlineClientsReq
    response: GetOnlineClientsRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetOnlineClientsAPI)

# region code/

