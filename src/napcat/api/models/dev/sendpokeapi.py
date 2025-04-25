# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['账号相关']
@homepage: https://napcat.apifox.cn/250286923e0
@llms.txt: https://napcat.apifox.cn/250286923e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:发送戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_poke"
__id__ = "250286923e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Use Literal for const values

logger = logging.getLogger(__name__)

# region req
class SendPokeReq(BaseModel):
    """
    发送戳一戳请求模型
    """
    user_id: int | str = Field(..., description="要戳的用户的QQ号或Unionid，必填")
    group_id: int | str | None = Field(None, description="要戳的用户的群号，不填则为私聊戳")

# endregion req



# region res
class SendPokeRes(BaseModel):
    """
    发送戳一戳响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据") # Based on OpenAPI override to null
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo")

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
