# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226656976e0
@endpoint: get_friend_list
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656976e0
@llms.txt: https://napcat.apifox.cn/226656976e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: get_friend_list API
@usage: 使用 `client.get_friend_list()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friend_list"
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
class GetFriendListReq(BaseHttpRequest):
    """
    get_friend_list 请求参数
    """

    pass
# region req/

# region data
class GetFriendListData(BaseModel):
    """
    get_friend_list 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetFriendListRes(BaseHttpResponse[list[GetFriendListData]]):
    """
    get_friend_list 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetFriendListAPI(BaseHttpAPI[GetFriendListReq, GetFriendListRes]):
    """
    获取好友列表
    """
    api: str = "/get_friend_list"
    method: Literal["POST", "GET"] = "POST"

    Request = GetFriendListReq
    Response = GetFriendListRes

    request: GetFriendListReq
    response: GetFriendListRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetFriendListAPI)

# region code/

