# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658971e0
@llms.txt: https://napcat.apifox.cn/226658971e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取推荐群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "ArkShareGroup"
__id__ = "226658971e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class ArksharegroupReq(BaseModel):
    """
    获取推荐群聊卡片 - 请求模型
    """

    group_id: str = Field(
        ..., description="群聊ID"
    )
# endregion req



# region res
class ArksharegroupRes(BaseModel):
    """
    获取推荐群聊卡片 - 响应模型
    """

    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: str = Field(
        ..., description="卡片json"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="文案"
    )
    echo: str | None = Field(
        default=None, description="Echo字段"
    )
# endregion res

# region api
class ArksharegroupAPI(BaseModel):
    """ArkShareGroup接口数据模型"""
    endpoint: str = "ArkShareGroup"
    method: str = "POST"
    Req: type[BaseModel] = ArksharegroupReq
    Res: type[BaseModel] = ArksharegroupRes
# endregion api




# endregion code