# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136236e0
@llms.txt: https://napcat.apifox.cn/283136236e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:获取rkey服务

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_rkey_server"
__id__ = "283136236e0"
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
class GetRkeyServerReq(BaseModel):
    """获取rkey服务"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetRkeyServerRes(BaseModel):
    """获取rkey服务"""
    class Data(BaseModel):
        """响应数据类型"""
        private_rkey: str = Field(default=None, description="private_rkey字段")
        group_rkey: str = Field(default=None, description="group_rkey字段")
        expired_time: float = Field(default=None, description="expired_time字段")
        name: str = Field(default=None, description="name字段")

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
class GetRkeyServerAPI(BaseModel):
    """get_rkey_server接口数据模型"""
    endpoint: str = "get_rkey_server"
    method: str = "POST"
    Req: type[BaseModel] = GetRkeyServerReq
    Res: type[BaseModel] = GetRkeyServerRes

# region api/
# endregion code

