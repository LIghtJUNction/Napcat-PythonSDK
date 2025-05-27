# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659190e0
@llms.txt: https://napcat.apifox.cn/226659190e0.md
@last_update: 2025-05-28 01:34:10

@description: 获取的最新消息是每个会话最新的消息

summary:最近消息列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_recent_contact"
__id__ = "226659190e0"
__method__ = "POST"

# endregion METADATA


# region code
from __future__ import annotations # Enable postponed evaluation of type annotations
from pydantic import BaseModel, Field
from typing import Literal, Union

# region component_models

class Sender(BaseModel):
    user_id: float = Field(description="用户ID")
    nickname: str = Field(description="用户昵称")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="性别，male/female/unknown")
    age: float | None = Field(None, description="年龄")
    card: str = Field(description="群名片")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="群成员角色，owner/admin/member")

    model_config = {
        "extra": "allow",
    }

class TextMessageData(BaseModel):
    text: str = Field(description="文本内容")

    model_config = {
        "extra": "allow",
    }

class TextMessage(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型")
    data: TextMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class AtMessageData(BaseModel):
    qq: str | int | Literal["all"] = Field(description="被艾特用户的QQ号，或 'all' 表示艾特全体成员")
    name: str | None = Field(None, description="被艾特用户的昵称 (仅在群聊中有效)")

    model_config = {
        "extra": "allow",
    }

class AtMessage(BaseModel):
    type: Literal["at"] = Field("at", description="消息类型")
    data: AtMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class FaceMessageData(BaseModel):
    id: float = Field(description="表情ID")

    model_config = {
        "extra": "allow",
    }

class FaceMessage(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型")
    data: FaceMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class ImageMessageData(BaseModel):
    file: str = Field(description="图片文件ID或URL")
    summary: str = Field("[图片]", description="外显文本，默认为'[图片]'")

    model_config = {
        "extra": "allow",
    }

class ImageMessage(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型")
    data: ImageMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class FileMessageData(BaseModel):
    file: str = Field(description="文件ID或URL")
    name: str | None = Field(None, description="文件名")

    model_config = {
        "extra": "allow",
    }

class FileMessage(BaseModel):
    type: Literal["file"] = Field("file", description="消息类型")
    data: FileMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class ReplyMessageData(BaseModel):
    id: str | float = Field(description="被回复消息的ID (可以是字符串或数字)")

    model_config = {
        "extra": "allow",
    }

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型")
    data: ReplyMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class JsonMessageData(BaseModel):
    data: str = Field(description="JSON字符串内容 (字段名为'data')")

    model_config = {
        "extra": "allow",
    }

class JsonMessage(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型")
    data: JsonMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class VoiceMessageData(BaseModel):
    file: str = Field(description="语音文件ID或URL")

    model_config = {
        "extra": "allow",
    }

class VoiceMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型 (OpenAPI const: record)")
    data: VoiceMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class VideoMessageData(BaseModel):
    file: str = Field(description="视频文件ID或URL")

    model_config = {
        "extra": "allow",
    }

class VideoMessage(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型")
    data: VideoMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

class MarkdownMessageData(BaseModel):
    content: str = Field(description="Markdown内容")

    model_config = {
        "extra": "allow",
    }

class MarkdownMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型 (OpenAPI const: record)")
    data: MarkdownMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

# Define a Union type for all possible message segments.
# Using __future__.annotations allows string literals for types not yet defined.
MessageSegment = Union[
    TextMessage, AtMessage, FaceMessage, ImageMessage, FileMessage,
    ReplyMessage, JsonMessage, VoiceMessage, VideoMessage, MarkdownMessage,
    "ForwardMessage" # Use string literal for ForwardMessage due to circular dependency
]

class MessageDetail(BaseModel):
    self_id: float = Field(description="机器人自身ID")
    user_id: float = Field(description="用户ID")
    time: float = Field(description="消息时间戳")
    message_id: float | None = Field(None, description="消息ID (可能为空)")
    message_seq: float | None = Field(None, description="消息序列号 (可能为空)")
    real_id: float | None = Field(None, description="真实消息ID (可能为空)")
    real_seq: str = Field(description="真实消息序列号")
    message_type: str = Field(description="消息类型 (e.g., private, group)")
    sender: Sender = Field(description="发送者信息")
    raw_message: str = Field(description="原始消息字符串")
    font: float = Field(description="字体")
    sub_type: str = Field(description="子类型 (e.g., normal, anonymous)")
    message: list[MessageSegment] = Field(description="消息段列表")
    message_format: str = Field(description="消息格式")
    post_type: str = Field(description="上报类型 (e.g., message)")
    group_id: float | None = Field(None, description="群组ID (如果是群消息，可能为空)")

    model_config = {
        "extra": "allow",
    }

class ForwardMessageData(BaseModel):
    id: str = Field(description="转发消息ID")
    content: list[MessageDetail] = Field(description="转发消息内容列表")

    model_config = {
        "extra": "allow",
    }

class ForwardMessage(BaseModel):
    type: Literal["forward"] = Field("forward", description="消息类型")
    data: ForwardMessageData = Field(description="数据字段")

    model_config = {
        "extra": "allow",
    }

# endregion component_models/

# region req
class GetRecentContactReq(BaseModel):
    """最近消息列表的请求模型"""
    count: float | None = Field(None, description="会话数量，可选，用于限制返回的最近会话数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetRecentContactRes(BaseModel):
    """最近消息列表的响应模型"""

    class RecentContactItem(BaseModel):
        """最近联系人项"""
        lastestMsg: MessageDetail = Field(description="最新消息内容")
        peerUin: str = Field(description="对方账号")
        remark: str = Field(description="备注信息")
        msgTime: str = Field(description="消息时间")
        chatType: float = Field(description="聊天类型")
        msgId: str = Field(description="消息ID")
        sendNickName: str = Field(description="发送人昵称")
        sendMemberName: str = Field(description="发送成员名称")
        peerName: str = Field(description="对方昵称")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="响应状态，固定为'ok'")
    retcode: float = Field(0, description="返回码")
    data: list[RecentContactItem] = Field(description="响应数据列表，包含最近联系人信息")
    message: str = Field("", description="响应消息")
    wording: str = Field("", description="提示语")
    echo: str | None = Field(None, description="回显信息，可能为空")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetRecentContactAPI(BaseModel):
    """get_recent_contact接口数据模型"""
    endpoint: str = "get_recent_contact"
    method: str = "POST"
    Req: type[BaseModel] = GetRecentContactReq
    Res: type[BaseModel] = GetRecentContactRes

# region api/
# endregion code
