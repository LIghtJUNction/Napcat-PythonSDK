# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['消息相关']
@homepage: https://napcat.apifox.cn/226656712e0
@llms.txt: https://napcat.apifox.cn/226656712e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_forward_msg"
__id__ = "226656712e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetForwardMsgReq(BaseModel):
    """
    获取合并转发消息请求模型
    """
    message_id: str = Field(..., description="合并转发消息的ID")
# endregion req



# region res
class GetForwardMsgRes(BaseModel):
    """
    获取合并转发消息响应模型
    """
    status: str = Field("ok", description="响应状态，总是ok")
    retcode: int = Field(..., description="响应码")
    data: dict[str, any] = Field({}, description="响应数据，对于此接口为空对象")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词")
    echo: str | None = Field(None, description="回显")
# endregion res

# region api
class GetForwardMsgAPI(BaseModel):
    """get_forward_msg接口数据模型"""
    endpoint: str = "get_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetForwardMsgReq
    Res: type[BaseModel] = GetForwardMsgRes
# endregion api




# endregion code
