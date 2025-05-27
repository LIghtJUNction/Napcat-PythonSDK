# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229486818e0
@llms.txt: https://napcat.apifox.cn/229486818e0.md
@last_update: 2025-05-28 01:34:11

@description:

summary:获取AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_ai_record"
__id__ = "229486818e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
# The original 'group_id' BaseModel was incorrect as per OpenAPI spec. 
# OpenAPI defines 'group_id' as 'oneOf: [number, string]', a primitive type.
# So, it's handled directly in GetAiRecordReq as 'int | str'.

class result(BaseModel):
    status: Literal["ok"] = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    # According to components/schemas/result in OpenAPI, data is an empty object
    data: dict[str, any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetAiRecordReq(BaseModel):
    """获取AI语音"""
    # 'group_id' is defined as 'oneOf: [number, string]' in OpenAPI components/schemas/group_id
    group_id: int | str = Field(description="标识ID (可以是数字或字符串)")
    character: str = Field(description="character_id")
    text: str = Field(description="文本")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetAiRecordRes(BaseModel):
    """获取AI语音"""
    # The 'data' field in this specific response is overridden to be a string,
    # despite the generic 'result' component defining it as an object.
    status: Literal["ok"] = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    # As per OpenAPI spec for /get_ai_record response, 'data' is a string '链接'
    data: str = Field(default="", description="链接")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetAiRecordAPI(BaseModel):
    """get_ai_record接口数据模型"""
    endpoint: str = "get_ai_record"
    method: str = "POST"
    Req: type[BaseModel] = GetAiRecordReq
    Res: type[BaseModel] = GetAiRecordRes

# region api/
# endregion code
