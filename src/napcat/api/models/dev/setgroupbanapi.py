# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656791e0
@llms.txt: https://napcat.apifox.cn/226656791e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:群禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_ban"
__id__ = "226656791e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupBanReq(BaseModel):
    """
    请求模型
    """
    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="要禁言的 QQ 号")
    duration: int = Field(..., description="禁言时长，单位秒，0 表示解除禁言")

# endregion req



# region res
class SetGroupBanRes(BaseModel):
    """
    响应模型
    """
    status: Literal["ok"] = Field(..., description="状态码")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显") # Echo字段在openapi中为nullable，Field的default=None表示当字段缺失或为null时，该字段值为None

# endregion res

# region api
class SetGroupBanAPI(BaseModel):
    """set_group_ban接口数据模型"""
    endpoint: str = "set_group_ban"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupBanReq
    Res: type[BaseModel] = SetGroupBanRes
# endregion api




# endregion code
