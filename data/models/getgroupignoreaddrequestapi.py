# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659234e0
@llms.txt: https://napcat.apifox.cn/226659234e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:获取被过滤的加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_ignore_add_request"
__id__ = "226659234e0"
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
class GetGroupIgnoreAddRequestReq(BaseModel):
    """获取被过滤的加群请求"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupIgnoreAddRequestRes(BaseModel):
    """获取被过滤的加群请求"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

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
class GetGroupIgnoreAddRequestAPI(BaseModel):
    """get_group_ignore_add_request接口数据模型"""
    endpoint: str = "get_group_ignore_add_request"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupIgnoreAddRequestReq
    Res: type[BaseModel] = GetGroupIgnoreAddRequestRes

# region api/
# endregion code

