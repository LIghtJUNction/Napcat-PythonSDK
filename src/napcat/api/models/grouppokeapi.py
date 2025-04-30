# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: [
    "消息相关/发送群聊消息"
]
@homepage: https://napcat.apifox.cn/226659265e0
@llms.txt: https://napcat.apifox.cn/226659265e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:发送群聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "group_poke"
__id__ = "226659265e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GroupPokeReq(BaseModel):
    """
    发送群聊戳一戳请求参数
    """

    group_id: int | str = Field(
        ..., description="群号",
        examples=[123456789]
    )
    user_id: int | str = Field(
        ..., description="要戳的 QQ 号",
        examples=[123456789]
    )
# endregion req



# region res
class GroupPokeRes(BaseModel):
    """
    发送群聊戳一戳响应参数
    """

    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    message: str = Field(
        ..., description="错误信息"
    )
    wording: str = Field(
        ..., description="错误信息描述"
    )
    echo: str | None = Field(
        None, description="echo回传"
    )
# endregion res

# region api
class GroupPokeAPI(BaseModel):
    """group_poke接口数据模型"""
    endpoint: str = "group_poke"
    method: str = "POST"
    Req: type[BaseModel] = GroupPokeReq
    Res: type[BaseModel] = GroupPokeRes
# endregion api




# endregion code
