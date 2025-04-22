# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 283136236e0
@endpoint: get_rkey_server
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/283136236e0
@llms.txt: https://napcat.apifox.cn/283136236e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_rkey_server API
@usage: 使用 `client.get_rkey_server()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_rkey_server"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetRkeyServerReq(BaseHttpRequest):
    """
    get_rkey_server 请求参数
    """

    pass
# region req/

# region data
class GetRkeyServerData(BaseModel):
    """
    get_rkey_server 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetRkeyServerRes(BaseHttpResponse[GetRkeyServerData]):
    """
    get_rkey_server 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetRkeyServerAPI(BaseHttpAPI[GetRkeyServerReq, GetRkeyServerRes]):
    """
    获取rkey服务
    """
    api: str = "/get_rkey_server"
    method: Literal["POST", "GET"] = "POST"

    Request = GetRkeyServerReq
    Response = GetRkeyServerRes

    request: GetRkeyServerReq
    response: GetRkeyServerRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetRkeyServerAPI)

# region code/

