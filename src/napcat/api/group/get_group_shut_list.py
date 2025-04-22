# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226659300e0
@endpoint: get_group_shut_list
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226659300e0
@llms.txt: https://napcat.apifox.cn/226659300e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: get_group_shut_list API
@usage: 使用 `client.get_group_shut_list()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_shut_list"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    -
    -
    -
    -
    -
    -
    -
    # 本行注释旨在测试构建清理逻辑


# region req
class GetGroupShutListReq(BaseHttpRequest):
    """
    get_group_shut_list 请求参数
    """

    pass
# region req/

# region data
class GetGroupShutListData(BaseModel):
    """
    get_group_shut_list 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupShutListRes(BaseHttpResponse[GetGroupShutListData]):
    """
    get_group_shut_list 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupShutListAPI(BaseHttpAPI[GetGroupShutListReq, GetGroupShutListRes]):
    """
    获取群禁言列表
    """
    api: str = "/get_group_shut_list"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupShutListReq
    Response = GetGroupShutListRes

    request: GetGroupShutListReq
    response: GetGroupShutListRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupShutListAPI)

# region code/

