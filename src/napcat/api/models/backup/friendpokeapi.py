# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/226659255e0
@llms.txt: https://napcat.apifox.cn/226659255e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:发送私聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "friend_poke"
__id__ = "226659255e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class FriendPokeReq(BaseModel):
    """
    发送私聊戳一戳 请求参数
    """

    user_id: int | str = Field(..., description="要戳的机器人好友QQ号")
# endregion req



# region res
class FriendPokeRes(BaseModel):
    """
    发送私聊戳一戳 响应参数
    """
    status: Literal['ok'] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="详细信息")
    echo: str | None = Field(None, description="Echo")
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
