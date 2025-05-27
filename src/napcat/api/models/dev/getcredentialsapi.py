# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657054e0
@llms.txt: https://napcat.apifox.cn/226657054e0.md
@last_update: 2025-05-28 01:34:09

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
from typing import Any, Literal

# region component_models
class result(BaseModel):
    """
    通用结果模型，通常用于表示API响应的基础结构。
    请注意：此模型中的`data`字段为通用类型，
    具体API响应中的`data`结构可能不同。
    """
    status: Literal["ok"] = Field(description="status字段，固定为 'ok'")
    retcode: float = Field(description="返回码")
    data: dict[str, Any] = Field(description="响应数据，具体结构取决于API")
    message: str = Field(description="消息")
    wording: str = Field(description="提示词")
    echo: str | None = Field(default=None, description="回显字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetCredentialsReq(BaseModel):
    """获取 QQ 相关接口凭证的请求模型"""
    domain: str = Field(description="域名")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetCredentialsRes(BaseModel):
    """获取 QQ 相关接口凭证的响应模型"""
    class Data(BaseModel):
        """响应数据类型"""
        cookies: str = Field(description="cookies字段")
        token: float = Field(description="token字段")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="status字段，固定为 'ok'")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: Data = Field(default_factory=Data, description="data字段，包含cookies和token")
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
