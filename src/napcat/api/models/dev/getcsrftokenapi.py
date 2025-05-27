# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657044e0
@llms.txt: https://napcat.apifox.cn/226657044e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取 CSRF Token

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_csrf_token"
__id__ = "226657044e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Added for Literal type

# region component_models
class Result(BaseModel): # Renamed to CamelCase
    """Generic result structure from OpenAPI components/schemas"""
    status: Literal["ok"] = Field(description="status字段") # Based on const: ok in OpenAPI schema, Pydantic handles default
    retcode: float = Field(description="retcode字段") # Required
    data: dict = Field(description="data字段") # Changed from dict[str, Any] to dict
    message: str = Field(description="message字段") # Required
    wording: str = Field(description="wording字段") # Required
    echo: str | None = Field(description="echo字段") # Required, but nullable

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetCsrfTokenReq(BaseModel):
    """获取 CSRF Token"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetCsrfTokenRes(BaseModel):
    """获取 CSRF Token"""
    class Data(BaseModel):
        """响应数据类型"""
        token: float = Field(description="token字段") # Required, no default as per OpenAPI 'required: [token]'

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="status字段") # Use Literal and provide default
    retcode: float = Field(0, description="retcode字段") # Default 0 as per OpenAPI example
    data: Data = Field(default_factory=Data, description="data字段") # Using default_factory for nested model
    message: str = Field("", description="message字段") # Default "" as per OpenAPI example
    wording: str = Field("", description="wording字段") # Default "" as per OpenAPI example
    echo: str | None = Field(None, description="echo字段") # Default None for nullable field

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetCsrfTokenAPI(BaseModel):
    """get_csrf_token接口数据模型"""
    endpoint: str = "get_csrf_token"
    method: str = "POST"
    Req: type[BaseModel] = GetCsrfTokenReq
    Res: type[BaseModel] = GetCsrfTokenRes

# region api/
# endregion code
