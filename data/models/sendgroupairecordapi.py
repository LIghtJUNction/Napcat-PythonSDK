# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229486774e0
@llms.txt: https://napcat.apifox.cn/229486774e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:发送群AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_group_ai_record"
__id__ = "229486774e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class SendGroupAiRecordReq(BaseModel):
    """发送群AI语音"""
    group_id: group_id
    character: str = Field(description="character_id")
    text: str = Field(description="文本")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SendGroupAiRecordRes(BaseModel):
    """发送群AI语音"""
    class Data(BaseModel):
        """响应数据类型"""
        message_id: str = Field(default=None, description="message_id字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class SendGroupAiRecordAPI(BaseModel):
    """send_group_ai_record接口数据模型"""
    endpoint: str = "send_group_ai_record"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupAiRecordReq
    Res: type[BaseModel] = SendGroupAiRecordRes

# region api/
# endregion code

