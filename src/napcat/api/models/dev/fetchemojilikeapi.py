# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659219e0
@llms.txt: https://napcat.apifox.cn/226659219e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:获取贴表情详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "fetch_emoji_like"
__id__ = "226659219e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
class MessageId(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class FetchEmojiLikeReq(BaseModel):
    """获取贴表情详情"""
    message_id: MessageId = Field(description="消息ID")
    emojiId: str = Field(description="表情ID")
    emojiType: str = Field(description="表情类型")
    count: float | None = Field(20.0, description="数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class FetchEmojiLikeRes(BaseModel):
    """获取贴表情详情"""
    class EmojiLikesListItem(BaseModel):
        """表情点赞列表项"""
        tinyId: str = Field(description="用户ID")
        nickName: str = Field(description="用户昵称")
        headUrl: str = Field(description="用户头像URL")

        model_config = {
            "extra": "allow",
        }

    class Data(BaseModel):
        """响应数据类型"""
        result: float = Field(description="结果码")
        errMsg: str = Field(description="错误信息")
        emojiLikesList: list[FetchEmojiLikeRes.EmojiLikesListItem] = Field(description="表情点赞列表")
        cookie: str = Field(description="用于下一页请求的cookie")
        isLastPage: bool = Field(description="是否是最后一页")
        isFirstPage: bool = Field(description="是否是第一页")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(description="状态码")
    retcode: float = Field(description="返回码")
    data: Data = Field(description="响应数据")
    message: str = Field(description="消息")
    wording: str = Field(description="提示信息")
    echo: str | None = Field(description="回声字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class FetchEmojiLikeAPI(BaseModel):
    """fetch_emoji_like接口数据模型"""
    endpoint: str = "fetch_emoji_like"
    method: str = "POST"
    Req: type[BaseModel] = FetchEmojiLikeReq
    Res: type[BaseModel] = FetchEmojiLikeRes

# region api/
# endregion code
