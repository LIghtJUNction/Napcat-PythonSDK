# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659265e0
@llms.txt: https://napcat.apifox.cn/226659265e0.md
@last_update: 2025-04-25 23:00:50

@description: 

summary:发送群聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "group_poke"
__id__ = "226659265e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)


# region component_models
class GroupPokeReq(BaseModel):
    """发送群聊戳一戳"""
    group_id: str | int = Field(description="群ID, 可以是字符串或者数字")
    user_id: str | int = Field(description="用户ID, 可以是字符串或者数字")

    model_config = {
        "extra": "allow",
    }


class GroupPokeRes(BaseModel):
    """发送群聊戳一戳"""
    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0.0, description="retcode字段")
    data: dict[str, Any] = Field(default={}, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req

# region req/


# region res
# region res/

# region api
class GroupPokeAPI(BaseModel):
    """group_poke接口数据模型"""
    endpoint: str = "group_poke"
    method: str = "POST"
    Req: type[BaseModel] = GroupPokeReq
    Res: type[BaseModel] = GroupPokeRes
    logger: logging.Logger = Field(default_factory=lambda: logging.getLogger(__name__))

    model_config = {
        "arbitrary_types_allowed": True
    }


# region api/
# region code/