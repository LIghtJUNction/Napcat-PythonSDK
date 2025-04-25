# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656913e0
@llms.txt: https://napcat.apifox.cn/226656913e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置群成员名片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_card"
__id__ = "226656913e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class SetGroupCardReq(BaseModel):
    """
    设置群成员名片 - 请求参数
    """

    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="成员QQ")
    card: str = Field(..., description="群名片，为空则为取消群名片")

# endregion req



# region res
class SetGroupCardRes(BaseModel):
    """
    设置群成员名片 - 响应参数
    """

    status: Literal['ok'] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据") # According to schema, data is null
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="进一步解释")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class SetGroupCardAPI(BaseModel):
    """set_group_card接口数据模型"""
    endpoint: str = "set_group_card"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupCardReq
    Res: type[BaseModel] = SetGroupCardRes
# endregion api




# endregion code
