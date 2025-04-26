# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/244510830e0
@llms.txt: https://napcat.apifox.cn/244510830e0.md
@last_update: 2025-04-27 00:53:41

@description: 发送群消息

summary:发送群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_group_msg"
__id__ = "244510830e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field


# region req
class FileMessageData(BaseModel):
    """文件消息数据"""
    file: str = Field(..., description="文件路径/URL/Base64")
    name: str | None = Field(None, description="文件名") # name is not marked as required in schema but file is.

class FileMessage(BaseModel):
    """文件消息对象"""
    type: Literal["file"] = Field("file", description="消息类型")
    data: FileMessageData = Field(..., description="文件消息数据")

class SendGroupMsgReq(BaseModel):
    """
    发送群消息请求模型
    """
    group_id: int | str = Field(..., description="群号")
    message: list[FileMessage] = Field(..., description="消息链，只支持文件消息")

# endregion req



# region res
class SendGroupMsgResData(BaseModel):
    """响应数据"""
    message_id: int = Field(..., description="消息ID")

class SendGroupMsgRes(BaseModel):
    """
    发送群消息响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: SendGroupMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应信息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class SendGroupMsgAPI(BaseModel):
    """send_group_msg接口数据模型"""
    endpoint: str = "send_group_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupMsgReq
    Res: type[BaseModel] = SendGroupMsgRes
# endregion api




# endregion code
