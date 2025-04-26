# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657054e0
@llms.txt: https://napcat.apifox.cn/226657054e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取 QQ 相关接口凭证

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_credentials"
__id__ = "226657054e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
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
class GetCredentialsReq(BaseModel):
    """获取 QQ 相关接口凭证"""
    domain: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetCredentialsRes(BaseModel):
    """获取 QQ 相关接口凭证"""
    class Data(BaseModel):
        """响应数据类型"""
        cookies: str = Field(default=None, description="cookies字段")
        token: float = Field(default=None, description="token字段")

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
class GetCredentialsAPI(BaseModel):
    """get_credentials接口数据模型"""
    endpoint: str = "get_credentials"
    method: str = "POST"
    Req: type[BaseModel] = GetCredentialsReq
    Res: type[BaseModel] = GetCredentialsRes

# region api/
# endregion code

