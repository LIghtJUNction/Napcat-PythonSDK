# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226657058e0
@llms.txt: https://napcat.apifox.cn/226657058e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取语音消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_record"
__id__ = "226657058e0"
__method__ = "POST"

# endregion METADATA


# region code
from enum import Enum
from pydantic import BaseModel, Field
from typing import Literal # Use Literal for const constraints

# region req
class OutFormatEnum(str, Enum):
    """语音消息输出格式"""
    MP3 = "mp3"
    AMR = "amr"
    WMA = "wma"
    M4A = "m4a"
    SPX = "spx"
    OGG = "ogg"
    WAV = "wav"
    FLAC = "flac"


class GetRecordReq(BaseModel):
    """
    请求获取语音消息详情
    """

    file: str = Field(..., description="语音文件名")
    out_format: OutFormatEnum = Field(..., description="需要转换到的语音格式")

# endregion req

# region res
class GetRecordRes(BaseModel):
    """
    响应获取语音消息详情
    """

    class GetRecordResData(BaseModel):
        """响应数据详情"""

        file: str = Field(..., description="本地路径")
        url: str = Field(..., description="网络路径")
        file_size: str = Field(..., description="文件大小")
        file_name: str = Field(..., description="文件名")
        base64: str = Field(..., description="base64编码后的文件内容")

    status: Literal['ok'] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: GetRecordResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class GetRecordAPI(BaseModel):
    """get_record接口数据模型"""

    endpoint: str = "get_record"
    method: str = "POST"
    Req: type[BaseModel] = GetRecordReq
    Res: type[BaseModel] = GetRecordRes

# endregion api

# endregion code
