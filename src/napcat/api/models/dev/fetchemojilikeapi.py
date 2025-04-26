# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['消息相关']
@homepage: https://napcat.apifox.cn/226659219e0
@llms.txt: https://napcat.apifox.cn/226659219e0.md
@last_update: 2025-04-27 00:53:40

@description: 获取贴表情详情

summary:获取贴表情详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "fetch_emoji_like"
__id__ = "226659219e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class FetchEmojiLikeReq(BaseModel):
    """
    获取贴表情详情请求模型
    """
    message_id: int | str = Field(..., description="消息ID")
    emojiId: str = Field(..., description="表情ID")
    emojiType: str = Field(..., description="表情类型")
    count: int = Field(20, description="数量")

# endregion req



# region res
class FetchEmojiLikeRes(BaseModel):
    """
    获取贴表情详情响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """

        class EmojiLikeItem(BaseModel):
            """
            表情点赞者信息
            """
            tinyId: str = Field(..., description="用户TinyID")
            nickName: str = Field(..., description="用户昵称")
            headUrl: str = Field(..., description="用户头像URL")

        result: int = Field(..., description="结果")
        errMsg: str = Field(..., description="错误信息")
        emojiLikesList: list[EmojiLikeItem] = Field(..., description="表情点赞列表")
        cookie: str = Field(..., description="Cookie")
        isLastPage: bool = Field(..., description="是否最后一页")
        isFirstPage: bool = Field(..., description="是否第一页")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="措辞")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class FetchEmojiLikeAPI(BaseModel):
    """fetch_emoji_like接口数据模型"""
    endpoint: str = "fetch_emoji_like"
    method: str = "POST"
    Req: type[BaseModel] = FetchEmojiLikeReq
    Res: type[BaseModel] = FetchEmojiLikeRes
# endregion api




# endregion code
