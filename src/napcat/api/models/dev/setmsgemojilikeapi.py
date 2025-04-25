# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659104e0
@llms.txt: https://napcat.apifox.cn/226659104e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:贴表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_msg_emoji_like"
__id__ = "226659104e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class SetMsgEmojiLikeReq(BaseModel):
    """
    Request model for setting message emoji likes.
    """

    message_id: int | str = Field(
        ..., description="消息 ID"
    )  # message_id could be number or string based on schema
    emoji_id: int = Field(..., description="表情 ID")
    set: bool = Field(..., description="设置状态 (true: 添加, false: 移除)")

# endregion req



# region res
class SetMsgEmojiLikeRes(BaseModel):
    """
    Response model for setting message emoji likes.
    """

    class Data(BaseModel):
        """
        Data payload for the response.
        """
        result: int = Field(..., description="操作结果 (例如 0 成功)") # Assuming result is an integer based on ref_0 type number
        errMsg: str = Field(..., description="错误消息，如果操作失败")

    status: Literal["ok"] = Field(
        ..., description="API 调用状态"
    )
    retcode: int = Field(..., description="API 返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="API 消息")
    wording: str = Field(..., description="API 提示")
    echo: str | None = Field(None, description="Echo 数据")


# endregion res

# region api
class SetMsgEmojiLikeAPI(BaseModel):
    """set_msg_emoji_like接口数据模型"""
    endpoint: str = "set_msg_emoji_like"
    method: str = "POST"
    Req: type[BaseModel] = SetMsgEmojiLikeReq
    Res: type[BaseModel] = SetMsgEmojiLikeRes
# endregion api




# endregion code
