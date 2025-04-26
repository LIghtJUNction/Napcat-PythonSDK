# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/保留
@homepage: https://napcat.apifox.cn/226656652e0
@llms.txt: https://napcat.apifox.cn/226656652e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:send_msg

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_msg"
__id__ = "226656652e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# Define Message Component Models

class TextData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextMessage(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型，永远为 text")
    data: TextData = Field(..., description="文本消息数据")

class AtData(BaseModel):
    qq: str | int | Literal["all"] = Field(..., description="@ 的 QQ 号，all 表示全体成员")
    name: str | None = Field(None, description="@ 的昵称，通常用于频道")

class AtMessage(BaseModel):
    type: Literal["at"] = Field("at", description="消息类型，永远为 at")
    data: AtData = Field(..., description="@ 消息数据")

class FaceData(BaseModel):
    id: int = Field(..., description="表情 ID")

class FaceMessage(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型，永远为 face")
    data: FaceData = Field(..., description="表情消息数据")

class ImageData(BaseModel):
    file: str = Field(..., description="图片文件路径，可以是本地路径、URL、或 Base64 数据")
    summary: str = Field("[图片]", description="图片外显")

class ImageMessage(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型，永远为 image")
    data: ImageData = Field(..., description="图片消息数据")

class ReplyData(BaseModel):
    id: str | int = Field(..., description="回复的消息 ID")

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型，永远为 reply")
    data: ReplyData = Field(..., description="回复消息数据")

class JsonData(BaseModel):
    data: str = Field(..., description="JSON 数据字符串")

class JsonMessage(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型，永远为 json")
    data: JsonData = Field(..., description="JSON 消息数据")

class VoiceData(BaseModel):
    file: str = Field(..., description="语音文件路径，可以是本地路径、URL、或 Base64 数据")

class VoiceMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型，永远为 record (语音)") # Note: OpenAPI spec uses 'record'
    data: VoiceData = Field(..., description="语音消息数据")

class VideoData(BaseModel):
    file: str = Field(..., description="视频文件路径，可以是本地路径、URL、或 Base64 数据")

class VideoMessage(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型，永远为 video")
    data: VideoData = Field(..., description="视频消息数据")

class MarkdownData(BaseModel):
    content: str = Field(..., description="Markdown 格式内容")

class MarkdownMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型，永远为 record (Markdown)") # Note: OpenAPI spec uses 'record'
    data: MarkdownData = Field(..., description="Markdown 消息数据")

# Union type for possible message components
MessageComponent = TextMessage | AtMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage | VoiceMessage | VideoMessage | MarkdownMessage

# region req
class SendMsgReq(BaseModel):
    """
    发送消息请求模型
    """
    message_type: Literal["group", "private"] = Field(..., description="消息类型：group 或 private")
    group_id: int | str | None = Field(None, description="群 ID，当 message_type 为 group 时必填，private 时不填")
    user_id: int | str | None = Field(None, description="用户 ID，当 message_type 为 private 时必填，group 时不填")
    message: list[MessageComponent] = Field(..., description="消息内容，数组形式，包含一个或多个消息组件")


# endregion req



# region res
class SendMsgRes(BaseModel):
    """
    发送消息响应模型
    """

    class Data(BaseModel):
        message_id: int = Field(..., description="消息 ID")

    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应描述")
    echo: str | None = Field(None, description="请求的 echo")

# endregion res

# region api
class SendMsgAPI(BaseModel):
    """send_msg接口数据模型"""
    endpoint: str = "send_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendMsgReq
    Res: type[BaseModel] = SendMsgRes
# endregion api




# endregion code
