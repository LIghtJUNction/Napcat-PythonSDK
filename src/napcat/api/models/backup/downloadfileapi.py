# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658887e0
@llms.txt: https://napcat.apifox.cn/226658887e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:下载文件到缓存目录

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "download_file"
__id__ = "226658887e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class DownloadFileReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    base64: str | None = Field(None, description="和url二选一")
    url: str | None = Field(None, description="下载地址")
    thread_count: float = Field(..., description="下载线程数") # OpenAPI spec says number, which is float or int
    headers: str | list[str] = Field(..., description="请求头")
    name: str | None = Field(None, description="自定义文件名称")

# endregion req



# region res
class DownloadFileData(BaseModel):
    """嵌套的data字段"""
    file: str = Field(..., description="下载后的路径")


class DownloadFileRes(BaseModel):
    # 定义响应参数
    status: str = Field(..., description="状态，固定为 'ok'")
    retcode: float = Field(..., description="返回码") # OpenAPI spec says number
    data: DownloadFileData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文字描述")
    echo: str | None = Field(None, description="回显")

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