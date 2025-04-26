# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['消息相关']
@homepage: https://napcat.apifox.cn/226656707e0
@llms.txt: https://napcat.apifox.cn/226656707e0.md
@last_update: 2025-04-27 00:53:40

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

# region req
class GetMsgReq(BaseModel):
    """
    获取消息详情请求参数
    """
    message_id: int | str = Field(..., description="消息 ID")
# endregion req

# region res

class TextMessageSegmentData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextMessageSegment(BaseModel):
    type: Literal["text"] = Field(..., description="消息段类型")
    data: TextMessageSegmentData = Field(..., description="消息段数据")

class AtMessageSegmentData(BaseModel):
    qq: str | int | Literal["all"] = Field(..., description="提及的 QQ 号，'all' 表示提及全体成员")
    name: str | None = Field(None, description="对应的 QQ 号或 'all' 的昵称，在群聊中有效")

class AtMessageSegment(BaseModel):
    type: Literal["at"] = Field(..., description="消息段类型")
    data: AtMessageSegmentData = Field(..., description="消息段数据")

class FaceMessageSegmentData(BaseModel):
    id: int = Field(..., description="表情 ID")

class FaceMessageSegment(BaseModel):
    type: Literal["face"] = Field(..., description="消息段类型")
    data: FaceMessageSegmentData = Field(..., description="消息段数据")

class ImageMessageSegmentData(BaseModel):
    file: str = Field(..., description="图片文件名或 URL")
    summary: str = Field('[图片]', description="图片外显")

class ImageMessageSegment(BaseModel):
    type: Literal["image"] = Field(..., description="消息段类型")
    data: ImageMessageSegmentData = Field(..., description="消息段数据")

class FileMessageSegmentData(BaseModel):
    file: str = Field(..., description="文件 ID")
    name: str | None = Field(None, description="文件名称")

class FileMessageSegment(BaseModel):
    type: Literal["file"] = Field(..., description="消息段类型")
    data: FileMessageSegmentData = Field(..., description="消息段数据")

class ReplyMessageSegmentData(BaseModel):
    id: str | int = Field(..., description="回复的消息 ID")

class ReplyMessageSegment(BaseModel):
    type: Literal["reply"] = Field(..., description="消息段类型")
    data: ReplyMessageSegmentData = Field(..., description="消息段数据")

class JsonMessageSegmentData(BaseModel):
    data: str = Field(..., description="JSON 字符串")

class JsonMessageSegment(BaseModel):
    type: Literal["json"] = Field(..., description="消息段类型")
    data: JsonMessageSegmentData = Field(..., description="消息段数据")

class RecordMessageSegmentData(BaseModel):
    file: str = Field(..., description="文件文件名或 URL")

class RecordMessageSegment(BaseModel):
    type: Literal["record"] = Field(..., description="消息段类型") # Voice
    data: RecordMessageSegmentData = Field(..., description="消息段数据")

class RecordMarkdownMessageSegmentData(BaseModel):
    content: str = Field(..., description="Markdown 内容")

# Note: This message type also uses type='record', differentiating via data structure.
class RecordMarkdownMessageSegment(BaseModel):
    type: Literal["record"] = Field(..., description="消息段类型") # Markdown
    data: RecordMarkdownMessageSegmentData = Field(..., description="消息段数据")

class VideoMessageSegmentData(BaseModel):
    file: str = Field(..., description="文件文件名或 URL")

class VideoMessageSegment(BaseModel):
    type: Literal["video"] = Field(..., description="消息段类型")
    data: VideoMessageSegmentData = Field(..., description="消息段数据")

# Define a union of all possible message segments
MessageSegment = (
    TextMessageSegment
    | AtMessageSegment
    | FaceMessageSegment
    | ImageMessageSegment
    | FileMessageSegment
    | ReplyMessageSegment
    | JsonMessageSegment
    | RecordMessageSegment # Voice
    | RecordMarkdownMessageSegment # Markdown
    | VideoMessageSegment
    # ForwardMessageSegment contains a list of GetMsgResData, creating recursion.
    # It needs to be defined AFTER GetMsgResData is defined, or use forward referencing.
    # Let's define GetMsgResData first, then ForwardMessageSegment.
)


class Sender(BaseModel):
    user_id: int = Field(..., description="发送者 QQ 号")
    nickname: str = Field(..., description="昵称")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="性别，male 或 female 或 unknown") # sex not required in schema
    age: int | None = Field(None, description="年龄") # age not required in schema
    card: str = Field(..., description="群名片／备注")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="角色，owner 或 admin 或 member") # role not required in schema


class GetMsgResData(BaseModel):
    """
    消息详情数据模型
    """
    self_id: int = Field(..., description="机器人 QQ 号")
    user_id: int = Field(..., description="消息发送者 QQ 号")
    time: int = Field(..., description="消息发送时间 (时间戳)")
    message_id: int = Field(..., description="消息 ID")
    message_seq: int = Field(..., description="消息序列号")
    real_id: int = Field(..., description="消息真实 ID")
    real_seq: str = Field(..., description="消息真实序列号 (字符串类型)") # Schema says string
    message_type: str = Field(..., description="消息类型，目前只有 group 或 private")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="消息子类型，群聊：normal, anonymous, notice，私聊：friend, group, other")
    # message field containing list of various message segments
    message: list[MessageSegment | 'ForwardMessageSegment'] = Field(..., description="消息内容数组") # Add ForwardSegment recursively
    message_format: str = Field(..., description="消息格式，目前只有 array")
    post_type: str = Field(..., description="上报类型，目前只有 message")
    group_id: int | None = Field(None, description="群号 (只有在群聊中有效)") # Schema required, but logically optional for private msg? Follow schema required.
    # Update: Schema says group_id is required. Will make it required.
    #group_id: int = Field(..., description="群号 (只有在群聊中有效)")


class ForwardMessageSegmentData(BaseModel):
    id: str = Field(..., description="合并转发消息 ID")
    # Recursively includes list of message detail objects
    content: list[GetMsgResData] = Field(..., description="合并转发消息内容列表")

# Define ForwardMessageSegment after GetMsgResData
class ForwardMessageSegment(BaseModel):
    type: Literal["forward"] = Field(..., description="消息段类型")
    data: ForwardMessageSegmentData = Field(..., description="消息段数据")

# Update the MessageSegment type alias to include ForwardMessageSegment
MessageSegmentUnion = (
    TextMessageSegment
    | AtMessageSegment
    | FaceMessageSegment
    | ImageMessageSegment
    | FileMessageSegment
    | ReplyMessageSegment
    | JsonMessageSegment
    | RecordMessageSegment
    | RecordMarkdownMessageSegment
    | VideoMessageSegment
    | ForwardMessageSegment # Now included
)

# Re-define GetMsgResData to use the final Union type
# This is verbose, but ensures type hints are correct after recursion is handled.
# Alternatively, Pydantic v2 handles forward refs ('ForwardMessageSegment') directly in the list type hint.
# So the initial definition of GetMsgResData with list[MessageSegment | 'ForwardMessageSegment'] should work.

class GetMsgRes(BaseModel):
    """
    获取消息详情响应参数
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: GetMsgResData = Field(..., description="消息详情数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo")

# endregion res

# region api
class GetMsgAPI(BaseModel):
    """get_msg接口数据模型"""
    endpoint: str = "get_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetMsgReq
    Res: type[BaseModel] = GetMsgRes
# endregion api


# endregion code
