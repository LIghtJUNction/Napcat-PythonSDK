# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659182e0
@endpoint: get_collection_list
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659182e0
@llms.txt: https://napcat.apifox.cn/226659182e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_collection_list API
@usage: 使用 `client.get_collection_list()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_collection_list"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetCollectionListReq(BaseHttpRequest):
    """
    get_collection_list 请求参数
    """

    pass
# region req/

# region data
class GetCollectionListData(BaseModel):
    """
    get_collection_list 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetCollectionListRes(BaseHttpResponse[list[GetCollectionListData]]):
    """
    get_collection_list 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetCollectionListAPI(BaseHttpAPI[GetCollectionListReq, GetCollectionListRes]):
    """
    获取收藏列表
    """
    api: str = "/get_collection_list"
    method: Literal["POST", "GET"] = "POST"

    Request = GetCollectionListReq
    Response = GetCollectionListRes

    request: GetCollectionListReq
    response: GetCollectionListRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetCollectionListAPI)

# region code/

