# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/226659280e0
@llms.txt: https://napcat.apifox.cn/226659280e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取packet状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_packet_status"
__id__ = "226659280e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class NcGetPacketStatusReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    # No fields required based on OpenAPI spec
    pass
# endregion req



# region res
class NcGetPacketStatusRes(BaseModel):
    """
    获取packet状态的响应模型
    """

    status: str = Field(..., description="响应状态，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据，此处为 null")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词")
    echo: str | None = Field(None, description="Echo 字段，客户端发送的字段，可能为 null")
# endregion res

# region api
class NcGetPacketStatusAPI(BaseModel):
    """nc_get_packet_status接口数据模型"""
    endpoint: str = "nc_get_packet_status"
    method: str = "POST"
    Req: type[BaseModel] = NcGetPacketStatusReq
    Res: type[BaseModel] = NcGetPacketStatusRes
# endregion api




# endregion code
