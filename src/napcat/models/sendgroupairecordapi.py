# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229486774e0
@llms.txt: https://napcat.apifox.cn/229486774e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:发送群AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_ai_record"
__id__ = "229486774e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendGroupAiRecordReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    character: str = Field(..., description="character_id")
    text: str = Field(..., description="文本")
# region req/


# region res
class SendGroupAiRecordRes(BaseModel):
    """
    响应参数
    """

    message_id: str = Field(..., description="")
# region res/

# region api
class SendGroupAiRecordAPI(BaseModel):
    
    Request : type[SendGroupAiRecordReq] = SendGroupAiRecordReq
    Response  : type[SendGroupAiRecordRes] = SendGroupAiRecordRes


# region api/
# region code/

