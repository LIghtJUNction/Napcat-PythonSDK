# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656707e0
@llms.txt: https://napcat.apifox.cn/226656707e0.md
@last_update: 2025-05-28 01:34:08

@description:

summary:获取消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_msg"
__id__ = "226656707e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal
from enum import Enum
import logging

logger = logging.getLogger(__name__)

# region component_models

# Enums
class SexEnum(str, Enum):
    """性别枚举"""
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"

class RoleEnum(str, Enum):
    """群成员角色枚举"""
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"

class Sender(BaseModel):
    """发送者信息"""
    user_id: float = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    card: str = Field(..., description="群名片")
    sex: SexEnum | None = Field(None, description="性别")
    age: float | None = Field(None, description="年龄")
    role: RoleEnum | None = Field(None, description="角色")

    model_config = {
        "extra": "allow",
    }

# Message Segment Data Models (nested)
class TextMessage(BaseModel):
    """文本消息"""
    type: Literal["text"] = Field("text", description="消息类型，固定为'text'")
    class Data(BaseModel):
        text: str = Field(..., description="文本内容")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class AtMessage(BaseModel):
    """艾特消息"""
    type: Literal["at"] = Field("at", description="消息类型，固定为'at'")
    class Data(BaseModel):
        qq: str | int | Literal["all"] = Field(..., description="被艾特QQ或'all'")
        name: str | None = Field(None, description="名称 (如果QQ为all则为群名)")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class FaceMessage(BaseModel):
    """表情消息"""
    type: Literal["face"] = Field("face", description="消息类型，固定为'face'")
    class Data(BaseModel):
        id: float = Field(..., description="表情ID")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class ImageMessage(BaseModel):
    """图片消息"""
    type: Literal["image"] = Field("image", description="消息类型，固定为'image'")
    class Data(BaseModel):
        file: str = Field(..., description="图片文件路径或URL")
        summary: str = Field("[图片]", description="外显")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class FileMessage(BaseModel):
    """文件消息"""
    type: Literal["file"] = Field("file", description="消息类型，固定为'file'")
    class Data(BaseModel):
        file: str = Field(..., description="文件路径或URL")
        name: str | None = Field(None, description="文件名")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class ReplyMessage(BaseModel):
    """回复消息"""
    type: Literal["reply"] = Field("reply", description="消息类型，固定为'reply'")
    class Data(BaseModel):
        id: str | float = Field(..., description="回复消息ID")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class JsonMessage(BaseModel):
    """JSON消息"""
    type: Literal["json"] = Field("json", description="消息类型，固定为'json'")
    class Data(BaseModel):
        data: str = Field(..., description="JSON字符串内容")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class VoiceMessage(BaseModel):
    """语音消息"""
    type: Literal["record"] = Field("record", description="消息类型，固定为'record' (语音)")
    class Data(BaseModel):
        file: str = Field(..., description="语音文件路径或URL")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class VideoMessage(BaseModel):
    """视频消息"""
    type: Literal["video"] = Field("video", description="消息类型，固定为'video'")
    class Data(BaseModel):
        file: str = Field(..., description="视频文件路径或URL")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

class MarkdownMessage(BaseModel):
    """Markdown消息"""
    type: Literal["record"] = Field("record", description="消息类型，固定为'record' (Markdown)")
    class Data(BaseModel):
        content: str = Field(..., description="Markdown内容")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

# Define the Union for message segments
MessageSegment = (
    TextMessage |
    AtMessage |
    FaceMessage |
    ImageMessage |
    FileMessage |
    ReplyMessage |
    JsonMessage |
    VoiceMessage |
    VideoMessage |
    MarkdownMessage
)

class MessageDetail(BaseModel):
    """消息详情"""
    self_id: float = Field(..., description="机器人自身ID")
    user_id: float = Field(..., description="用户ID")
    time: float = Field(..., description="消息时间戳")
    message_id: float = Field(..., description="消息ID")
    message_seq: float = Field(..., description="消息序列号")
    real_id: float = Field(..., description="真实ID")
    real_seq: str = Field(..., description="真实序列号")
    message_type: str = Field(..., description="消息类型 (e.g., private, group)")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: float = Field(..., description="字体")
    sub_type: str = Field(..., description="子类型")
    message: list[MessageSegment | "ForwardMessage"] = Field(..., description="消息内容列表")
    message_format: str = Field(..., description="消息格式")
    post_type: str = Field(..., description="post_type字段")
    group_id: float | None = Field(None, description="群ID (仅群消息有)")

    model_config = {
        "extra": "allow",
    }

class ForwardMessage(BaseModel):
    """转发消息"""
    type: Literal["forward"] = Field("forward", description="消息类型，固定为'forward'")
    class Data(BaseModel):
        id: str = Field(..., description="转发消息ID")
        content: list[MessageDetail] = Field(..., description="转发内容列表")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="消息数据")
    model_config = {"extra": "allow"}

# region component_models/

# region req
class GetMsgReq(BaseModel):
    """获取消息详情请求模型"""
    message_id: int | str = Field(..., description="消息ID", examples=[123456789, "123456789"])

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetMsgRes(BaseModel):
    """获取消息详情响应模型"""
    status: Literal["ok"] = Field("ok", description="状态码，固定为'ok'")
    retcode: float = Field(0.0, description="返回码")
    data: MessageDetail = Field(..., description="消息详情数据")
    message: str = Field("", description="错误消息")
    wording: str = Field("", description="错误提示")
    echo: str | None = Field(None, description="回显数据")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetMsgAPI(BaseModel):
    """get_msg接口数据模型"""
    endpoint: str = "get_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetMsgReq
    Res: type[BaseModel] = GetMsgRes

# region api/
# endregion code
