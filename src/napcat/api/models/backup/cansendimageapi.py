# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226657071e0
@llms.txt: https://napcat.apifox.cn/226657071e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:检查是否可以发送图片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "can_send_image"
__id__ = "226657071e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class CanSendImageReq(BaseModel):
    """
    请求模型
    """
    # Request body is empty according to the OpenAPI spec
    pass
# endregion req



# region res
class CanSendImageRes(BaseModel):
    """
    响应模型
    """
    class Data(BaseModel):
        """
        响应数据
        """
        yes: bool = Field(..., description="是否可以发送图片")

    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应描述")
    echo: str | None = Field(None, description="Echo回显")

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
