# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226657058e0
@llms.txt: https://napcat.apifox.cn/226657058e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取语音消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_record"
__id__ = "226657058e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetRecordReq(BaseModel):
    """
    获取语音消息详情请求模型
    """
    file: str | None = Field(None, description="文件路径")
    file_id: str | None = Field(None, description="文件 ID")
    out_format: Literal["mp3", "amr", "wma", "m4a", "spx", "ogg", "wav", "flac"] = Field(..., description="转换的目标格式")

# endregion req



# region res
class GetRecordRes(BaseModel):
    """
    获取语音消息详情响应模型
    """

    class Data(BaseModel):
        """
        响应数据
        """
        file: str = Field(..., description="本地路径")
        url: str = Field(..., description="网络路径")
        file_size: str = Field(..., description="文件大小")
        file_name: str = Field(..., description="文件名")
        base64: str = Field(..., description="base64")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="echo")

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
