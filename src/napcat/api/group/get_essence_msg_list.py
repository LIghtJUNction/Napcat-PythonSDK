# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 165
@api_id: 226658664e0
@endpoint: get_essence_msg_list
@tags: 群聊相关
@homepage: https://api.napcat.com/226658664e0
@llms.txt: https://api.napcat.com/226658664e0.md
@version: 4.7.17
@last_update: 2025-04-22 22:32:34

@description: get_essence_msg_list API
@usage: 使用 `client.get_essence_msg_list()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_essence_msg_list"
__method__ = "POST"


# region {
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    # 示例 endpoint : send_group_message  特殊 endpoint : _开头 .开头 给类命名时 .忽略即可(如 _get_model_show -> GetModelShowAPI)
    # 示例 class : SendGroupMessageAPI
    # 示例 request : SendGroupMessageReq
    # 示例 response : SendGroupMessageRes
    # 示例 data : SendGroupMessageData
    # 请将你需要展示给用户的注释符："#"放置于行首
    # 否则将被清理掉


# request model
class GetEssenceMsgListReq(BaseHttpRequest):
    """
    get_essence_msg_list 请求参数
    """

    pass


class GetEssenceMsgListData(BaseModel):
    """
    get_essence_msg_list 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# response model
class GetEssenceMsgListRes(BaseHttpResponse[GetEssenceMsgListData]):
    """
    get_essence_msg_list 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# API class
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
    

if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetEssenceMsgListAPI)

# region }

