# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 个人操作
@homepage: https://napcat.apifox.cn/229486818e0
@llms.txt: https://napcat.apifox.cn/229486818e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_record"
__id__ = "229486818e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetAiRecordReq(BaseModel):
    """
    获取AI语音请求模型
    """
    group_id: int | str = Field(..., description="群组ID")
    character: str = Field(..., description="character_id")
    text: str = Field(..., description="文本")
# endregion req



# region res
class GetAiRecordRes(BaseModel):
    """
    获取AI语音响应模型
    """
    status: Literal['ok'] = Field('ok', description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: str = Field(..., description="链接")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词")
    echo: str | None = Field(None, description="Echo")
# endregion res

# region api
class GetAiRecordAPI(BaseModel):
    """get_ai_record接口数据模型"""
    endpoint: str = "get_ai_record"
    method: str = "POST"
    Req: type[BaseModel] = GetAiRecordReq
    Res: type[BaseModel] = GetAiRecordRes
# endregion api




# endregion code
