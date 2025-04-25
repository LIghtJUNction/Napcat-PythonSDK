# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656979e0
@llms.txt: https://napcat.apifox.cn/226656979e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取群信息

summary:获取群信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_info"
__id__ = "226656979e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models

# region component_models/

# region req
class GetGroupInfoReq(BaseModel):
    """获取群信息"""
    group_id: str | int = Field(description="群组ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupInfoRes(BaseModel):
    """获取群信息"""
    class ResponseData(BaseModel):
        """响应数据类型"""

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: ResponseData(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
# region api/
# region code/