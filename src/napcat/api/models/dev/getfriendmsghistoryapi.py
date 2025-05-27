# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659174e0
@llms.txt: https://napcat.apifox.cn/226659174e0.md
@last_update: 2025-05-28 01:34:10

@description:

summary:获取好友历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_friend_msg_history"
__id__ = "226659174e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models

class Sender(BaseModel):
    user_id: float = Field(description="user_id字段")
    nickname: str = Field(description="nickname字段")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="sex字段")
    age: float | None = Field(None, description="age字段")
    card: str = Field(description="card字段")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="role字段")

    model_config = {
        "extra": "allow",
    }

# Nested Data models for various message types
class TextMessageData(BaseModel):
    text: str = Field(description="文本内容")
    model_config = {"extra": "allow"}

class AtMessageData(BaseModel):
    qq: int | str = Field(description="艾特目标的QQ号或'all'")
    name: str | None = Field(None, description="艾特目标的名称")
    model_config = {"extra": "allow"}

class FaceMessageData(BaseModel):
    id: float = Field(description="表情ID")
    model_config = {"extra": "allow"}

class ImageMessageData(BaseModel):
    file: str = Field(description="图片文件信息")
    summary: str = Field("[图片]", description="外显")
    model_config = {"extra": "allow"}

class FileMessageData(BaseModel):
    file: str = Field(description="文件信息")
    name: str | None = Field(None, description="文件名称")
    model_config = {"extra": "allow"}

class ReplyMessageData(BaseModel):
    id: int | str = Field(description="回复的消息ID")
    model_config = {"extra": "allow"}

class JsonMessageData(BaseModel):
    data: str = Field(description="JSON字符串内容")
    model_config = {"extra": "allow"}

class VoiceMessageData(BaseModel):
    file: str = Field(description="语音文件信息")
    model_config = {"extra": "allow"}

class VideoMessageData(BaseModel):
    file: str = Field(description="视频文件信息")
    model_config = {"extra": "allow"}

class MarkdownMessageData(BaseModel):
    content: str = Field(description="Markdown内容")
    model_config = {"extra": "allow"}

# Define the message types using their respective data models
class TextMessage(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型：文本")
    data: TextMessageData = Field(description="文本消息数据")
    model_config = {"extra": "allow"}

class AtMessage(BaseModel):
    type: Literal["at"] = Field("at", description="消息类型：艾特")
    data: AtMessageData = Field(description="艾特消息数据")
    model_config = {"extra": "allow"}

class FaceMessage(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型：表情")
    data: FaceMessageData = Field(description="表情消息数据")
    model_config = {"extra": "allow"}

class ImageMessage(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型：图片")
    data: ImageMessageData = Field(description="图片消息数据")
    model_config = {"extra": "allow"}

class FileMessage(BaseModel):
    type: Literal["file"] = Field("file", description="消息类型：文件")
    data: FileMessageData = Field(description="文件消息数据")
    model_config = {"extra": "allow"}

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型：回复")
    data: ReplyMessageData = Field(description="回复消息数据")
    model_config = {"extra": "allow"}

class JsonMessage(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型：JSON")
    data: JsonMessageData = Field(description="JSON消息数据")
    model_config = {"extra": "allow"}

class VoiceMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型：语音")
    data: VoiceMessageData = Field(description="语音消息数据")
    model_config = {"extra": "allow"}

class VideoMessage(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型：视频")
    data: VideoMessageData = Field(description="视频消息数据")
    model_config = {"extra": "allow"}

class MarkdownMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型：Markdown")
    data: MarkdownMessageData = Field(description="Markdown消息数据")
    model_config = {"extra": "allow"}

# Define a Union type for all possible message parts (excluding MessageForward itself)
MessageType = (
    TextMessage | AtMessage | FaceMessage | ImageMessage | FileMessage |
    ReplyMessage | JsonMessage | VoiceMessage | VideoMessage | MarkdownMessage
)

# MessageForward needs MessageDetail, so it must be defined later or use forward reference
class MessageForwardData(BaseModel):
    id: str = Field(description="转发消息ID")
    content: list["MessageDetail"] = Field(description="转发的消息列表") # Forward reference
    model_config = {"extra": "allow"}

class MessageForward(BaseModel):
    type: Literal["forward"] = Field("forward", description="消息类型：转发")
    data: MessageForwardData = Field(description="转发消息数据")
    model_config = {"extra": "allow"}

# Now define MessageDetail (original "消息详情")
class MessageDetail(BaseModel):
    self_id: float = Field(description="机器人自身ID")
    user_id: float = Field(description="消息发送者ID")
    time: float = Field(description="消息发送时间戳")
    message_id: float = Field(description="消息ID")
    message_seq: float = Field(description="消息序列号")
    real_id: float = Field(description="真实ID")
    real_seq: str = Field(description="真实序列号")
    message_type: str = Field(description="消息类型")
    sender: Sender = Field(description="发送者信息")
    raw_message: str = Field(description="原始消息内容")
    font: float = Field(description="字体")
    sub_type: str = Field(description="子类型")
    message: list[MessageType | MessageForward] = Field(description="消息链内容，包含多种消息类型")
    message_format: str = Field(description="消息格式")
    post_type: str = Field(description="上报类型")
    group_id: float | None = Field(None, description="群组ID（私聊时可能为None）")

    model_config = {
        "extra": "allow",
    }
# Fix forward reference for MessageForwardData.content
MessageForwardData.model_rebuild()


# region component_models/

# region req
class GetFriendMsgHistoryReq(BaseModel):
    """获取好友历史消息请求体"""
    user_id: int | str = Field(description="好友QQ号")
    message_seq: int | str | None = Field(None, description="从哪个消息序列号开始获取，0为最新")
    count: float = Field(20.0, description="获取消息的数量，默认20")
    reverseOrder: bool = Field(False, description="是否倒序获取消息，默认false（即正序）")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFriendMsgHistoryRes(BaseModel):
    """获取好友历史消息响应体"""
    class Data(BaseModel):
        """响应数据类型"""
        messages: list[MessageDetail] = Field(description="好友历史消息列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: float = Field(0.0, description="响应码")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field("", description="错误信息")
    wording: str = Field("", description="错误详情")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetFriendMsgHistoryAPI(BaseModel):
    """get_friend_msg_history接口数据模型"""
    endpoint: str = "get_friend_msg_history"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendMsgHistoryReq
    Res: type[BaseModel] = GetFriendMsgHistoryRes

# region api/
# endregion code
