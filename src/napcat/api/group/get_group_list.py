# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226656992e0
@endpoint: get_group_list
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656992e0
@llms.txt: https://napcat.apifox.cn/226656992e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: get_group_list API
@usage: 使用 `client.get_group_list()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_list"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetGroupListReq(BaseHttpRequest):
    """
    get_group_list 请求参数
    """

    pass
# region req/

# region data
class GetGroupListData(BaseModel):
    """
    get_group_list 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupListRes(BaseHttpResponse[list[GetGroupListData]]):
    """
    get_group_list 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupListAPI(BaseHttpAPI[GetGroupListReq, GetGroupListRes]):
    """
    获取群列表
    """
    api: str = "/get_group_list"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupListReq
    Response = GetGroupListRes

    request: GetGroupListReq
    response: GetGroupListRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupListAPI)

# region code/

