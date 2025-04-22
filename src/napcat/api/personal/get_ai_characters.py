# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 165
@api_id: 229485683e0
@endpoint: get_ai_characters
@tags: 个人操作
@homepage: https://api.napcat.com/229485683e0
@llms.txt: https://api.napcat.com/229485683e0.md
@version: 4.7.17
@last_update: 2025-04-22 22:32:34

@description: get_ai_characters API
@usage: 使用 `client.get_ai_characters()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_characters"
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
class GetAiCharactersReq(BaseHttpRequest):
    """
    get_ai_characters 请求参数
    """

    pass


class GetAiCharactersData(BaseModel):
    """
    get_ai_characters 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# response model
class GetAiCharactersRes(BaseHttpResponse[GetAiCharactersData]):
    """
    get_ai_characters 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# API class
class GetAiCharactersAPI(BaseHttpAPI[GetAiCharactersReq, GetAiCharactersRes]):
    """
    获取AI语音人物
    """
    api: str = "/get_ai_characters"
    method: Literal["POST", "GET"] = "POST"

    Request = GetAiCharactersReq
    Response = GetAiCharactersRes

    request: GetAiCharactersReq
    response: GetAiCharactersRes
    

if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetAiCharactersAPI)

# region }

