# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229486818e0
@llms.txt: https://napcat.apifox.cn/229486818e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_record"
__id__ = "229486818e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetAiRecordReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    character: str = Field(..., description="character_id")
    text: str = Field(..., description="文本")
# region req/


# region res
class GetAiRecordRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetAiRecordAPI(BaseModel):
    
    Request : type[GetAiRecordReq] = GetAiRecordReq
    Response  : type[GetAiRecordRes] = GetAiRecordRes


# region api/
# region code/

