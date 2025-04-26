# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/226659297e0
@llms.txt: https://napcat.apifox.cn/226659297e0.md
@last_update: 2025-04-27 00:53:40

@description: nc获取rkey

summary:nc获取rkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "nc_get_rkey"
__id__ = "226659297e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class NcGetRkeyReq(BaseModel):
    """
nc_get_rkey请求参数

请求体为空
"""
    pass
# endregion req



# region res
class NcGetRkeyRes(BaseModel):
    """
nc_get_rkey响应参数
"""

    class RkeyItem(BaseModel):
        """
        Rkey项
        """
        rkey: str = Field(..., description="rkey")
        ttl: str = Field(..., description="生存时间")
        time: float = Field(..., description="时间戳")
        type: int = Field(..., description="类型")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[RkeyItem] = Field(..., description="数据列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(..., description="echo")

# endregion res

# region api
class NcGetRkeyAPI(BaseModel):
    """nc_get_rkey接口数据模型"""
    endpoint: str = "nc_get_rkey"
    method: str = "POST"
    Req: type[BaseModel] = NcGetRkeyReq
    Res: type[BaseModel] = NcGetRkeyRes
# endregion api




# endregion code
