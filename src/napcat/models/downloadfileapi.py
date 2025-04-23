# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658887e0
@llms.txt: https://napcat.apifox.cn/226658887e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:下载文件到缓存目录

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "download_file"
__id__ = "226658887e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class DownloadFileReq(BaseModel):
    """
    请求参数
    """

    base64: str | None = Field(None, description="和url二选一")
    url: str | None = Field(None, description="下载地址")
    thread_count: float = Field(..., description="下载线程数")
    headers: str | list = Field(..., description="请求头")
    name: str | None = Field(None, description="自定义文件名称")
# region req/


# region res
class DownloadFileRes(BaseModel):
    """
    响应参数
    """

    file: str = Field(..., description="下载后的路径")
# region res/

# region api
class DownloadFileAPI(BaseModel):
    
    Request : type[DownloadFileReq] = DownloadFileReq
    Response  : type[DownloadFileRes] = DownloadFileRes


# region api/
# region code/

