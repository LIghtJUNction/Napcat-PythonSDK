# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657041e0
@llms.txt: https://napcat.apifox.cn/226657041e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取cookies

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_cookies"
__id__ = "226657041e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal, Any

# region component_models
class Result(BaseModel):
    """通用响应结果模型"""
    status: Literal["ok"] = Field(description="状态码，固定为'ok'")
    retcode: float = Field(description="返回码")
    data: dict[str, Any] = Field(description="数据字段，通用类型为字典")
    message: str = Field(description="消息")
    wording: str = Field(description="提示词")
    echo: str | None = Field(description="回显字段")

    model_config = {
        "extra": "allow",
    }
# endregion component_models


# region req
class GetCookiesReq(BaseModel):
    """获取cookies请求"""
    domain: str = Field(description="请求的域名")

    model_config = {
        "extra": "allow",
    }
# endregion req


# region res
class GetCookiesRes(BaseModel):
    """获取cookies响应"""
    class Data(BaseModel):
        """响应数据类型"""
        cookies: str = Field(description="cookies字符串")
        bkn: str = Field(description="bkn字符串")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(default="ok", description="status字段，固定为'ok'")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: Data = Field(default_factory=Data, description="data字段，包含cookies和bkn")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# endregion res

# region api
class GetCookiesAPI(BaseModel):
    """get_cookies接口数据模型"""
    endpoint: str = "get_cookies"
    method: str = "POST"
    Req: type[BaseModel] = GetCookiesReq
    Res: type[BaseModel] = GetCookiesRes

# endregion api
