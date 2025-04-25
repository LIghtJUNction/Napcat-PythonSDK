# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/250286915e0
@llms.txt: https://napcat.apifox.cn/250286915e0.md
@last_update: 2025-04-26 01:17:45

@description:

summary:获取clientkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_clientkey"
__id__ = "250286915e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetClientkeyReq(BaseModel):
    """
    获取clientkey的请求模型
    """
    # No fields required in the request body according to the spec.
    pass
# endregion req



# region res
class GetClientkeyRes(BaseModel):
    """
    获取clientkey的响应模型
    """

    class Data(BaseModel):
        """
        响应数据模型
        """
        clientkey: str = Field(..., description="Client key")

    status: Literal["ok"] = Field(..., description="Status of the operation")
    retcode: int = Field(..., description="Return code")
    data: Data = Field(..., description="Response data")
    message: str = Field(..., description="Message")
    wording: str = Field(..., description="Wording")
    echo: str | None = Field(..., description="Echo string")
# endregion res

# region api
class GetClientkeyAPI(BaseModel):
    """get_clientkey接口数据模型"""
    endpoint: str = "get_clientkey"
    method: str = "POST"
    Req: type[BaseModel] = GetClientkeyReq
    Res: type[BaseModel] = GetClientkeyRes
# endregion api




# endregion code
