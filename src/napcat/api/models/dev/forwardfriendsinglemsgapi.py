# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/226659051e0
@llms.txt: https://napcat.apifox.cn/226659051e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:消息转发到私聊

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "forward_friend_single_msg"
__id__ = "226659051e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class ForwardFriendSingleMsgReq(BaseModel):
    """
    Request model for forwarding message to a private chat.
    """
    user_id: int | str = Field(..., description="Target user ID")
    message_id: int | str = Field(..., description="Message ID to forward")
# endregion req



# region res
class ForwardFriendSingleMsgRes(BaseModel):
    """
    Response model for forwarding message to a private chat.
    """
    status: str = Field("ok", description="Response status, 'ok' for success")
    retcode: int = Field(..., description="Response return code")
    data: None = Field(None, description="Data field (expected to be null)") # Based on OpenAPI override
    message: str = Field(..., description="Response message")
    wording: str = Field(..., description="Response wording")
    echo: str | None = Field(None, description="Echo field from request")
# endregion res

# region api
class ForwardFriendSingleMsgAPI(BaseModel):
    """forward_friend_single_msg接口数据模型"""
    endpoint: str = "forward_friend_single_msg"
    method: str = "POST"
    Req: type[BaseModel] = ForwardFriendSingleMsgReq
    Res: type[BaseModel] = ForwardFriendSingleMsgRes
# endregion api




# endregion code
