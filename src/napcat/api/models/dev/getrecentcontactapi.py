# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659190e0
@llms.txt: https://napcat.apifox.cn/226659190e0.md
@last_update: 2025-04-27 00:53:40

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
import logging
from typing import Literal, Union
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetRecentContactReq(BaseModel):
    """
    获取最近消息列表的请求模型
    """
    count: int = Field(..., description="会话数量")
# endregion req


# region res
# Define nested models based on OpenAPI spec components and response structure

# Message Components Base
class MessageComponentBase(BaseModel):
    type: str = Field(..., description="消息类型")

# Specific Message Component Data Models
class TextMessageData(BaseModel):
    text: str = Field(..., description="文本内容")

class AtMessageData(BaseModel):
    qq: str | int | Literal["all"] = Field(..., description="艾特的QQ号或all")
    name: str | None = Field(None, description="艾特的群名片 (可选)")

class FaceMessageData(BaseModel):
    id: int = Field(..., description="表情ID")

class ImageMessageData(BaseModel):
    file: str = Field(..., description="图片文件标识")
    summary: str = Field("[图片]", description="外显描述")

class FileMessageData(BaseModel):
    file: str = Field(..., description="文件文件标识")
    name: str | None = Field(None, description="文件名 (可选)")

class ReplyMessageData(BaseModel):
    id: str | int = Field(..., description="回复消息的ID")

class JsonMessageData(BaseModel):
    data: str = Field(..., description="JSON字符串内容")

class VoiceMessageData(BaseModel):
    file: str = Field(..., description="语音文件标识")

class VideoMessageData(BaseModel):
    file: str = Field(..., description="视频文件标识")

class MarkdownMessageData(BaseModel):
    content: str = Field(..., description="Markdown内容")

class ForwardMessageData(BaseModel):
    id: str = Field(..., description="Forward消息ID")
    content: list["MessageComponentUnion"] = Field(..., description="Forward消息内容列表") # Forward reference

# Specific Message Component Models (Inherit from base and use specific data model)
class TextMessage(MessageComponentBase):
    type: Literal["text"] = Field("text", description="消息类型: 文本")
    data: TextMessageData = Field(..., description="消息数据")

class AtMessage(MessageComponentBase):
    type: Literal["at"] = Field("at", description="消息类型: 艾特")
    data: AtMessageData = Field(..., description="消息数据")

class FaceMessage(MessageComponentBase):
    type: Literal["face"] = Field("face", description="消息类型: 表情")
    data: FaceMessageData = Field(..., description="消息数据")

class ImageMessage(MessageComponentBase):
    type: Literal["image"] = Field("image", description="消息类型: 图片")
    data: ImageMessageData = Field(..., description="消息数据")

class FileMessage(MessageComponentBase):
    type: Literal["file"] = Field("file", description="消息类型: 文件")
    data: FileMessageData = Field(..., description="消息数据")

class ReplyMessage(MessageComponentBase):
    type: Literal["reply"] = Field("reply", description="消息类型: 回复")
    data: ReplyMessageData = Field(..., description="消息数据")

class JsonMessage(MessageComponentBase):
    type: Literal["json"] = Field("json", description="消息类型: JSON")
    data: JsonMessageData = Field(..., description="消息数据")

class VoiceMessage(MessageComponentBase):
    type: Literal["record"] = Field("record", description="消息类型: 录音")
    data: VoiceMessageData = Field(..., description="消息数据")

class VideoMessage(MessageComponentBase):
    type: Literal["video"] = Field("video", description="消息类型: 视频")
    data: VideoMessageData = Field(..., description="消息数据")

class MarkdownMessage(MessageComponentBase):
     # Potential spec issue: type is 'record', same as VoiceMessage.
     type: Literal["record"] = Field("record", description="消息类型: Markdown (Potential spec issue: same type as voice)")
     data: MarkdownMessageData = Field(..., description="消息数据")

class ForwardMessage(MessageComponentBase):
    type: Literal["forward"] = Field("forward", description="消息类型: Forward")
    data: ForwardMessageData = Field(..., description="消息数据")

# Define the Union for message components
MessageComponentUnion = Union[
    TextMessage, AtMessage, FaceMessage, ImageMessage, FileMessage,
    ReplyMessage, JsonMessage, VoiceMessage, VideoMessage, MarkdownMessage,
    ForwardMessage # Now defined
]

# Resolve forward references now that all component classes are defined
ForwardMessageData.model_rebuild()


class Sender(BaseModel):
    """
    发送者信息
    """
    user_id: int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="性别")
    age: int | None = Field(None, description="年龄")
    card: str = Field(..., description="群名片")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="群角色")

class LatestMessage(BaseModel):
    """
    最新消息内容 (基于消息详情 schema with overrides)
    """
    self_id: int = Field(..., description="机器人自身ID")
    user_id: int = Field(..., description="消息发送者ID")
    time: int = Field(..., description="消息发送时间戳")
    # Following the override suggestion of null/absence
    message_id: int | None = Field(None, description="消息ID (可能为null)") # Required in base, null in override
    message_seq: int | None = Field(None, description="消息序号 (可能为null)") # Required in base, null in override
    real_id: int | None = Field(None, description="真实消息ID (可能为null)") # Required in base, null in override
    real_seq: str = Field(..., description="真实消息序号") # Required
    message_type: str = Field(..., description="消息类型 (如: private, group)") # Required
    sender: Sender = Field(..., description="发送者信息") # Required
    raw_message: str = Field(..., description="原始消息内容") # Required
    font: int = Field(..., description="字体") # Required
    sub_type: str = Field(..., description="消息子类型") # Required
    message: list[MessageComponentUnion] = Field(..., description="消息内容列表 (分解后的CQ码)") # Required
    message_format: str = Field(..., description="消息格式") # Required
    post_type: str = Field(..., description="上报类型") # Required
    group_id: int | None = Field(None, description="群ID (私聊时为null)") # Not required

class RecentContactItem(BaseModel):
    """
    最近联系人列表项
    """
    lastestMsg: LatestMessage = Field(..., description="最新消息内容")
    peerUin: str = Field(..., description="对方账号")
    remark: str = Field(..., description="备注")
    msgTime: str = Field(..., description="消息时间")
    chatType: int = Field(..., description="会话类型") # Spec is number, assuming int
    msgId: str = Field(..., description="消息ID")
    sendNickName: str = Field(..., description="发送人昵称")
    sendMemberName: str = Field(..., description="发送人成员名")
    peerName: str = Field(..., description="对方昵称")


class GetRecentContactRes(BaseModel):
    """
    获取最近消息列表的响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码") # Spec is number, assuming int
    data: list[RecentContactItem] = Field(..., description="最近消息列表数据") # Corrected: data is the list directly
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo字段") # Nullable in spec


# endregion res

# region api
class GetRecentContactAPI(BaseModel):
    """get_recent_contact接口数据模型"""
    endpoint: str = "get_recent_contact"
    method: str = "POST"
    Req: type[GetRecentContactReq] = GetRecentContactReq
    Res: type[GetRecentContactRes] = GetRecentContactRes
# endregion api


# endregion code
