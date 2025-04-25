# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226657066e0
@llms.txt: https://napcat.apifox.cn/226657066e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取图片消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_image"
__id__ = "226657066e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetImageReq(BaseModel):
    """
    获取图片消息详情请求模型
    """
    file_id: str = Field(..., description="图片消息的file_id")

# endregion req



# region res
class GetImageResData(BaseModel):
    """
    获取图片消息详情响应数据模型
    """
    file: str = Field(..., description="本地路径")
    url: str = Field(..., description="网络路径")
    file_size: str = Field(..., description="文件大小")
    file_name: str = Field(..., description="文件名")
    base64: str = Field(..., description="图片Base64编码")


class GetImageRes(BaseModel):
    """
    获取图片消息详情响应模型
    """
    status: str = Field("ok", description="Status of the response", const=True)
    retcode: int = Field(..., description="Return code")
    data: GetImageResData = Field(..., description="Image data details")
    message: str = Field(..., description="Response message")
    wording: str = Field(..., description="Response wording")
    echo: str | None = Field(None, description="Echo string, can be null")

# endregion res

# region api
class GetImageAPI(BaseModel):
    """get_image接口数据模型"""
    endpoint: str = "get_image"
    method: str = "POST"
    Req: type[BaseModel] = GetImageReq
    Res: type[BaseModel] = GetImageRes
# endregion api




# endregion code
