# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658887e0
@llms.txt: https://napcat.apifox.cn/226658887e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:下载文件到缓存目录

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "download_file"
__id__ = "226658887e0"
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
class DownloadFileReq(BaseModel):
    """下载文件到缓存目录"""
    url: str | None = Field(None, description="下载地址")
    base64: str | None = Field(None, description="和url二选一")
    name: str | None = Field(None, description="自定义文件名称")
    headers: str | list[str] | None = Field(None, description="请求头")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class DownloadFileRes(BaseModel):
    """下载文件到缓存目录"""
    class Data(BaseModel):
        """响应数据类型"""
        file: str = Field(default=None, description="下载后的路径")

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
class DownloadFileAPI(BaseModel):
    """download_file接口数据模型"""
    endpoint: str = "download_file"
    method: str = "POST"
    Req: type[BaseModel] = DownloadFileReq
    Res: type[BaseModel] = DownloadFileRes

# region api/
# endregion code

