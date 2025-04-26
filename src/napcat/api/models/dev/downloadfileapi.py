# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658887e0
@llms.txt: https://napcat.apifox.cn/226658887e0.md
@last_update: 2025-04-27 00:53:40

@description: 下载文件到缓存目录

summary:下载文件到缓存目录

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "download_file"
__id__ = "226658887e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

logger = logging.getLogger(__name__)

# region req
class DownloadFileReq(BaseModel):
    """
    下载文件到缓存目录请求体
    """

    url: str | None = Field(default=None, description="下载地址")
    base64: str | None = Field(default=None, description="和url二选一")
    name: str | None = Field(default=None, description="自定义文件名称")
    headers: str | list[str] | None = Field(default=None, description="请求头")
    
    model_config = ConfigDict(extra='allow') # Allow extra fields if the spec is incomplete

# endregion req



# region res
class DownloadFileRes(BaseModel):
    """
    下载文件到缓存目录响应体
    """
    class Data(BaseModel):
        """
        响应数据
        """
        file: str = Field(..., description="下载后的路径")
        
        model_config = ConfigDict(extra='allow') # Allow extra fields if the spec is incomplete

    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="词语") # Assuming this is a string based on spec
    echo: str | None = Field(default=None, description="echo")

    model_config = ConfigDict(extra='allow') # Allow extra fields based on base result schema


# endregion res

# region api
class DownloadFileAPI(BaseModel):
    """download_file接口数据模型"""
    endpoint: str = "download_file"
    method: str = "POST"
    Req: type[BaseModel] = DownloadFileReq
    Res: type[BaseModel] = DownloadFileRes
# endregion api




# endregion code
