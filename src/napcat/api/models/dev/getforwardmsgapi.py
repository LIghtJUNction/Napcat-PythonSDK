# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: [
    "消息相关"
]
@homepage: https://napcat.apifox.cn/226656712e0
@llms.txt: https://napcat.apifox.cn/226656712e0.md
@last_update: 2025-04-27 00:53:40

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

from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetForwardMsgReq(BaseModel):
    """
    获取合并转发消息请求模型
    """
    message_id: str = Field(..., description="合并转发消息ID")
# endregion req


# region res

# Define nested models for message components

class TextMessageData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextMessage(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型")
    data: TextMessageData = Field(..., description="消息数据")

class AtMessageData(BaseModel):
    qq: int | str = Field(..., description="被艾特用户的QQ号，或者all")
    name: str | None = Field(None, description="被艾特用户的群名片或昵称")

class AtMessage(BaseModel):
    type: Literal["at"] = Field("at", description="消息类型")
    data: AtMessageData = Field(..., description="消息数据")

class FaceMessageData(BaseModel):
    id: int = Field(..., description="表情ID")

class FaceMessage(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型")
    data: FaceMessageData = Field(..., description="消息数据")

class ImageMessageData(BaseModel):
    file: str = Field(..., description="图片文件名或链接")
    summary: str = Field("[图片]", description="外显")

class ImageMessage(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型")
    data: ImageMessageData = Field(..., description="消息数据")

class ReplyMessageData(BaseModel):
    id: int | str = Field(..., description="回复消息的ID")

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型")
    data: ReplyMessageData = Field(..., description="消息数据")

class JsonMessageData(BaseModel):
    data: str = Field(..., description="JSON字符串")

class JsonMessage(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型")
    data: JsonMessageData = Field(..., description="消息数据")

# Note: OpenAPI spec uses 'record' for both voice and markdown
# Pydantic Union handles this by trying models in order.

class VoiceMessageData(BaseModel):
    file: str = Field(..., description="语音文件名或链接")

class VoiceMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型 (语音)")
    data: VoiceMessageData = Field(..., description="消息数据")

class MarkdownMessageData(BaseModel):
    content: str = Field(..., description="Markdown内容")

class MarkdownMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型 (Markdown)")
    data: MarkdownMessageData = Field(..., description="消息数据")

class FileMessageData(BaseModel):
    file: str = Field(..., description="文件名或链接")
    name: str | None = Field(None, description="文件名") # Not required in schema

class FileMessage(BaseModel):
    type: Literal["file"] = Field("file", description="消息类型")
    data: FileMessageData = Field(..., description="消息数据")

# Define the union of all possible message component types
AnyOfMessageTypes = TextMessage | AtMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage | VoiceMessage | VideoMessage | FileMessage | MarkdownMessage # ForwardMessage is handled separately within MessageDetail

class Sender(BaseModel):
    user_id: int = Field(..., description="发送者QQ号")
    nickname: str = Field(..., description="发送者昵称")
    sex: Literal["male", "female", "unknown"] = Field(..., description="性别")
    age: int | None = Field(None, description="年龄")
    card: str = Field(..., description="群名片")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="群角色") # Not required in schema

class MessageDetail(BaseModel):
    # Note: This model represents an item within the 'message' array in the response data, and also the content of a 'forward' message.
    self_id: int = Field(..., description="机器人QQ号")
    user_id: int = Field(..., description="消息发送者QQ号")
    time: int = Field(..., description="消息发送时间 (Unix timestamp)")
    message_id: int = Field(..., description="消息ID")
    message_seq: int = Field(..., description="消息序列号")
    real_id: int = Field(..., description="真实消息ID")
    real_seq: str = Field(..., description="真实消息序列号")
    message_type: str = Field(..., description="消息类型，如private, group")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始CQ码消息")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="消息子类型")
    message: list[AnyOfMessageTypes | 'ForwardMessage'] = Field(..., description="消息内容，数组形式，每个元素是不同的消息段") # Needs forward declaration due to recursion
    message_format: str = Field(..., description="消息格式，如array")
    post_type: str = Field(..., description="上报类型")
    group_id: int | None = Field(None, description="群号 (仅群消息) ") # Not required in schema

class VideoMessageData(BaseModel):
    file: str = Field(..., description="视频文件名或链接")

class VideoMessage(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型")
    data: VideoMessageData = Field(..., description="消息数据")

# Define the recursive ForwardMessage here after MessageDetail
class ForwardMessageData(BaseModel):
    id: str = Field(..., description="合并转发消息ID")
    content: list[MessageDetail] = Field(..., description="合并转发消息内容")

class ForwardMessage(BaseModel):
    type: Literal["forward"] = Field("forward", description="消息类型")
    data: ForwardMessageData = Field(..., description="消息数据")

# Update MessageDetail's 'message' field definition after ForwardMessage is defined
MessageDetail.model_rebuild()

class GetForwardMsgRes(BaseModel):
    """
    获取合并转发消息响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        # The 'message' field here is an array of MessageDetail
        message: list[MessageDetail] = Field(..., description="合并转发消息的详细内容列表")

    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: int = Field(..., description="响应码") # Schema says number, int is common for retcode
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="中文描述")
    echo: str | None = Field(None, description="Echo回显")

# endregion res

# region api
class GetForwardMsgAPI(BaseModel):
    """get_forward_msg接口数据模型"""
    endpoint: str = "get_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetForwardMsgReq
    Res: type[BaseModel] = GetForwardMsgRes
# endregion api


# endregion code