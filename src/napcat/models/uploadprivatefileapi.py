# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658883e0
@llms.txt: https://napcat.apifox.cn/226658883e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:上传私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "upload_private_file"
__id__ = "226658883e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class user_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

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
class UploadPrivateFileReq(BaseModel):
    """上传私聊文件"""
    user_id: user_id
    file: str
    name: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class UploadPrivateFileRes(BaseModel):
    """上传私聊文件"""
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
class UploadPrivateFileAPI(BaseModel):
    """upload_private_file接口数据模型"""
    endpoint: str = "upload_private_file"
    method: str = "POST"
    Req: type[BaseModel] = UploadPrivateFileReq
    Res: type[BaseModel] = UploadPrivateFileRes

# region api/
# endregion code

