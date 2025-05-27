# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657087e0
@llms.txt: https://napcat.apifox.cn/226657087e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取版本信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_version_info"
__id__ = "226657087e0"
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
class GetVersionInfoReq(BaseModel):
    """获取版本信息"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetVersionInfoRes(BaseModel):
    """获取版本信息"""
    class Data(BaseModel):
        """响应数据类型"""
        app_name: str = Field(default=None, description="app_name字段")
        protocol_version: str = Field(default=None, description="protocol_version字段")
        app_version: str = Field(default=None, description="app_version字段")

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
class GetVersionInfoAPI(BaseModel):
    """get_version_info接口数据模型"""
    endpoint: str = "get_version_info"
    method: str = "POST"
    Req: type[BaseModel] = GetVersionInfoReq
    Res: type[BaseModel] = GetVersionInfoRes

# region api/
# endregion code

