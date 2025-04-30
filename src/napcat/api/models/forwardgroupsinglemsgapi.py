# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/226659074e0
@llms.txt: https://napcat.apifox.cn/226659074e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:消息转发到群

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "forward_group_single_msg"
__id__ = "226659074e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class ForwardGroupSingleMsgReq(BaseModel):
    """
    请求模型：消息转发到群
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    message_id: int | str = Field(
        ..., description="消息ID"
    )
# endregion req



# region res
class ForwardGroupSingleMsgRes(BaseModel):
    """
    响应模型：消息转发到群
    """
    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: None = Field(
        ..., description="响应数据"
    )
    message: str = Field(
        ..., description="错误信息"
    )
    wording: str = Field(
        ..., description="错误信息的自然语言描述"
    )
    echo: str | None = Field(
        None,
        description="echo",
    )
# endregion res

# region api
class ForwardGroupSingleMsgAPI(BaseModel):
    """forward_group_single_msg接口数据模型"""
    endpoint: str = "forward_group_single_msg"
    method: str = "POST"
    Req: type[BaseModel] = ForwardGroupSingleMsgReq
    Res: type[BaseModel] = ForwardGroupSingleMsgRes
# endregion api




# endregion code