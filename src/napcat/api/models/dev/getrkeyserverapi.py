# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['密钥相关']
@homepage: https://napcat.apifox.cn/283136236e0
@llms.txt: https://napcat.apifox.cn/283136236e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取rkey服务

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_rkey_server"
__id__ = "283136236e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetRkeyServerReq(BaseModel):
    """
    请求模型
    """

    pass
# endregion req



# region res
class GetRkeyServerRes(BaseModel):
    """
    响应模型
    """

    class Data(BaseModel):
        """
        响应数据
        """
        private_rkey: str = Field(..., description="Private Rkey")
        group_rkey: str = Field(..., description="Group Rkey")
        expired_time: int = Field(..., description="Expiration time (timestamp)") # Assuming integer timestamp based on 'number' type
        name: str = Field(..., description="Server Name")

    status: Literal["ok"] = Field(..., description="API status, must be ok")
    retcode: int = Field(..., description="Return code")
    data: Data = Field(..., description="Response data payload")
    message: str = Field(..., description="Message")
    wording: str = Field(..., description="Wording")
    echo: str | None = Field(None, description="Echo string")

# endregion res

# region api
class GetRkeyServerAPI(BaseModel):
    """get_rkey_server接口数据模型"""
    endpoint: str = "get_rkey_server"
    method: str = "POST"
    Req: type[BaseModel] = GetRkeyServerReq
    Res: type[BaseModel] = GetRkeyServerRes
# endregion api




# endregion code
