# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658669e0
@llms.txt: https://napcat.apifox.cn/226658669e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置群头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_portrait"
__id__ = "226658669e0"
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
class SetGroupPortraitReq(BaseModel):
    """设置群头像"""
    group_id: group_id
    file: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SetGroupPortraitRes(BaseModel):
    """设置群头像"""
    class Data(BaseModel):
        """响应数据类型"""
        result: str = Field(default=None, description="result字段")
        errMsg: str = Field(default=None, description="errMsg字段")

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
class SetGroupPortraitAPI(BaseModel):
    """set_group_portrait接口数据模型"""
    endpoint: str = "set_group_portrait"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupPortraitReq
    Res: type[BaseModel] = SetGroupPortraitRes

# region api/
# endregion code

