# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: [
    "密钥相关"
]
@homepage: https://napcat.apifox.cn/283136230e0
@llms.txt: https://napcat.apifox.cn/283136230e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取rkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_rkey"
__id__ = "283136230e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetRkeyReq(BaseModel):
    """
    请求: 获取rkey
    对应 endpoint: get_rkey
    "
    # 请求体为空，无需定义字段
    pass
# endregion req



# region res
class GetRkeyRes(BaseModel):
    """
    响应: 获取rkey
    对应 endpoint: get_rkey
    "

    class GetRkeyData(BaseModel):
        """
        响应数据项模型
        "
        type: str = Field(..., description="Type of the key")
        rkey: str = Field(..., description="The rkey value")
        created_at: int = Field(..., description="Timestamp of creation (seconds)")
        ttl: str = Field(..., description="Time to live")

    status: str = Field(..., description="Response status, 'ok' for success")
    retcode: int = Field(..., description="Response return code")
    data: list[GetRkeyData] = Field(..., description="List of rkey data objects")
    message: str = Field(..., description="Response message")
    wording: str = Field(..., description="Response wording")
    echo: str | None = Field(..., description="Echo value")

# endregion res

# region api
class GetRkeyAPI(BaseModel):
    """get_rkey接口数据模型"""
    endpoint: str = "get_rkey"
    method: str = "POST"
    Req: type[BaseModel] = GetRkeyReq
    Res: type[BaseModel] = GetRkeyRes
# endregion api




# endregion code
