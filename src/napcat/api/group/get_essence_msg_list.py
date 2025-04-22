# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226658664e0
@endpoint: get_essence_msg_list
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658664e0
@llms.txt: https://napcat.apifox.cn/226658664e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: get_essence_msg_list API
@usage: 使用 `client.get_essence_msg_list()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_essence_msg_list"
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
class GetEssenceMsgListReq(BaseHttpRequest):
    """
    get_essence_msg_list 请求参数
    """

    pass
# region req/

# region data
class GetEssenceMsgListData(BaseModel):
    """
    get_essence_msg_list 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetEssenceMsgListRes(BaseHttpResponse[list[GetEssenceMsgListData]]):
    """
    get_essence_msg_list 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetEssenceMsgListAPI(BaseHttpAPI[GetEssenceMsgListReq, GetEssenceMsgListRes]):
    """
    获取群精华消息
    """
    api: str = "/get_essence_msg_list"
    method: Literal["POST", "GET"] = "POST"

    Request = GetEssenceMsgListReq
    Response = GetEssenceMsgListRes

    request: GetEssenceMsgListReq
    response: GetEssenceMsgListRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetEssenceMsgListAPI)

# region code/

