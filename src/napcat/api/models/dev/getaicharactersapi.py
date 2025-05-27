# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229485683e0
@llms.txt: https://napcat.apifox.cn/229485683e0.md
@last_update: 2025-05-28 01:34:11

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
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
# Removed 'group_id' and 'result' component models
# as per OpenAPI specification, 'group_id' is a simple type (float | str)
# and 'result' is used as a base with 'data' field overridden in the response.

# region component_models/

# region req
class GetAiCharactersReq(BaseModel):
    """获取AI语音人物请求"""
    # 'group_id' changed to float | str based on OpenAPI 'oneOf' schema
    group_id: float | str = Field(description="标识ID")
    chat_type: float | str | None = Field(None, description="聊天类型，可选")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetAiCharactersRes(BaseModel):
    """获取AI语音人物响应"""

    class Character(BaseModel):
        """AI语音人物详情"""
        character_id: str = Field(description="人物ID")
        character_name: str = Field(description="人物名字")
        preview_url: str = Field(description="试听网址")

        model_config = {
            "extra": "allow",
        }

    class DataTypeItem(BaseModel):
        """响应数据项"""
        type: str = Field(description="类型")
        characters: list[Character] = Field(description="人物列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: list[DataTypeItem] = Field(description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetAiCharactersAPI(BaseModel):
    """get_ai_characters接口数据模型"""
    endpoint: str = "get_ai_characters"
    method: str = "POST"
    Req: type[BaseModel] = GetAiCharactersReq
    Res: type[BaseModel] = GetAiCharactersRes

# region api/
# endregion code
