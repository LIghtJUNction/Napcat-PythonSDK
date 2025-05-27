# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659255e0
@llms.txt: https://napcat.apifox.cn/226659255e0.md
@last_update: 2025-05-28 01:34:10

@description:

summary:发送私聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "friend_poke"
__id__ = "226659255e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
class Result(BaseModel):
    """result字段"""
    status: Literal["ok"] = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, any] = Field(default_factory=dict, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# endregion component_models/

# region req
class FriendPokeReq(BaseModel):
    """发送私聊戳一戳"""
    user_id: int | str = Field(description="私聊对象") # OpenAPI specifies oneOf: [number, string]
    target_id: float | str | None = Field(default=None, description="戳一戳对象，可不填") # OpenAPI specifies anyOf: [number, string]

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class FriendPokeRes(BaseModel):
    """发送私聊戳一戳"""
    # Based on OpenAPI response schema for /friend_poke 200, which directly lists these fields.
    # The nested Data class from the original code has been removed as it does not align with the OpenAPI spec.
    status: Literal["ok"] = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class FriendPokeAPI(BaseModel):
    """friend_poke接口数据模型"""
    endpoint: str = "friend_poke"
    method: str = "POST"
    Req: type[BaseModel] = FriendPokeReq
    Res: type[BaseModel] = FriendPokeRes

# endregion api/
# endregion code
