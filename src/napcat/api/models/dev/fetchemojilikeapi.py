# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659219e0
@llms.txt: https://napcat.apifox.cn/226659219e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取贴表情详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_emoji_like"
__id__ = "226659219e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class FetchEmojiLikeReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    message_id: int | str = Field(..., description="消息ID")
    emojiId: str = Field(..., description="表情ID")
    emojiType: str = Field(..., description="表情类型")
    group_id: int | str | None = Field(default=None, description="群组ID (可选)")
    user_id: int | str | None = Field(default=None, description="用户ID (可选)")
    count: int | None = Field(default=None, description="数量 (可选)")
# endregion req



# region res

class EmojiLikeItem(BaseModel):
    """表情点赞详情项"""

    tinyId: str = Field(..., description="用户tinyId")
    nickName: str = Field(..., description="用户昵称")
    headUrl: str = Field(..., description="用户头像URL")


class FetchEmojiLikeData(BaseModel):
    """fetch_emoji_like接口响应数据"""

    result: int = Field(..., description="结果码")
    errMsg: str = Field(..., description="错误消息")
    emojiLikesList: list[EmojiLikeItem] = Field(..., description="表情点赞列表")
    cookie: str = Field(..., description="cookie")
    isLastPage: bool = Field(..., description="是否最后一页")
    isFirstPage: bool = Field(..., description="是否第一页")


class FetchEmojiLikeRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """

    status: Literal['ok'] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: FetchEmojiLikeData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(default=None, description="echo")


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