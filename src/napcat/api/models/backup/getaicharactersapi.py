# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 个人操作
@homepage: https://napcat.apifox.cn/229485683e0
@llms.txt: https://napcat.apifox.cn/229485683e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取AI语音人物

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_ai_characters"
__id__ = "229485683e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetAiCharactersReq(BaseModel):
    """
    获取AI语音人物请求模型
    """

    group_id: int | str = Field(
        ..., description="群组ID"
    ) # Using Union[int, str] for group_id as per spec
    chat_type: int | str = Field(
        ..., description="聊天类型，0:私聊 1:群聊"
    ) # Using Union[int, str] for chat_type as per spec

# endregion req


# region res

class Character(BaseModel):
    """
    AI语音人物模型
    """
    character_id: str = Field(..., description="人物ID")
    character_name: str = Field(..., description="人物名字")
    preview_url: str = Field(..., description="试听网址")


class CharacterType(BaseModel):
    """
    AI语音人物类型模型
    """
    type: str = Field(..., description="类型")
    characters: list[Character] = Field(..., description="人物列表")


class GetAiCharactersRes(BaseModel):
    """
    获取AI语音人物响应模型
    """

    status: str = Field(..., description="状态，'ok'表示成功")
    retcode: int = Field(..., description="返回码")
    data: list[CharacterType] = Field(
        ..., description="AI语音人物数据列表"
    )
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="附加消息")
    echo: str | None = Field(None, description="Echo字段") # Nullable field


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
