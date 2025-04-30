# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227233993e0
@llms.txt: https://napcat.apifox.cn/227233993e0.md
@last_update: 2025-04-27 00:53:41

@description: 
功能：设置在线机型
用于设置QQ在线时显示的设备类型
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_set_model_show"
__id__ = "227233993e0"
__method__ = "POST"
# endregion METADATA

# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.debug("加载 SetModelShowAPI 模型")

# region req
class SetModelShowReq(BaseModel):
    """设置在线机型请求模型"""
    model: str = Field(..., description="在线机型")
    model_show: str = Field(..., description="显示的机型")
# endregion req

# region res
class SetModelShowRes(BaseModel):
    """设置在线机型响应模型"""
    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(0, description="返回码")
    data: None = Field(None, description="响应数据体，固定为 null")
    message: str = Field("", description="消息")
    wording: str = Field("", description="额外消息或提示")
    echo: str | None = Field(None, description="回显信息") 
# endregion res

# region api
class SetModelShowAPI(BaseModel):
    """_set_model_show接口数据模型"""
    endpoint: str = "_set_model_show"
    method: str = "POST"
    Req: type[BaseModel] = SetModelShowReq
    Res: type[BaseModel] = SetModelShowRes
# endregion api
# endregion code
