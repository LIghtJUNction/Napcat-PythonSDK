# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/250286923e0
@llms.txt: https://napcat.apifox.cn/250286923e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:发送戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_poke"
__id__ = "250286923e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Literal is standard library, not deprecated typing

logger = logging.getLogger(__name__)

# region req
class SendPokeReq(BaseModel):
    """
    发送戳一戳请求模型
    """

    user_id: int | str = Field(
        ...,
        description="要戳的用户ID，必填"
    )
    group_id: int | str | None = Field(
        default=None,
        description="群组ID，不填则为私聊戳"
    )
# endregion req



# region res
class SendPokeRes(BaseModel):
    """
    发送戳一戳响应模型
    """
    status: Literal["ok"] = Field(
        ...,
        description="响应状态"
    )
    retcode: int = Field(
        ...,
        description="响应码"
    )
    data: None = Field(
        ...,
        description="数据字段，此处为null"
    )
    message: str = Field(
        ...,
        description="错误消息"
    )
    wording: str = Field(
        ...,
        description="详细错误描述"
    )
    echo: str | None = Field(
        default=None,
        description="可能包含请求的echo信息"
    )
# endregion res

# region api
class SendPokeAPI(BaseModel):
    """send_poke接口数据模型"""
    endpoint: str = "send_poke"
    method: str = "POST"
    Req: type[BaseModel] = SendPokeReq
    Res: type[BaseModel] = SendPokeRes
# endregion api




# endregion code