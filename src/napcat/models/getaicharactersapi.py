# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229485683e0
@llms.txt: https://napcat.apifox.cn/229485683e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取AI语音人物

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_characters"
__id__ = "229485683e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetAiCharactersReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    chat_type: float | str = Field(..., description="")
# region req/


# region res
class GetAiCharactersRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetAiCharactersAPI(BaseModel):
    
    Request : type[GetAiCharactersReq] = GetAiCharactersReq
    Response  : type[GetAiCharactersRes] = GetAiCharactersRes


# region api/
# region code/

