# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 266151878e0
@endpoint: get_unidirectional_friend_list
@tags: 账号相关
@homepage: https://napcat.apifox.cn/266151878e0
@llms.txt: https://napcat.apifox.cn/266151878e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: get_unidirectional_friend_list API
@usage: 使用 `client.get_unidirectional_friend_list()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_unidirectional_friend_list"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetUnidirectionalFriendListReq(BaseHttpRequest):
    """
    get_unidirectional_friend_list 请求参数
    """

    pass
# region req/

# region data
class GetUnidirectionalFriendListData(BaseModel):
    """
    get_unidirectional_friend_list 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetUnidirectionalFriendListRes(BaseHttpResponse[list[GetUnidirectionalFriendListData]]):
    """
    get_unidirectional_friend_list 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetUnidirectionalFriendListAPI(BaseHttpAPI[GetUnidirectionalFriendListReq, GetUnidirectionalFriendListRes]):
    """
    获取单向好友列表
    """
    api: str = "/get_unidirectional_friend_list"
    method: Literal["POST", "GET"] = "POST"

    Request = GetUnidirectionalFriendListReq
    Response = GetUnidirectionalFriendListRes

    request: GetUnidirectionalFriendListReq
    response: GetUnidirectionalFriendListRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetUnidirectionalFriendListAPI)

# region code/

