# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226657401e0
@llms.txt: https://napcat.apifox.cn/226657401e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_msg_history"
__id__ = "226657401e0"
__method__ = "POST"

# endregion METADATA


# region code
from enum import Enum
from pydantic import BaseModel, Field

# region req
class GetGroupMsgHistoryReq(BaseModel):
    """获取群历史消息请求数据模型"""
    group_id: int | str = Field(..., description="群号")
    message_seq: int | str = Field(default=0, description="0为最新")
    count: int = Field(default=20, description="数量")
    reverseOrder: bool = Field(default=False, description="倒序")
# endregion req


# region common models (Used in Response)
class Sex(Enum):
    male = "male"
    female = "female"
    unknown = "unknown"

class Role(Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

class Sender(BaseModel):
    """发送者信息"""
    user_id: int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    sex: Sex | None = Field(default=None, description="性别")
    age: int | None = Field(default=None, description="年龄")
    card: str | None = Field(default=None, description="群名片")
    role: Role | None = Field(default=None, description="群角色")

# Message Content Types

class TextData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextMsg(BaseModel):
    type: str = Field("text", const=True, description="消息类型: text")
    data: TextData

class AtData(BaseModel):
    qq: int | str = Field(..., description="@的QQ号，all为@全体成员")
    name: str | None = Field(default=None, description="@的群成员的昵称，仅在 @全体成员 时有效")

class AtMsg(BaseModel):
    type: str = Field("at", const=True, description="消息类型: at")
    data: AtData

class FaceData(BaseModel):
    id: int = Field(..., description="表情ID")

class FaceMsg(BaseModel):
    type: str = Field("face", const=True, description="消息类型: face")
    data: FaceData

class ImageData(BaseModel):
    file: str = Field(..., description="图片文件")
    summary: str = Field(default="[图片]", description="图片摘要")

class ImageMsg(BaseModel):
    type: str = Field("image", const=True, description="消息类型: image")
    data: ImageData

class FileData(BaseModel):
    file: str = Field(..., description="文件路径/ID")
    name: str | None = Field(default=None, description="文件名")

class FileMsg(BaseModel):
    type: str = Field("file", const=True, description="消息类型: file")
    data: FileData

class ReplyData(BaseModel):
    id: int | str = Field(..., description="回复的消息ID")

class ReplyMsg(BaseModel):
    type: str = Field("reply", const=True, description="消息类型: reply")
    data: ReplyData

class JsonData(BaseModel):
    data: str = Field(..., description="JSON字符串内容")

class JsonMsg(BaseModel):
    type: str = Field("json", const=True, description="消息类型: json")
    data: JsonData

class VoiceData(BaseModel):
    file: str = Field(..., description="语音文件路径/ID")

class VoiceMsg(BaseModel):
    type: str = Field("record", const=True, description="消息类型: record (语音)") # Note: record for voice/markdown
    data: VoiceData

class VideoData(BaseModel):
    file: str = Field(..., description="视频文件路径/ID")

class VideoMsg(BaseModel):
    type: str = Field("video", const=True, description="消息类型: video")
    data: VideoData

class MarkdownData(BaseModel):
    content: str = Field(..., description="Markdown文本内容")

class MarkdownMsg(BaseModel):
    type: str = Field("record", const=True, description="消息类型: record (markdown)") # Note: record for voice/markdown
    data: MarkdownData

# ForwardMsg requires recursion, define MessageDetail first

class MessageDetail(BaseModel):
    """消息详情"""
    self_id: int = Field(..., description="机器人自身ID")
    user_id: int = Field(..., description="发送者用户ID")
    time: int = Field(..., description="消息时间戳")
    message_id: int = Field(..., description="消息ID")
    message_seq: int = Field(..., description="消息序列号")
    real_id: int = Field(..., description="真实消息ID")
    real_seq: str = Field(..., description="真实消息序列号")
    message_type: str = Field(..., description="消息类型，如 group")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="子类型，如 normal")
    message: list[TextMsg | AtMsg | FaceMsg | ImageMsg | FileMsg | ReplyMsg | JsonMsg | VoiceMsg | VideoMsg | MarkdownMsg | 'ForwardMsg'] = Field(..., description="消息段列表")
    message_format: str = Field(..., description="消息格式，如 string, array")
    post_type: str = Field(..., description="上报类型，如 message")
    group_id: int | None = Field(default=None, description="群号 (仅群消息有)") # Added optionality based on context

class ForwardData(BaseModel):
    id: str = Field(..., description="转发消息ID")
    content: list[MessageDetail] = Field(..., description="转发消息内容列表")

class ForwardMsg(BaseModel):
    type: str = Field("forward", const=True, description="消息类型: forward")
    data: ForwardData

# Update MessageDetail forward reference
MessageDetail.model_rebuild()

# endregion common models

# region res
class GetGroupMsgHistoryResData(BaseModel):
    """获取群历史消息响应数据"""
    messages: list[MessageDetail] = Field(..., description="消息列表")

class GetGroupMsgHistoryRes(BaseModel):
    """获取群历史消息响应数据模型"""
    status: str = Field("ok", const=True, description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: GetGroupMsgHistoryResData = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="补充信息")
    echo: str | None = Field(default=None, description="echo")
# endregion res

# region api
class GetGroupMsgHistoryAPI(BaseModel):
    """get_group_msg_history接口数据模型"""
    endpoint: str = "get_group_msg_history"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupMsgHistoryReq
    Res: type[BaseModel] = GetGroupMsgHistoryRes
# endregion api

# endregion code