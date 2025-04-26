# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/244510838e0
@llms.txt: https://napcat.apifox.cn/244510838e0.md
@last_update: 2025-04-27 00:53:41

@description: 发送群消息

summary:发送私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
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
class FileData(BaseModel):
    """文件消息数据详情"""
    file: str = Field(..., description="文件路径或URL (本地路径, 网络路径, base64或DataUrl)")
    name: str | None = Field(None, description="文件名")

class FileMessage(BaseModel):
    """文件消息"""
    type: Literal["file"] = Field("file", description="消息类型，固定为 file")
    data: FileData = Field(..., description="文件数据详情")

class SendPrivateMsgReq(BaseModel):
    """
    发送私聊消息请求模型
    """
    user_id: str | int = Field(..., description="私聊对象 QQ 号")
    message: list[FileMessage] = Field(..., description="文件消息列表")
# endregion req



# region res
class SendPrivateMsgRes(BaseModel):
    """
    发送私聊消息响应模型
    """
    class Data(BaseModel):
        """
        响应数据详情
        """
        message_id: int = Field(..., description="消息ID")

    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据详情")
    message: str = Field("", description="响应消息")
    wording: str = Field("", description="响应提示")
    echo: str | None = Field(None, description="回显")
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
