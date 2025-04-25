# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659219e0
@llms.txt: https://napcat.apifox.cn/226659219e0.md
@last_update: 2025-04-25 23:00:50

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
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class UserId(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


class GroupId(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


class MessageId(BaseModel):
    id: str | int = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, Any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

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
    group_id: GroupId | None = Field(None, description="群组ID")
    user_id: UserId | None = Field(None, description="用户ID")
    count: float | None = Field(None, description="数量")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class FetchEmojiLikeRes(BaseModel):
    """获取贴表情详情"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        result: float | None = Field(default=None, description="result字段")
        errMsg: str | None = Field(default=None, description="errMsg字段")
        emojiLikesList: list["FetchEmojiLikeRes.EmojiLikesListItem"] | None = Field(default=None, description="emojiLikesList字段")
        cookie: str | None = Field(default=None, description="cookie字段")
        isLastPage: bool | None = Field(default=None, description="isLastPage字段")
        isFirstPage: bool | None = Field(default=None, description="isFirstPage字段")

        model_config = {
            "extra": "allow",
        }

    class EmojiLikesListItem(BaseModel):
        """emojiLikesList Item"""
        tinyId: str = Field(description="tinyId")
        nickName: str = Field(description="nickName")
        headUrl: str = Field(description="headUrl")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class FetchEmojiLikeAPI(BaseModel):
    """fetch_emoji_like接口数据模型"""
    endpoint: str = Field(default="fetch_emoji_like", description="endpoint")
    method: str = Field(default="POST", description="method")
    Req: type[BaseModel] = Field(default=FetchEmojiLikeReq, description="请求模型")
    Res: type[BaseModel] = Field(default=FetchEmojiLikeRes, description="响应模型")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="logger")

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 FetchEmojiLikeAPI")

    def __call__(self, req: FetchEmojiLikeReq) -> FetchEmojiLikeRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 FetchEmojiLikeAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/