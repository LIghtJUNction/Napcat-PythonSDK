# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['账号相关']
@homepage: https://napcat.apifox.cn/266151905e0
@llms.txt: https://napcat.apifox.cn/266151905e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:设置自定义在线状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_diy_online_status"
__id__ = "266151905e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetDiyOnlineStatusReq(BaseModel):
    """
    设置自定义在线状态请求模型
    """

    face_id: str | int | float = Field(
        ..., description="表情ID, 可以是字符串或数字"
    )
    face_type: str | int | float | None = Field(
        default=None, description="表情类型, 可以是字符串或数字, 可选"
    )
    wording: str | None = Field(default=None, description="描述文本, 可选")

# endregion req



# region res
class SetDiyOnlineStatusRes(BaseModel):
    """
    设置自定义在线状态响应模型
    """

    status: Literal["ok"] = Field(
        ..., description="API状态, 固定为 'ok'"
    )
    retcode: int = Field(..., description="返回码")
    data: str = Field(
        ..., description="响应数据, 字符串类型"
    )
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(default=None, description="Echo数据, 可为null")

# endregion res

# region api
class SetDiyOnlineStatusAPI(BaseModel):
    """set_diy_online_status接口数据模型"""
    endpoint: str = "set_diy_online_status"
    method: str = "POST"
    Req: type[BaseModel] = SetDiyOnlineStatusReq
    Res: type[BaseModel] = SetDiyOnlineStatusRes
# endregion api




# endregion code
