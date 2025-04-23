# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226659104e0
@endpoint: set_msg_emoji_like
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659104e0
@llms.txt: https://napcat.apifox.cn/226659104e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:贴表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_msg_emoji_like"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class SetMsgEmojiLikeReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class SetMsgEmojiLikeRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetMsgEmojiLikeAPI(BaseModel):
    
    Request : type[SetMsgEmojiLikeReq] = SetMsgEmojiLikeReq
    Response  : type[SetMsgEmojiLikeRes] = SetMsgEmojiLikeRes


# region api/




# region code/

