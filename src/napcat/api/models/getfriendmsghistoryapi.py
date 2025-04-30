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
from typing import Any, Literal


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
class TextMessage(BaseModel):
    """文本消息段"""
    class Data(BaseModel):
        text: str = Field(..., description="文本内容")

    type: Literal["text"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class AtMessage(BaseModel):
    """@消息段"""
    class Data(BaseModel):
        qq: int | str = Field(..., description="被@的QQ号, 或 'all'")
        name: str | None = Field(None, description="被@的群名片/昵称 (仅限群聊)")

    type: Literal["at"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class FaceMessage(BaseModel):
    """表情消息段"""
    class Data(BaseModel):
        id: int = Field(..., description="表情ID")

    type: Literal["face"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class ImageMessage(BaseModel):
    """图片消息段"""
    class Data(BaseModel):
        file: str = Field(..., description="图片文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI
        summary: str = Field("[图片]", description="外显文字")

    type: Literal["image"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class FileMessage(BaseModel):
    """文件消息段"""
    class Data(BaseModel):
        file: str = Field(..., description="文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI
        name: str = Field(..., description="文件名")

    type: Literal["file"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class ReplyMessage(BaseModel):
    """回复消息段"""
    class Data(BaseModel):
        id: int | str = Field(..., description="回复的消息ID或序列号")

    type: Literal["reply"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class JsonMessage(BaseModel):
    """JSON/App消息段"""
    class Data(BaseModel):
        data: str = Field(..., description="JSON字符串")

    type: Literal["json", "app"] = Field(..., description="消息段类型") # Added 'app' based on common usage/OpenAPI notes
    data: Data = Field(..., description="消息段数据")

class VoiceMessage(BaseModel):
    """语音消息段"""
    class Data(BaseModel):
        file: str = Field(..., description="语音文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI

    type: Literal["record", "voice"] = Field(..., description="消息段类型") # Added 'voice' based on common usage
    data: Data = Field(..., description="消息段数据")

class VideoMessage(BaseModel):
    """视频消息段"""
    class Data(BaseModel):
        file: str = Field(..., description="视频文件信息") # Note: file field can be complex, simplifying to str based on OpenAPI

    type: Literal["video"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class MarkdownMessage(BaseModel):
    """Markdown消息段"""
    class Data(BaseModel):
        content: str = Field(..., description="Markdown内容")

    type: Literal["markdown"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")

class ForwardMessage(BaseModel):
    """合并转发消息段"""
    class Data(BaseModel):
        id: str = Field(..., description="转发消息ID")
        # 使用更具体的类型而不是通用 dict，避免使用无类型参数的泛型
        # 由于转发消息内容实际上是简化的消息段，我们使用 str 作为键，任何值作为值
        content: list[dict[str, str | int | bool | list[Any] | None]] = Field(
            ..., description="转发消息内容列表 (简略格式)"
        )

    type: Literal["forward"] = Field(..., description="消息段类型")
    data: Data = Field(..., description="消息段数据")


type MessageSegment = TextMessage | AtMessage | FaceMessage | ImageMessage | FileMessage | ReplyMessage | JsonMessage | VoiceMessage | VideoMessage | MarkdownMessage | ForwardMessage

# --- Sender Model ---
class Sender(BaseModel):
    """发送者信息模型"""
    user_id: int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="性别")
    age: int | None = Field(None, description="年龄")
    card: str | None = Field(None, description="群名片 (仅限群聊)") # Added None as it's only for group
    role: Literal["owner", "admin", "member"] | None = Field(None, description="角色 (仅限群聊)")

# --- Message Detail Model ---
class MessageDetail(BaseModel):
    """消息详情模型"""
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
    group_id: int | None = Field(None, description="群ID (仅限群聊)") # Made optional as it's only for group


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
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: GetFriendMsgHistoryResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词")
    echo: str | None = Field(None, description="回显数据")

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