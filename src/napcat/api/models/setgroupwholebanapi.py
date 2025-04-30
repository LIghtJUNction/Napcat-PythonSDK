# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656802e0
@llms.txt: https://napcat.apifox.cn/226656802e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:全体禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_whole_ban"
__id__ = "226656802e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class SetGroupWholeBanReq(BaseModel):
    """
    全体禁言 请求数据模型
    """
    group_id: int | str = Field(..., description="群号")
    enable: bool = Field(..., description="是否禁言，当为 true 时 解除禁言，当为 false 时 全体禁言")

# endregion req



# region res
class SetGroupWholeBanRes(BaseModel):
    """
    全体禁言 响应数据模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(None, description="响应数据，固定为 null") # Explicitly null as per spec override
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class SetGroupWholeBanAPI(BaseModel):
    """set_group_whole_ban接口数据模型"""
    endpoint: str = "set_group_whole_ban"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupWholeBanReq
    Res: type[BaseModel] = SetGroupWholeBanRes
# endregion api




# endregion code