# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659255e0
@llms.txt: https://napcat.apifox.cn/226659255e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:发送私聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "friend_poke"
__id__ = "226659255e0"
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
    name: str | None = Field(default=None, description="名称")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(default={}, description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class FriendPokeReq(BaseModel):
    """发送私聊戳一戳"""
    user_id: UserId = Field(description="用户ID")

    model_config = {
        "extra": "allow",
    }


# region req/


# region res
class FriendPokeRes(BaseModel):
    """发送私聊戳一戳"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class FriendPokeAPI(BaseModel):
    """friend_poke接口数据模型"""
    endpoint: str = Field(default="friend_poke", description="API endpoint")
    method: str = Field(default="POST", description="HTTP method")
    Req: type[BaseModel] = Field(default=FriendPokeReq, description="Request model")
    Res: type[BaseModel] = Field(default=FriendPokeRes, description="Response model")
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__), description="Logger instance")


# region api/
# region code/