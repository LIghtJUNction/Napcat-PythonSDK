# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656952e0
@llms.txt: https://napcat.apifox.cn/226656952e0.md
@last_update: 2025-05-28 01:34:08

@description:

summary:获取登录号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_login_info"
__id__ = "226656952e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any, Literal

# region component_models
class result(BaseModel):
    status: Literal["ok"] = Field("ok", description="status字段")
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
class GetLoginInfoReq(BaseModel):
    """获取登录号信息"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetLoginInfoRes(BaseModel):
    """获取登录号信息"""
    class Data(BaseModel):
        """响应数据类型"""
        user_id: float = Field(description="user_id字段") # Removed default=None as it's required
        nickname: str = Field(description="nickname字段") # Removed default=None as it's required

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="status字段") # Changed to Literal["ok"]
    retcode: float = Field(0.0, description="retcode字段") # Ensured default is float
    data: Data = Field(default_factory=Data, description="data字段") # Correct default_factory
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetLoginInfoAPI(BaseModel):
    """get_login_info接口数据模型"""
    endpoint: str = "get_login_info"
    method: str = "POST"
    Req: type[BaseModel] = GetLoginInfoReq
    Res: type[BaseModel] = GetLoginInfoRes

# region api/
# endregion code
