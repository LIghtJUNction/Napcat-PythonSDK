# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
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
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class UploadPrivateFileReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    user_id: int | str = Field(..., description="私聊对象 QQ 号")
    file: str = Field(..., description="文件路径或 URL")
    name: str = Field(..., description="文件名")
# endregion req



# region res
class UploadPrivateFileRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据 (此处为 null)") # Data is null as per OpenAPI spec override
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="额外信息")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class UploadPrivateFileAPI(BaseModel):
    """upload_private_file接口数据模型"""
    endpoint: str = "upload_private_file"
    method: str = "POST"
    Req: type[BaseModel] = UploadPrivateFileReq
    Res: type[BaseModel] = UploadPrivateFileRes
# endregion api




# endregion code
