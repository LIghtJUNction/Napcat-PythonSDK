# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657083e0
@llms.txt: https://napcat.apifox.cn/226657083e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_status"
__id__ = "226657083e0"
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
class GetStatusReq(BaseModel):
    """获取状态"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetStatusRes(BaseModel):
    """获取状态"""
    class Data(BaseModel):
        """响应数据类型"""
        online: bool = Field(default=None, description="online字段")
        good: bool = Field(default=None, description="good字段")
        stat: dict[str, Any] = Field(default=None, description="stat字段")

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
class GetStatusAPI(BaseModel):
    """get_status接口数据模型"""
    endpoint: str = "get_status"
    method: str = "POST"
    Req: type[BaseModel] = GetStatusReq
    Res: type[BaseModel] = GetStatusRes

# region api/
# endregion code

