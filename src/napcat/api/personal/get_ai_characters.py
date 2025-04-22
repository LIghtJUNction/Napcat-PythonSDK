# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 229485683e0
@endpoint: get_ai_characters
@tags: 个人操作
@homepage: https://napcat.apifox.cn/229485683e0
@llms.txt: https://napcat.apifox.cn/229485683e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_ai_characters API
@usage: 使用 `client.get_ai_characters()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_characters"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetAiCharactersReq(BaseHttpRequest):
    """
    get_ai_characters 请求参数
    """

    pass
# region req/

# region data
class GetAiCharactersData(BaseModel):
    """
    get_ai_characters 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetAiCharactersRes(BaseHttpResponse[list[GetAiCharactersData]]):
    """
    get_ai_characters 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
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
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetAiCharactersAPI)

# region code/

