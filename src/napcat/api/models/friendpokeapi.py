# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['消息相关/发送私聊消息']
@homepage: https://napcat.apifox.cn/226659255e0
@llms.txt: https://napcat.apifox.cn/226659255e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:发送私聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "friend_poke"
__id__ = "226659255e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class FriendPokeReq(BaseModel):
    """
    发送私聊戳一戳请求模型
    """
    user_id: int | str = Field(..., description="要戳的QQ号")
# endregion req



# region res
class FriendPokeRes(BaseModel):
    """
    发送私聊戳一戳响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="用于識別本次操作的任意字符串, client在每次請求時填入相同的字符串, response會原樣返回")
# endregion res

# region api
class FriendPokeAPI(BaseModel):
    """friend_poke接口数据模型"""
    endpoint: str = "friend_poke"
    method: str = "POST"
    Req: type[BaseModel] = FriendPokeReq
    Res: type[BaseModel] = FriendPokeRes
# endregion api




# endregion code