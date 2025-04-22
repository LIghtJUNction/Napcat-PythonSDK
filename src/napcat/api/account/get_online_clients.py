# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 165
@api_id: 226657379e0
@endpoint: get_online_clients
@tags: 账号相关
@homepage: https://api.napcat.com/226657379e0
@llms.txt: https://api.napcat.com/226657379e0.md
@version: 4.7.17
@last_update: 2025-04-22 22:32:33

@description: get_online_clients API
@usage: 使用 `client.get_online_clients()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_online_clients"
__method__ = "POST"


# region {
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    # 示例 endpoint : send_group_message  特殊 endpoint : _开头 .开头 给类命名时 .忽略即可(如 _get_model_show -> GetModelShowAPI)
    # 示例 class : SendGroupMessageAPI
    # 示例 request : SendGroupMessageReq
    # 示例 response : SendGroupMessageRes
    # 示例 data : SendGroupMessageData
    # 请将你需要展示给用户的注释符："#"放置于行首
    # 否则将被清理掉


# request model
class GetOnlineClientsReq(BaseHttpRequest):
    """
    get_online_clients 请求参数
    """

    pass


class GetOnlineClientsData(BaseModel):
    """
    get_online_clients 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# response model
class GetOnlineClientsRes(BaseHttpResponse[GetOnlineClientsData]):
    """
    get_online_clients 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# API class
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
    

if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetOnlineClientsAPI)

# region }

