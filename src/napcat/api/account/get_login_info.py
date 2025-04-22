# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226656952e0
@endpoint: get_login_info
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656952e0
@llms.txt: https://napcat.apifox.cn/226656952e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: get_login_info API
@usage: 使用 `client.get_login_info()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_login_info"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetLoginInfoReq(BaseHttpRequest):
    """
    get_login_info 请求参数
    """

    pass
# region req/

# region data
class GetLoginInfoData(BaseModel):
    """
    get_login_info 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetLoginInfoRes(BaseHttpResponse[GetLoginInfoData]):
    """
    get_login_info 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetLoginInfoAPI(BaseHttpAPI[GetLoginInfoReq, GetLoginInfoRes]):
    """
    获取登录号信息
    """
    api: str = "/get_login_info"
    method: Literal["POST", "GET"] = "POST"

    Request = GetLoginInfoReq
    Response = GetLoginInfoRes

    request: GetLoginInfoReq
    response: GetLoginInfoRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetLoginInfoAPI)

# region code/

