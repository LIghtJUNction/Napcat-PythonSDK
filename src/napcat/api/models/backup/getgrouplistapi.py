# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656992e0
@llms.txt: https://napcat.apifox.cn/226656992e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_list"
__id__ = "226656992e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetGroupListReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    no_cache: bool = Field(
        default=False, description="不缓存"
    )
# endregion req



# region res
class GetGroupListRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """

    status: Literal['ok'] = Field(
        ..., description="状态，永远是 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: list[dict] = Field(
        ..., description="群列表数据，每个元素是一个群的信息"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="描述"
    )
    echo: str | None = Field(
        None, description="Echo" # Nullable field, None is a valid default/initial value
    )
# endregion res

# region api
class GetGroupListAPI(BaseModel):
    """get_group_list接口数据模型"""
    endpoint: str = "get_group_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupListReq
    Res: type[BaseModel] = GetGroupListRes
# endregion api




# endregion code