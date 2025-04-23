# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659219e0
@llms.txt: https://napcat.apifox.cn/226659219e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取贴表情详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_emoji_like"
__id__ = "226659219e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class FetchEmojiLikeReq(BaseModel):
    """
    请求参数
    """

    message_id: float | str = Field(..., description="")
    emojiId: str = Field(..., description="表情ID")
    emojiType: str = Field(..., description="表情类型")
    group_id: float | str | None = Field(None, description="")
    user_id: float | str | None = Field(None, description="")
    count: float | None = Field(None, description="")
# region req/


# region res
class FetchEmojiLikeRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
    emojiLikesList: list[dict] = Field(..., description="")
    cookie: str = Field(..., description="")
    isLastPage: bool = Field(..., description="")
    isFirstPage: bool = Field(..., description="")
# region res/

# region api
class FetchEmojiLikeAPI(BaseModel):
    
    Request : type[FetchEmojiLikeReq] = FetchEmojiLikeReq
    Response  : type[FetchEmojiLikeRes] = FetchEmojiLikeRes


# region api/
# region code/

