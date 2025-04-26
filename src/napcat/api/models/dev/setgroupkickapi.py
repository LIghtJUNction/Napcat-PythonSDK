# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656748e0
@llms.txt: https://napcat.apifox.cn/226656748e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:群踢人

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_kick"
__id__ = "226656748e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class SetGroupKickReq(BaseModel):
    """
    群踢人接口请求参数
    """

    group_id: int | str = Field(
        ...,
        description="群号"
    )
    user_id: int | str = Field(
        ...,
        description="要踢的 QQ 号"
    )
    reject_add_request: bool = Field(
        ...,
        description="是否群拉黑"
    )
# endregion req



# region res
class SetGroupKickRes(BaseModel):
    """
    群踢人接口响应参数
    """

    status: Literal["ok"] = Field(
        ...,
        description="状态"
    )
    retcode: int = Field(
        ...,
        description="返回码"
    )
    data: None = Field(
        ...,
        description="数据"
    ) # OpenAPI spec indicates null
    message: str = Field(
        ...,
        description="消息"
    )
    wording: str = Field(
        ...,
        description="提示"
    )
    echo: str | None = Field(
        ...,
        description="Echo"
    )
# endregion res

# region api
class SetGroupKickAPI(BaseModel):
    """set_group_kick接口数据模型"""
    endpoint: str = "set_group_kick"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupKickReq
    Res: type[BaseModel] = SetGroupKickRes
# endregion api




# endregion code
