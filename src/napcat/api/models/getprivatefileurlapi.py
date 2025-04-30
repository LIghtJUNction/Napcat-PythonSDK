# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/266151849e0
@llms.txt: https://napcat.apifox.cn/266151849e0.md
@last_update: 2025-04-27 00:53:41

@description: 获取私聊文件链接

summary:获取私聊文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_private_file_url"
__id__ = "266151849e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetPrivateFileUrlReq(BaseModel):
    """
    获取私聊文件链接请求模型
    """

    file_id: str = Field(..., description="文件的唯一标识符")

# endregion req



# region res
class GetPrivateFileUrlRes(BaseModel):
    """
    获取私聊文件链接响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="文字说明")
    echo: str | None = Field(None, description="echo")

    class Data(BaseModel):
        """
        响应数据模型
        """
        url: str = Field(..., description="私聊文件的下载链接")

    data: Data = Field(..., description="响应数据")

# endregion res

# region api
class GetPrivateFileUrlAPI(BaseModel):
    """get_private_file_url接口数据模型"""
    endpoint: str = "get_private_file_url"
    method: str = "POST"
    Req: type[BaseModel] = GetPrivateFileUrlReq
    Res: type[BaseModel] = GetPrivateFileUrlRes
# endregion api




# endregion code