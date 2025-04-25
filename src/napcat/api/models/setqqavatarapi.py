# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658980e0
@llms.txt: https://napcat.apifox.cn/226658980e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置头像

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_qq_avatar"
__id__ = "226658980e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetQqAvatarReq(BaseModel):
    """
    设置头像请求模型
    """
    file: str = Field(..., description="路径或链接")
# endregion req



# region res
class SetQqAvatarRes(BaseModel):
    """
    设置头像响应模型
    """
    status: Literal["ok"] = Field('ok', description="状态, 总是 ok")
    retcode: int = Field(..., description="状态码")
    data: None = Field(None, description="数据字段，总是 null")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误信息，更详细")
    echo: str | None = Field(None, description="回显，可能为 null")
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
