# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658980e0
@llms.txt: https://napcat.apifox.cn/226658980e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_qq_avatar"
__id__ = "226658980e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Required for Literal

logger = logging.getLogger(__name__)

# region req
class SetQqAvatarReq(BaseModel):
    """
    设置QQ头像请求模型
    """

    file: str = Field(..., description="头像文件路径、网络链接或Base64编码")

# endregion req



# region res
class SetQqAvatarRes(BaseModel):
    """
    设置QQ头像响应模型
    """

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="接口返回数据，此处为null") # OpenAPI spec shows data is null
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo回显") # Nullable

# endregion res

# region api
class SetQqAvatarAPI(BaseModel):
    """set_qq_avatar接口数据模型"""
    endpoint: str = "set_qq_avatar"
    method: str = "POST"
    Req: type[BaseModel] = SetQqAvatarReq
    Res: type[BaseModel] = SetQqAvatarRes
# endregion api




# endregion code