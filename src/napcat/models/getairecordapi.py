# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 229486818e0
@endpoint: get_ai_record
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229486818e0
@llms.txt: https://napcat.apifox.cn/229486818e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:获取AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_record"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class GetAiRecordReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class GetAiRecordRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetAiRecordAPI(BaseModel):
    
    Request : type[GetAiRecordReq] = GetAiRecordReq
    Response  : type[GetAiRecordRes] = GetAiRecordRes


# region api/




# region code/

