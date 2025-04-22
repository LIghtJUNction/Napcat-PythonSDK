# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226657087e0
@endpoint: get_version_info
@tags: 系统操作
@homepage: https://napcat.apifox.cn/226657087e0
@llms.txt: https://napcat.apifox.cn/226657087e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_version_info API
@usage: 使用 `client.get_version_info()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_version_info"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetVersionInfoReq(BaseHttpRequest):
    """
    get_version_info 请求参数
    """

    pass
# region req/

# region data
class GetVersionInfoData(BaseModel):
    """
    get_version_info 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetVersionInfoRes(BaseHttpResponse[GetVersionInfoData]):
    """
    get_version_info 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetVersionInfoAPI(BaseHttpAPI[GetVersionInfoReq, GetVersionInfoRes]):
    """
    获取版本信息
    """
    api: str = "/get_version_info"
    method: Literal["POST", "GET"] = "POST"

    Request = GetVersionInfoReq
    Response = GetVersionInfoRes

    request: GetVersionInfoReq
    response: GetVersionInfoRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetVersionInfoAPI)

# region code/

