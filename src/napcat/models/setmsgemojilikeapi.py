# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659104e0
@llms.txt: https://napcat.apifox.cn/226659104e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:贴表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_msg_emoji_like"
__id__ = "226659104e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetMsgEmojiLikeReq(BaseModel):
    """
    请求参数
    """

    message_id: float | str = Field(..., description="")
    emoji_id: float = Field(..., description="")
    set: bool = Field(..., description="")
# region req/


# region res
class SetMsgEmojiLikeRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class SetMsgEmojiLikeAPI(BaseModel):
    
    Request : type[SetMsgEmojiLikeReq] = SetMsgEmojiLikeReq
    Response  : type[SetMsgEmojiLikeRes] = SetMsgEmojiLikeRes


# region api/
# region code/

