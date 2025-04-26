# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['消息相关']
@homepage: https://napcat.apifox.cn/226657401e0
@llms.txt: https://napcat.apifox.cn/226657401e0.md
@last_update: 2025-04-27 00:53:40

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
from pydantic import BaseModel, Field, Literal
from typing import list, str, int, bool, Any # Using built-in lowercase types as per instructions


# region req
class GetGroupMsgHistoryReq(BaseModel):
    """
    获取群历史消息请求模型
    """
    group_id: int | str = Field(..., description="群号")
    message_seq: int | str | None = Field(default=None, description="起始消息序号，0为最新")
    count: int = Field(default=20, description="获取数量")
    reverseOrder: bool = Field(default=True, description="是否倒序获取")
# endregion req



# region res

# --- Nested Message Content Data Models ---
class MessageTypeTextData(BaseModel):
    text: str = Field(..., description="文本内容")

class MessageTypeAtData(BaseModel):
    qq: int | str = Field(..., description="@的QQ号，all为全体成员")
    name: str | None = Field(default=None, description="@的昵称")

class MessageTypeFaceData(BaseModel):
    id: int = Field(..., description="表情ID")

class MessageTypeImageData(BaseModel):
    file: str = Field(..., description="图片文件名")
    summary: str = Field(default='[图片]', description="外显内容")

class MessageTypeFileData(BaseModel):
    file: str = Field(..., description="文件ID或文件名")
    name: str = Field(..., description="文件名")

class MessageTypeReplyData(BaseModel):
    id: int | str = Field(..., description="回复的消息ID")

class MessageTypeJsonData(BaseModel):
    data: str = Field(..., description="JSON字符串") # Note: Field named 'data' inside 'data'

class MessageTypeRecordDataVoice(BaseModel):
    file: str = Field(..., description="语音文件名")

class MessageTypeRecordDataMarkdown(BaseModel):
     content: str = Field(..., description="Markdown文本内容")

class MessageTypeVideoData(BaseModel):
    file: str = Field(..., description="视频文件名")


# --- Recursive Forward Message Data Model ---
class MessageTypeForwardData(BaseModel):
    id: str = Field(..., description="转发消息ID")
    content: list["MessageDetail"] = Field(..., description="转发消息内容列表")


# --- Nested Message Content Models (with type discriminator) ---
# Note: 'record' type is used for both Voice and Markdown in spec, handled by Pydantic's union parsing
class MessageTypeText(BaseModel):
    type: Literal["text"] = "text"
    data: MessageTypeTextData = Field(...)

class MessageTypeAt(BaseModel):
    type: Literal["at"] = "at"
    data: MessageTypeAtData = Field(...)

class MessageTypeFace(BaseModel):
    type: Literal["face"] = "face"
    data: MessageTypeFaceData = Field(...)

class MessageTypeImage(BaseModel):
    type: Literal["image"] = "image"
    data: MessageTypeImageData = Field(...)

class MessageTypeFile(BaseModel):
    type: Literal["file"] = "file"
    data: MessageTypeFileData = Field(...)

class MessageTypeReply(BaseModel):
    type: Literal["reply"] = "reply"
    data: MessageTypeReplyData = Field(...)

class MessageTypeJson(BaseModel):
    type: Literal["json"] = "json"
    data: MessageTypeJsonData = Field(...)

class MessageTypeVoice(BaseModel):
    type: Literal["record"] = "record"
    data: MessageTypeRecordDataVoice = Field(...)

class MessageTypeMarkdown(BaseModel):
    type: Literal["record"] = "record"
    data: MessageTypeRecordDataMarkdown = Field(...)

class MessageTypeVideo(BaseModel):
    type: Literal["video"] = "video"
    data: MessageTypeVideoData = Field(...)

class MessageTypeForward(BaseModel):
    type: Literal["forward"] = "forward"
    data: MessageTypeForwardData = Field(...)


# --- Message Content Union Type ---
MessageContent = (MessageTypeText | MessageTypeAt | MessageTypeFace | MessageTypeImage |
                  MessageTypeFile | MessageTypeReply | MessageTypeJson | MessageTypeVoice |
                  MessageTypeMarkdown | MessageTypeVideo | MessageTypeForward)


# --- Nested Sender Model ---
class Sender(BaseModel):
    user_id: int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    sex: Literal["male", "female", "unknown"] | None = Field(default=None, description="性别")
    age: int | None = Field(default=None, description="年龄")
    card: str = Field(..., description="群名片")
    role: Literal["owner", "admin", "member"] | None = Field(default=None, description="角色")


# --- Recursive Message Detail Model ---
class MessageDetail(BaseModel):
    self_id: int = Field(..., description="机器人账号")
    user_id: int = Field(..., description="发送者账号")
    time: int = Field(..., description="时间戳")
    message_id: int = Field(..., description="消息ID")
    message_seq: int = Field(..., description="消息序列号")
    real_id: int = Field(..., description="实时ID")
    real_seq: str = Field(..., description="实时序列号")
    message_type: str = Field(..., description="消息类型 (e.g., group, private)")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息字符串")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="消息子类型")
    message: list[MessageContent] = Field(..., description="消息内容列表")
    message_format: str = Field(..., description="消息格式")
    post_type: str = Field(..., description="POST类型")
    group_id: int | None = Field(default=None, description="群ID (仅群聊)")

# --- Nested Response Data Model ---
class GetGroupMsgHistoryResData(BaseModel):
    messages: list[MessageDetail] = Field(..., description="历史消息列表")


# --- Main Response Model ---
class GetGroupMsgHistoryRes(BaseModel):
    """
    获取群历史消息响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: GetGroupMsgHistoryResData = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="wording")
    echo: str | None = Field(..., description="echo")

# --- Model Rebuild for Recursion ---
# These classes are mutually recursive via MessageContent and MessageTypeForwardData
MessageDetail.model_rebuild()
MessageTypeForwardData.model_rebuild()

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
