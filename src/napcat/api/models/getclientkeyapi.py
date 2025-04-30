# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/250286915e0
@llms.txt: https://napcat.apifox.cn/250286915e0.md
@last_update: 2025-04-30 00:00:00

@description: 
功能：获取客户端密钥
获取客户端用于加密通信的密钥信息
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_clientkey"
__id__ = "250286915e0"
__method__ = "POST"
# endregion METADATA

# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.debug("加载 GetClientkeyAPI 模型")

# region req
class GetClientkeyReq(BaseModel):
    """获取clientkey请求模型
    
    OpenAPI规范中此请求不需要任何参数
    """
    pass
# endregion req

# region res
class GetClientkeyRes(BaseModel):
    """获取clientkey响应模型"""
    class Data(BaseModel):
        """响应数据模型"""
        clientkey: str = Field(..., description="客户端密钥")

    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(0, description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示")
    echo: str | None = Field(None, description="回显内容")
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
