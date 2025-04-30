# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/226659051e0
@llms.txt: https://napcat.apifox.cn/226659051e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:消息转发到私聊

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "forward_friend_single_msg"
__id__ = "226659051e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class ForwardFriendSingleMsgReq(BaseModel):
    """
    消息转发到私聊 请求体
    """

    user_id: int | str = Field(
        ..., description="目标用户 ID"
    )
    message_id: int | str = Field(
        ..., description="需要转发的消息 ID"
    )

# endregion req



# region res
class ForwardFriendSingleMsgRes(BaseModel):
    """
    消息转发到私聊 响应体
    """

    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ..., description="响应码"
    )
    data: None = Field(
        ..., description="响应数据"
    )
    message: str = Field(
        ..., description="响应信息"
    )
    wording: str = Field(
        ..., description="响应提示"
    )
    echo: str | None = Field(
        None, description="回声数据，如果请求时指定了 echo 字段，则响应时会带上"
    )

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
