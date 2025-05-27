# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656712e0
@llms.txt: https://napcat.apifox.cn/226656712e0.md
@last_update: 2025-05-28 01:34:08

@description: 

summary:获取合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_forward_msg"
__id__ = "226656712e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal, Union

# region component_models

# Enum for sender sex
class SenderSex(Literal["male", "female", "unknown"]):
    pass

# Enum for sender role
class SenderRole(Literal["owner", "admin", "member"]):
    pass

class Sender(BaseModel):
    user_id: float = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    sex: SenderSex | None = Field(None, description="性别")
    age: float | None = Field(None, description="年龄")
    card: str = Field(..., description="群名片")
    role: SenderRole | None = Field(None, description="群成员角色")

    model_config = {
        "extra": "allow",
    }

# Define specific message data models
class TextData(BaseModel):
    text: str = Field(..., description="文本内容")

    model_config = {
        "extra": "allow",
    }

class AtData(BaseModel):
    qq: str | float | Literal["all"] = Field(..., description="艾特的QQ号或'all'")
    name: str | None = Field(None, description="艾特的名称")

    model_config = {
        "extra": "allow",
    }

class FaceData(BaseModel):
    id: float = Field(..., description="表情ID")

    model_config = {
        "extra": "allow",
    }

class ImageData(BaseModel):
    file: str = Field(..., description="图片文件ID")
    summary: str = Field("[图片]", description="外显文本")

    model_config = {
        "extra": "allow",
    }

class ReplyData(BaseModel):
    id: str | float = Field(..., description="回复消息ID")

    model_config = {
        "extra": "allow",
    }

class JsonData(BaseModel):
    data: str = Field(..., description="JSON数据")

    model_config = {
        "extra": "allow",
    }

class VoiceData(BaseModel):
    file: str = Field(..., description="语音文件ID")

    model_config = {
        "extra": "allow",
    }

class VideoData(BaseModel):
    file: str = Field(..., description="视频文件ID")

    model_config = {
        "extra": "allow",
    }

class MarkdownData(BaseModel):
    content: str = Field(..., description="Markdown内容")

    model_config = {
        "extra": "allow",
    }

class FileData(BaseModel):
    file: str = Field(..., description="文件ID")
    name: str | None = Field(None, description="文件名")

    model_config = {
        "extra": "allow",
    }

# Define the message types themselves, using the data models
class TextMessage(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型")
    data: TextData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class AtMessage(BaseModel):
    type: Literal["at"] = Field("at", description="消息类型")
    data: AtData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class FaceMessage(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型")
    data: FaceData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class ImageMessage(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型")
    data: ImageData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型")
    data: ReplyData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class JsonMessage(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型")
    data: JsonData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class VoiceMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型")
    data: VoiceData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class VideoMessage(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型")
    data: VideoData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class MarkdownMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型")
    data: MarkdownData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

class FileMessage(BaseModel):
    type: Literal["file"] = Field("file", description="消息类型")
    data: FileData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

# MessageDetail must be defined before ForwardMessage can fully use it in its content list
class MessageDetail(BaseModel):
    self_id: float = Field(..., description="自身ID")
    user_id: float = Field(..., description="用户ID")
    time: float = Field(..., description="时间戳")
    message_id: float = Field(..., description="消息ID")
    message_seq: float = Field(..., description="消息序列号")
    real_id: float = Field(..., description="真实ID")
    real_seq: str = Field(..., description="真实序列号")
    message_type: str = Field(..., description="消息类型")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: float = Field(..., description="字体")
    sub_type: str = Field(..., description="子类型")
    message: list[Union[TextMessage, AtMessage, FaceMessage, ImageMessage, ReplyMessage, JsonMessage, VoiceMessage, VideoMessage, MarkdownMessage, FileMessage, 'ForwardMessage']] = Field(default_factory=list, description="消息内容列表")
    message_format: str = Field(..., description="消息格式")
    post_type: str = Field(..., description="事件类型")
    group_id: float | None = Field(None, description="群ID (如果是群消息)")

    model_config = {
        "extra": "allow",
    }

class ForwardData(BaseModel):
    id: str = Field(..., description="转发消息ID")
    content: list[MessageDetail] = Field(default_factory=list, description="转发消息内容列表")

    model_config = {
        "extra": "allow",
    }

class ForwardMessage(BaseModel):
    type: Literal["forward"] = Field("forward", description="消息类型")
    data: ForwardData = Field(..., description="消息数据")

    model_config = {
        "extra": "allow",
    }

# Update MessageDetail's message field to include the now-defined ForwardMessage
# This is done for handling circular references if Pydantic needs it at runtime, though for type hints it's often automatic.
MessageDetail.model_fields['message'].annotation = list[Union[TextMessage, AtMessage, FaceMessage, ImageMessage, ReplyMessage, JsonMessage, VoiceMessage, VideoMessage, MarkdownMessage, FileMessage, ForwardMessage]]

class GetCombinedForwardMessage(BaseModel):
    self_id: float = Field(..., description="自身ID")
    user_id: float = Field(..., description="用户ID")
    time: float = Field(..., description="时间戳")
    message_id: float = Field(..., description="消息ID")
    message_seq: float = Field(..., description="消息序列号")
    real_id: float = Field(..., description="真实ID")
    real_seq: str = Field(..., description="真实序列号")
    message_type: str = Field(..., description="消息类型")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: float = Field(..., description="字体")
    sub_type: str = Field(..., description="子类型")
    message: list[Union[TextMessage, AtMessage, FaceMessage, ImageMessage, ReplyMessage, JsonMessage, VoiceMessage, VideoMessage, MarkdownMessage, FileMessage, ForwardMessage]] = Field(default_factory=list, description="消息内容列表")
    message_format: str = Field(..., description="消息格式")
    post_type: str = Field(..., description="事件类型")
    group_id: float | None = Field(None, description="群ID (如果是群消息)")

    model_config = {
        "extra": "allow",
    }

# region component_models/

# region req
class GetForwardMsgReq(BaseModel):
    """获取合并转发消息请求"""
    message_id: str = Field(..., description="合并转发消息ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetForwardMsgRes(BaseModel):
    """获取合并转发消息响应"""
    class Data(BaseModel):
        """响应数据类型"""
        message: list[GetCombinedForwardMessage] = Field(default_factory=list, description="合并转发消息列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: float = Field(0.0, description="响应码")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field("", description="错误信息")
    wording: str = Field("", description="错误提示")
    echo: str | None = Field(None, description="回声")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetForwardMsgAPI(BaseModel):
    """get_forward_msg接口数据模型"""
    endpoint: str = "get_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetForwardMsgReq
    Res: type[BaseModel] = GetForwardMsgRes

# region api/
# endregion code
