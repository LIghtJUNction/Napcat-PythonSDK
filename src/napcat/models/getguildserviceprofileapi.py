# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659317e0
@llms.txt: https://napcat.apifox.cn/226659317e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:get_guild_service_profile

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_guild_service_profile"
__id__ = "226659317e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region req
class GetGuildServiceProfileReq(BaseModel):
    """get_guild_service_profile"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGuildServiceProfileRes(BaseModel):
    """get_guild_service_profile"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="状态，如 'ok'")
    retcode: float = Field(default=0, description="返回码，0表示成功")
    data: Data = Field(default_factory=lambda: Data(), description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="文字描述")
    echo: str | None = Field(default=None, description="回显内容")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGuildServiceProfileAPI(BaseModel):
    """get_guild_service_profile接口数据模型"""
    endpoint: str = "get_guild_service_profile"
    method: str = "POST"
    Req: type[BaseModel] = GetGuildServiceProfileReq
    Res: type[BaseModel] = GetGuildServiceProfileRes

# region api/
# endregion code

