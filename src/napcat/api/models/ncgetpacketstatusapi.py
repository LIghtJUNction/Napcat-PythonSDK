# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/226659280e0
@llms.txt: https://napcat.apifox.cn/226659280e0.md
@last_update: 2025-04-27 00:53:40

@description:

summary:获取packet状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "nc_get_packet_status"
__id__ = "226659280e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class NcGetPacketStatusReq(BaseModel):
    """
    获取packet状态请求模型
    """

    pass
# endregion req



# region res
class NcGetPacketStatusRes(BaseModel):
    """
    获取packet状态响应模型
    """

    # 定义响应参数
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="API返回码")
    data: None = Field(..., description="数据载荷 (此处为null)")
    message: str = Field(..., description="API处理消息")
    wording: str = Field(..., description="API处理文案")
    echo: str | None = Field(None, description="API回显字段")

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