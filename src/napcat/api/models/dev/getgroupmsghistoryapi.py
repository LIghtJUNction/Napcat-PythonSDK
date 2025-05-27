# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657401e0
@llms.txt: https://napcat.apifox.cn/226657401e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_msg_history"
__id__ = "226657401e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal
from __future__ import annotations # For forward references in message content

# region component_models

class Sender(BaseModel):
    """sender字段"""
    user_id: float = Field(..., description="user_id字段")
    nickname: str = Field(..., description="nickname字段")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="sex字段")
    age: float | None = Field(None, description="age字段")
    card: str = Field(..., description="card字段")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="role字段")

    model_config = {
        "extra": "allow",
    }

class TextMessage(BaseModel):
    """文本消息"""
    type: Literal["text"] = Field("text", description="type字段")
    class Data(BaseModel):
        text: str = Field(..., description="文本内容")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class AtMessage(BaseModel):
    """艾特消息"""
    type: Literal["at"] = Field("at", description="type字段")
    class Data(BaseModel):
        qq: int | str | Literal["all"] = Field(..., description="艾特的QQ号，或 'all' 表示艾特全体成员")
        name: str | None = Field(None, description="艾特的名称")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class FaceMessage(BaseModel):
    """表情消息"""
    type: Literal["face"] = Field("face", description="type字段")
    class Data(BaseModel):
        id: float = Field(..., description="表情ID")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class ImageMessage(BaseModel):
    """图片消息"""
    type: Literal["image"] = Field("image", description="type字段")
    class Data(BaseModel):
        file: str = Field(..., description="文件ID")
        summary: str = Field("[图片]", description="外显")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class FileMessage(BaseModel):
    """文件消息"""
    type: Literal["file"] = Field("file", description="type字段")
    class Data(BaseModel):
        file: str = Field(..., description="文件ID")
        name: str | None = Field(None, description="文件名称")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class ReplyMessage(BaseModel):
    """回复消息"""
    type: Literal["reply"] = Field("reply", description="type字段")
    class Data(BaseModel):
        id: int | str = Field(..., description="回复的消息ID")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class JSONMessage(BaseModel):
    """JSON消息"""
    type: Literal["json"] = Field("json", description="type字段")
    class Data(BaseModel):
        data: str = Field(..., description="JSON字符串数据")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class VoiceMessage(BaseModel):
    """语音消息"""
    type: Literal["record"] = Field("record", description="type字段")
    class Data(BaseModel):
        file: str = Field(..., description="文件ID")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class VideoMessage(BaseModel):
    """视频消息"""
    type: Literal["video"] = Field("video", description="type字段")
    class Data(BaseModel):
        file: str = Field(..., description="文件ID")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class MarkdownMessage(BaseModel):
    """Markdown消息"""
    type: Literal["record"] = Field("record", description="type字段")
    class Data(BaseModel):
        content: str = Field(..., description="Markdown内容")
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

# Define the union type for message content, using string literals for forward references
MessageContent = TextMessage | AtMessage | FaceMessage | ImageMessage | FileMessage | ReplyMessage | JSONMessage | VoiceMessage | VideoMessage | MarkdownMessage | "ForwardMessage"

class ForwardMessage(BaseModel):
    """消息forward (合并转发)"""
    type: Literal["forward"] = Field("forward", description="type字段")
    class Data(BaseModel):
        id: str = Field(..., description="合并转发ID")
        content: list[MessageContent] = Field(..., description="合并转发的消息列表") # This will refer to the global MessageContent
        model_config = {"extra": "allow"}
    data: Data = Field(..., description="data字段")

    model_config = {
        "extra": "allow",
    }

class MessageDetail(BaseModel):
    """消息详情"""
    self_id: float = Field(..., description="self_id字段")
    user_id: float = Field(..., description="user_id字段")
    time: float = Field(..., description="time字段")
    message_id: float = Field(..., description="message_id字段")
    message_seq: float = Field(..., description="message_seq字段")
    real_id: float = Field(..., description="real_id字段")
    real_seq: str = Field(..., description="real_seq字段")
    message_type: str = Field(..., description="message_type字段")
    sender: Sender = Field(..., description="sender字段")
    raw_message: str = Field(..., description="raw_message字段")
    font: float = Field(..., description="font字段")
    sub_type: str = Field(..., description="sub_type字段")
    message: list[MessageContent] = Field(..., description="message字段") # Use the union type here
    message_format: str = Field(..., description="message_format字段")
    post_type: str = Field(..., description="post_type字段")
    group_id: float | None = Field(None, description="group_id字段")

    model_config = {
        "extra": "allow",
    }

# endregion component_models/

# region req
class GetGroupMsgHistoryReq(BaseModel):
    """获取群历史消息"""
    group_id: int | str = Field(..., description="群ID")
    message_seq: int | str | None = Field(None, description="起始消息序列号，0为最新")
    count: int = Field(20, description="获取消息的数量")
    reverseOrder: bool = Field(False, description="是否倒序获取消息")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupMsgHistoryRes(BaseModel):
    """获取群历史消息"""
    class Data(BaseModel):
        """响应数据类型"""
        messages: list[MessageDetail] = Field(..., description="消息列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(..., description="retcode字段")
    data: Data = Field(..., description="data字段")
    message: str = Field(..., description="message字段")
    wording: str = Field(..., description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupMsgHistoryAPI(BaseModel):
    """get_group_msg_history接口数据模型"""
    endpoint: str = "get_group_msg_history"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupMsgHistoryReq
    Res: type[BaseModel] = GetGroupMsgHistoryRes

# region api/
# endregion code
