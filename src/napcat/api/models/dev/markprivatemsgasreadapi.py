# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659165e0
@llms.txt: https://napcat.apifox.cn/226659165e0.md
@last_update: 2025-04-27 00:53:40

@description: 设置私聊消息为已读。

summary:设置私聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "mark_private_msg_as_read"
__id__ = "226659165e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class MarkPrivateMsgAsReadReq(BaseModel):
    """
    设置私聊已读请求模型
    """

    user_id: int | str = Field(
        ..., description="对方QQ号 (必填)"
    )
# endregion req



# region res
class MarkPrivateMsgAsReadRes(BaseModel):
    """
    设置私聊已读响应模型
    """
    status: Literal["ok"] = Field(
        ..., description="状态，'ok'表示成功"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: None = Field(
        ..., description="响应数据，固定为null"
    )
    message: str = Field(
        ..., description="错误信息"
    )
    wording: str = Field(
        ..., description="错误信息的口语化描述"
    )
    echo: str | None = Field(
        None, description="请求时的echo字段"
    )
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
