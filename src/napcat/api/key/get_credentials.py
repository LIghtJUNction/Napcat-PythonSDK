# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226657054e0
@endpoint: get_credentials
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/226657054e0
@llms.txt: https://napcat.apifox.cn/226657054e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_credentials API
@usage: 使用 `client.get_credentials()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_credentials"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetCredentialsReq(BaseHttpRequest):
    """
    get_credentials 请求参数
    """

    pass
# region req/

# region data
class GetCredentialsData(BaseModel):
    """
    get_credentials 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetCredentialsRes(BaseHttpResponse[GetCredentialsData]):
    """
    get_credentials 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetCredentialsAPI(BaseHttpAPI[GetCredentialsReq, GetCredentialsRes]):
    """
    获取 QQ 相关接口凭证
    """
    api: str = "/get_credentials"
    method: Literal["POST", "GET"] = "POST"

    Request = GetCredentialsReq
    Response = GetCredentialsRes

    request: GetCredentialsReq
    response: GetCredentialsRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetCredentialsAPI)

# region code/

