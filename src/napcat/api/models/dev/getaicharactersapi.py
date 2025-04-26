# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['个人操作']
@homepage: https://napcat.apifox.cn/229485683e0
@llms.txt: https://napcat.apifox.cn/229485683e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取AI语音人物

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_ai_characters"
__id__ = "229485683e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # For status 'ok'

logger = logging.getLogger(__name__)

# region req
class GetAiCharactersReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """
    group_id: int | str = Field(..., description="群组ID")
    chat_type: int | str | None = Field(None, description="聊天类型")
# endregion req



# region res
class CharacterItem(BaseModel):
    """AI语音人物详情"""
    character_id: str = Field(..., description="人物ID")
    character_name: str = Field(..., description="人物名字")
    preview_url: str = Field(..., description="试听网址")

class DataItem(BaseModel):
    """AI语音人物分组"""
    type: str = Field(..., description="类型")
    characters: list[CharacterItem] = Field(..., description="人物列表")

class GetAiCharactersRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[DataItem] = Field(..., description="AI语音人物列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="补充说明")
    echo: str | None = Field(None, description="回显") # Nullable means it can be None
# endregion res

# region api
class GetAiCharactersAPI(BaseModel):
    """get_ai_characters接口数据模型"""
    endpoint: str = "get_ai_characters"
    method: str = "POST"
    Req: type[BaseModel] = GetAiCharactersReq
    Res: type[BaseModel] = GetAiCharactersRes
# endregion api




# endregion code
