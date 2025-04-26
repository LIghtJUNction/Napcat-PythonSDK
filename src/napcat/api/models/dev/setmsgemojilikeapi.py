# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659104e0
@llms.txt: https://napcat.apifox.cn/226659104e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:贴表情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_msg_emoji_like"
__id__ = "226659104e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal # Required for Literal type


# region req
class SetMsgEmojiLikeReq(BaseModel):
    """
    贴表情请求模型
    """

    message_id: int | str = Field(
        ..., description="消息ID，可以是整数或字符串"
    )
    emoji_id: int = Field(..., description="表情ID")
    set: bool = Field(..., description="true表示设置表情，false表示取消表情")

# endregion req



# region res
class SetMsgEmojiLikeRes(BaseModel):
    """
    贴表情响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """

        result: int = Field(..., description="结果代码")
        errMsg: str = Field(..., description="错误信息")

    status: Literal["ok"] = Field(..., description="响应状态，总是'ok'")
    retcode: int = Field(..., description="响应返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词语")
    echo: str | None = Field(None, description="请求中的echo数据，如果存在")

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
