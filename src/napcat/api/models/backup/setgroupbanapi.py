# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226656791e0
@llms.txt: https://napcat.apifox.cn/226656791e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:群禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_ban"
__id__ = "226656791e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class SetGroupBanReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="禁言用户QQ号")
    duration: float = Field(..., description="禁言时长，单位秒，0表示解除禁言")

# endregion req



# region res
class SetGroupBanRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """

    status: str = Field(..., description="响应状态", const="ok")
    retcode: float = Field(..., description="返回码")
    data: None = Field(None, description="响应数据，此接口无数据返回")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误描述")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class SetGroupBanAPI(BaseModel):
    """set_group_ban接口数据模型"""
    endpoint: str = "set_group_ban"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupBanReq
    Res: type[BaseModel] = SetGroupBanRes
# endregion api




# endregion code
