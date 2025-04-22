# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659255e0
@endpoint: friend_poke
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/226659255e0
@llms.txt: https://napcat.apifox.cn/226659255e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:49

@description: friend_poke API
@usage: 使用 `client.friend_poke()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "friend_poke"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class FriendPokeReq(BaseHttpRequest):
    """
    friend_poke 请求参数
    """

    pass
# region req/

# region data
class FriendPokeData(BaseModel):
    """
    friend_poke 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class FriendPokeRes(BaseHttpResponse[FriendPokeData]):
    """
    friend_poke 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class FriendPokeAPI(BaseHttpAPI[FriendPokeReq, FriendPokeRes]):
    """
    发送私聊戳一戳
    """
    api: str = "/friend_poke"
    method: Literal["POST", "GET"] = "POST"

    Request = FriendPokeReq
    Response = FriendPokeRes

    request: FriendPokeReq
    response: FriendPokeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(FriendPokeAPI)

# region code/

