# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['文件相关']
@homepage: https://napcat.apifox.cn/266151849e0
@llms.txt: https://napcat.apifox.cn/266151849e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取私聊文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_private_file_url"
__id__ = "266151849e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetPrivateFileUrlReq(BaseModel):
    """
    获取私聊文件链接 请求参数
    """

    file_id: str = Field(..., description="文件ID")

# endregion req



# region res
class GetPrivateFileUrlRes(BaseModel):
    """
    获取私聊文件链接 响应参数
    """

    class Data(BaseModel):
        """
        响应数据
        """
        url: str = Field(..., description="文件链接")

    status: str = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="额外说明")
    echo: str | None = Field(None, description="发送时携带的 echo")

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
