# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/244510830e0
@llms.txt: https://napcat.apifox.cn/244510830e0.md
@last_update: 2025-04-26 01:17:45

@description: 发送群消息

summary:发送群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_msg"
__id__ = "244510830e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal


# region req
class FileMessageData(BaseModel):
    """文件消息数据"""
    file: str = Field(..., description="文件路径，可以是本地路径、网络路径或base64编码")
    name: str | None = Field(None, description="文件名称")

class FileMessage(BaseModel):
    """文件消息类型"""
    type: Literal["file"] = Field("file", description="消息类型，固定为 file")
    data: FileMessageData = Field(..., description="文件消息数据")

class SendGroupMsgReq(BaseModel):
    """
    发送群消息请求模型
    """
    group_id: int | str = Field(..., description="群号")
    message: list[FileMessage] = Field(..., description="消息内容，只支持文件消息列表")
# endregion req



# region res
class SendGroupMsgResData(BaseModel):
    """发送群消息响应数据"""
    message_id: int = Field(..., description="消息ID")

class SendGroupMsgRes(BaseModel):
    """
    发送群消息响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: SendGroupMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo")
# endregion res

# region api
class SendGroupMsgAPI(BaseModel):
    """send_group_msg接口数据模型"""
    endpoint: Literal["send_group_msg"] = "send_group_msg"
    method: Literal["POST"] = "POST"
    Req: type[SendGroupMsgReq] = SendGroupMsgReq
    Res: type[SendGroupMsgRes] = SendGroupMsgRes
# endregion api




# endregion code
