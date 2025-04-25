# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
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
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class FriendPokeReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class FriendPokeRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
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

