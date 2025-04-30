# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656913e0
@llms.txt: https://napcat.apifox.cn/226656913e0.md
@last_update: 2025-04-27 00:53:40

@description: 设置指定群的群成员名片。

summary:设置群成员名片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_card"
__id__ = "226656913e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field


# region req
class SetGroupCardReq(BaseModel):
    """
    设置群成员名片 请求模型
    """

    group_id: int | str = Field(
        ...,
        description="群号"
    )
    user_id: int | str = Field(
        ...,
        description="要设置的 QQ 号"
    )
    card: str | None = Field(
        None,
        description="群名片, 为空则为取消群名片"
    )

# endregion req



# region res
class SetGroupCardRes(BaseModel):
    """
    设置群成员名片 响应模型
    """

    status: Literal["ok"] = Field(
        "ok",
        description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ...,
        description="响应码"
    )
    data: None = Field(
        None,
        description="响应数据，固定为 null"
    )
    message: str = Field(
        ...,
        description="响应消息"
    )
    wording: str = Field(
        ...,
        description="详细响应描述"
    )
    echo: str | None = Field(
        None,
        description="用于标识客户端请求，可选"
    )

# endregion res

# region api
class SetGroupCardAPI(BaseModel):
    """set_group_card接口数据模型"""
    endpoint: Literal["set_group_card"] = "set_group_card"
    method: Literal["POST"] = "POST"
    Req: type[SetGroupCardReq] = SetGroupCardReq
    Res: type[SetGroupCardRes] = SetGroupCardRes
# endregion api




# endregion code