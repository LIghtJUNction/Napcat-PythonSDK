# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['个人操作']
@homepage: https://napcat.apifox.cn/226657071e0
@llms.txt: https://napcat.apifox.cn/226657071e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:检查是否可以发送图片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "can_send_image"
__id__ = "226657071e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Literal is allowed for specific values

logger = logging.getLogger(__name__)

# region req
class CanSendImageReq(BaseModel):
    """
    检查是否可以发送图片 请求模型
    "
    # Request body is empty based on OpenAPI spec
    pass
# endregion req



# region res
class CanSendImageResData(BaseModel):
    """
    检查是否可以发送图片 响应数据模型
    "
    yes: bool = Field(..., description="是否可以发送图片")


class CanSendImageRes(BaseModel):
    """
    检查是否可以发送图片 响应模型
    "
    status: Literal["ok"] = Field(
        ..., description="响应状态", examples=["ok"]
    )
    retcode: int = Field(..., description="响应码")
    data: CanSendImageResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo")
# endregion res

# region api
class CanSendImageAPI(BaseModel):
    """can_send_image接口数据模型"""
    endpoint: str = "can_send_image"
    method: str = "POST"
    Req: type[BaseModel] = CanSendImageReq
    Res: type[BaseModel] = CanSendImageRes
# endregion api


# endregion code