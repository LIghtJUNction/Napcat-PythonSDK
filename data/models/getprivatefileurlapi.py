# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151849e0
@llms.txt: https://napcat.apifox.cn/266151849e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:获取私聊文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_private_file_url"
__id__ = "266151849e0"
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
class GetPrivateFileUrlReq(BaseModel):
    """获取私聊文件链接"""
    file_id: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetPrivateFileUrlRes(BaseModel):
    """获取私聊文件链接"""
    class Data(BaseModel):
        """响应数据类型"""
        url: str = Field(default=None, description="url字段")

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
class GetPrivateFileUrlAPI(BaseModel):
    """get_private_file_url接口数据模型"""
    endpoint: str = "get_private_file_url"
    method: str = "POST"
    Req: type[BaseModel] = GetPrivateFileUrlReq
    Res: type[BaseModel] = GetPrivateFileUrlRes

# region api/
# endregion code

