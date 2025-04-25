# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226659165e0
@llms.txt: https://napcat.apifox.cn/226659165e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置私聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_private_msg_as_read"
__id__ = "226659165e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Added for status='ok' type hint

logger = logging.getLogger(__name__)

# region req
class MarkPrivateMsgAsReadReq(BaseModel):
    """
    请求模型: 设置私聊已读
    """
    user_id: int | str = Field(..., description="目标用户ID")
# endregion req



# region res
class MarkPrivateMsgAsReadRes(BaseModel):
    """
    响应模型: 设置私聊已读
    """
    status: Literal['ok'] = Field(..., description="响应状态") # 根据spec，status固定为'ok'
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据，应为null") # 根据spec，data固定为null
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应措辞")
    echo: str | None = Field(default=None, description="Echo字符串，可空") # 使用 default=None 处理 nullable
# endregion res

# region api
class MarkPrivateMsgAsReadAPI(BaseModel):
    """mark_private_msg_as_read接口数据模型"""
    endpoint: str = "mark_private_msg_as_read"
    method: str = "POST"
    Req: type[BaseModel] = MarkPrivateMsgAsReadReq
    Res: type[BaseModel] = MarkPrivateMsgAsReadRes
# endregion api




# endregion code
