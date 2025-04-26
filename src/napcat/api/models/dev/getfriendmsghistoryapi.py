# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659174e0
@llms.txt: https://napcat.apifox.cn/226659174e0.md
@last_update: 2025-04-27 00:53:40

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
from typing import list, Literal


# region req
class GetFriendMsgHistoryReq(BaseModel):
    """
    获取好友历史消息 请求模型
    """
    user_id: int | str = Field(..., description="用户ID")
    message_seq: int | str = Field(0, description="0为最新，消息序列号")
    count: int = Field(20, description="数量")
    reverseOrder: bool = Field(False, description="是否倒序")

# endregion req


# region models
# --- Message Segment Models ---
class TextMessageData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextMessage(BaseModel):
    type: Literal["text"] = Field(..., description="消息段类型")
    data: TextMessageData = Field(..., description="消息段数据")

class AtMessageData(BaseModel):
    qq: int | str = Field(..., description="被@的QQ号, 或 'all'")
    name: str | None = Field(None, description="被@的群名片/昵称 (仅限群聊)")

class AtMessage(BaseModel):
    type: Literal["at"] = Field(..., description="消息段类型")
    data: AtMessageData = Field(..., description="消息段数据")

class FaceMessageData(BaseModel):
    id: int = Field(..., description="表情ID")

class FaceMessage(BaseModel):
    type: Literal["face"] = Field(..., description="消息段类型")
    data: FaceMessageData = Field(..., description="消息段数据")

class ImageMessageData(BaseModel):
    file: str = Field(..., description="图片文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI
    summary: str = Field("[图片]", description="外显文字")

class ImageMessage(BaseModel):
    type: Literal["image"] = Field(..., description="消息段类型")
    data: ImageMessageData = Field(..., description="消息段数据")

class FileMessageData(BaseModel):
    file: str = Field(..., description="文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI
    name: str = Field(..., description="文件名")

class FileMessage(BaseModel):
    type: Literal["file"] = Field(..., description="消息段类型")
    data: FileMessageData = Field(..., description="消息段数据")

class ReplyMessageData(BaseModel):
    id: int | str = Field(..., description="回复的消息ID或序列号")

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field(..., description="消息段类型")
    data: ReplyMessageData = Field(..., description="消息段数据")

class JsonMessageData(BaseModel):
    data: str = Field(..., description="JSON字符串")

class JsonMessage(BaseModel):
    type: Literal["json"] = Field(..., description="消息段类型") # Note: OpenAPI has type as 'json' but also 'app' - using 'json' based on schema name
    data: JsonMessageData = Field(..., description="消息段数据")

class VoiceMessageData(BaseModel):
    file: str = Field(..., description="语音文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI

class VoiceMessage(BaseModel):
    type: Literal["record"] = Field(..., description="消息段类型") # Note: OpenAPI has type as 'record'
    data: VoiceMessageData = Field(..., description="消息段数据")

class VideoMessageData(BaseModel):
    file: str = Field(..., description="视频文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI

class VideoMessage(BaseModel):
    type: Literal["video"] = Field(..., description="消息段类型")
    data: VideoMessageData = Field(..., description="消息段数据")

class MarkdownMessageData(BaseModel):
    content: str = Field(..., description="Markdown内容")

class MarkdownMessage(BaseModel):
    type: Literal["markdown"] = Field(..., description="消息段类型") # Note: OpenAPI has type as 'record' but implies markdown - using 'markdown'
    data: MarkdownMessageData = Field(..., description="消息段数据")

class ForwardMessageData(BaseModel):
    id: str = Field(..., description="转发消息ID")
    # Note: OpenAPI content schema reference points back to MessageDetail array, creating a potential circular dependency.
    # Assuming a simplified representation or need for manual handling.
    # For now, using a placeholder or a simplified type.
    content: list[dict | TextMessage] = Field(..., description="转发消息内容列表") # Using dict as a placeholder for complex recursive message structure

class ForwardMessage(BaseModel):
    type: Literal["forward"] = Field(..., description="消息段类型")
    data: ForwardMessageData = Field(..., description="消息段数据")

# Union of all message segment types
MessageSegment = (TextMessage | AtMessage | FaceMessage | ImageMessage |
                  FileMessage | ReplyMessage | JsonMessage | VoiceMessage |
                  VideoMessage | MarkdownMessage | ForwardMessage)

# --- Sender Model ---
class Sender(BaseModel):
    user_id: int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="性别")
    age: int | None = Field(None, description="年龄")
    card: str = Field(..., description="群名片 (仅限群聊)")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="角色 (仅限群聊)")

# --- Message Detail Model ---
class MessageDetail(BaseModel):
    self_id: int = Field(..., description="自身QQ号")
    user_id: int = Field(..., description="发送者用户ID")
    time: int = Field(..., description="消息发送时间戳")
    message_id: int = Field(..., description="消息ID")
    message_seq: int = Field(..., description="消息序列号")
    real_id: int = Field(..., description="实际消息ID (可能用于回复)")
    real_seq: str = Field(..., description="实际消息序列号") # OpenAPI says string
    message_type: str = Field(..., description="消息类型 (e.g., 'private', 'group')")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="消息子类型")
    message: list[MessageSegment] = Field(..., description="消息段列表")
    message_format: str = Field(..., description="消息格式 (e.g., 'string', 'array')")
    post_type: str = Field(..., description="POST类型 (e.g., 'message')")
    group_id: int | None = Field(None, description="群ID (仅限群聊)")


# region res
class GetFriendMsgHistoryResData(BaseModel):
    """
    获取好友历史消息 响应数据模型
    """
    messages: list[MessageDetail] = Field(..., description="历史消息列表")


class GetFriendMsgHistoryRes(BaseModel):
    """
    获取好友历史消息 响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: GetFriendMsgHistoryResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词")
    echo: str | None = Field(..., description="回显数据，可能为null")

# endregion res

# region api
class GetFriendMsgHistoryAPI(BaseModel):
    """get_friend_msg_history接口数据模型"""
    endpoint: str = "get_friend_msg_history"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendMsgHistoryReq
    Res: type[BaseModel] = GetFriendMsgHistoryRes
# endregion api

# endregion code
