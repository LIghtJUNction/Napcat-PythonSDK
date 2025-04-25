# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658883e0
@llms.txt: https://napcat.apifox.cn/226658883e0.md
@last_update: 2025-04-26 01:17:44

@description: 上传私聊文件

summary:上传私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
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
    上传私聊文件的请求模型
    """

    user_id: int | str = Field(..., description="用户ID")
    file: str = Field(..., description="文件内容（可能是文件路径或base64编码）")
    name: str = Field(..., description="文件名")

# endregion req



# region res
class UploadPrivateFileRes(BaseModel):
    """
    上传私聊文件的响应模型
    """
    status: Literal['ok'] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据体 (为null)")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应文案")
    echo: str | None = Field(..., description="echo回显字段")

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
