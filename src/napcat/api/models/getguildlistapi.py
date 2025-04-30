# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/226659311e0
@llms.txt: https://napcat.apifox.cn/226659311e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:get_guild_list

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_guild_list"
__id__ = "226659311e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Any, Literal

logger = logging.getLogger(__name__)

# region req
class GetGuildListReq(BaseModel):
    """
    get_guild_list请求模型
    """

    pass
# endregion req



# region res
class GetGuildListRes(BaseModel):
    """
    get_guild_list响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: dict[Any,Any] = Field(default_factory=dict, description="响应数据")
    msg: str = Field(..., description="错误信息")
    wording: str = Field(..., description="友好提示")
# endregion res

# region api
class GetGuildListAPI(BaseModel):
    """get_guild_list接口数据模型"""
    endpoint: str = "get_guild_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGuildListReq
    Res: type[BaseModel] = GetGuildListRes
# endregion api




# endregion code
