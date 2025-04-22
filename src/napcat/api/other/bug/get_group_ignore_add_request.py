# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659234e0
@endpoint: get_group_ignore_add_request
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659234e0
@llms.txt: https://napcat.apifox.cn/226659234e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_group_ignore_add_request API
@usage: 使用 `client.get_group_ignore_add_request()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_ignore_add_request"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetGroupIgnoreAddRequestReq(BaseHttpRequest):
    """
    get_group_ignore_add_request 请求参数
    """

    pass
# region req/

# region data
class GetGroupIgnoreAddRequestData(BaseModel):
    """
    get_group_ignore_add_request 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupIgnoreAddRequestRes(BaseHttpResponse[list[GetGroupIgnoreAddRequestData]]):
    """
    get_group_ignore_add_request 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupIgnoreAddRequestAPI(BaseHttpAPI[GetGroupIgnoreAddRequestReq, GetGroupIgnoreAddRequestRes]):
    """
    获取被过滤的加群请求
    """
    api: str = "/get_group_ignore_add_request"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupIgnoreAddRequestReq
    Response = GetGroupIgnoreAddRequestRes

    request: GetGroupIgnoreAddRequestReq
    response: GetGroupIgnoreAddRequestRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupIgnoreAddRequestAPI)

# region code/

