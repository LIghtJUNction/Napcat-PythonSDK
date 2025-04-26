# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/244510838e0
@llms.txt: https://napcat.apifox.cn/244510838e0.md
@last_update: 2025-04-26 01:17:45

@description: 发送群消息

summary:发送私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_msg"
__id__ = "244510838e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


# region req

class SendPrivateMsgReq(BaseModel):
    """
    发送私聊文件请求模型
    """

    class FileMessage(BaseModel):
        """文件消息"""
        class FileMessageData(BaseModel):
            """文件消息数据"""

            file: str = Field(
                ..., description="文件路径 (本地路径/网络路径/base64)"
            )
            name: str | None = Field(
                None, description="文件名 (可选)"
            )

        type: Literal["file"] = Field(
            "file", description="消息类型"
        )
        data: FileMessageData = Field(
            ..., description="消息数据"
        )

    user_id: int | str = Field(
        ..., description="用户ID"
    )
    message: list[FileMessage] = Field(
        ..., description="消息列表"
    )


# endregion req


# region res


class SendPrivateMsgRes(BaseModel):
    """
    发送私聊文件响应模型
    """
    class ResponseData(BaseModel):
        """响应数据"""
    
        message_id: int = Field(
            ..., description="消息ID"
        )


    status: Literal["ok"] = Field(
        "ok", description="响应状态"
    )
    retcode: int = Field(
        ..., description="响应码"
    )
    data: ResponseData = Field(
        ..., description="响应数据"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="提示"
    )
    echo: str | None = Field(
        None, description="Echo"
    )


# endregion res


# region api
class SendPrivateMsgAPI(BaseModel):
    """send_private_msg接口数据模型"""

    endpoint: str = "send_private_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendPrivateMsgReq
    Res: type[BaseModel] = SendPrivateMsgRes


# endregion api


# endregion code
