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

# Define simple message segments with nested Data classes
class TextMessageSegment(BaseModel):
    type: Literal["text"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        text: str = Field(..., description="文本内容")
    data: Data = Field(..., description="消息段数据")

class AtMessageSegment(BaseModel):
    type: Literal["at"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        qq: str | int | Literal["all"] = Field(..., description="提及的 QQ 号，'all' 表示提及全体成员")
        name: str | None = Field(None, description="对应的 QQ 号或 'all' 的昵称，在群聊中有效")
    data: Data = Field(..., description="消息段数据")

class FaceMessageSegment(BaseModel):
    type: Literal["face"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        id: int = Field(..., description="表情 ID")
    data: Data = Field(..., description="消息段数据")

class ImageMessageSegment(BaseModel):
    type: Literal["image"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        file: str = Field(..., description="图片文件名或 URL")
        summary: str = Field('[图片]', description="图片外显")
    data: Data = Field(..., description="消息段数据")

class FileMessageSegment(BaseModel):
    type: Literal["file"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        file: str = Field(..., description="文件 ID")
        name: str | None = Field(None, description="文件名称")
    data: Data = Field(..., description="消息段数据")

class ReplyMessageSegment(BaseModel):
    type: Literal["reply"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        id: str | int = Field(..., description="回复的消息 ID")
    data: Data = Field(..., description="消息段数据")

class JsonMessageSegment(BaseModel):
    type: Literal["json"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        data: str = Field(..., description="JSON 字符串")
    data: Data = Field(..., description="消息段数据")

class RecordMessageSegment(BaseModel):
    type: Literal["record"] = Field(..., description="消息段类型") # Voice or Markdown
    class Data(BaseModel):
        file: str = Field(..., description="文件文件名或 URL")
    data: Data = Field(..., description="消息段数据")

# Although 'record' with Markdown content is possible, 
# the structure 'type=record, data={content: ...}' differs 
# significantly from 'type=record, data={file: ...}'.
# A better approach is to use separate segment types if possible (e.g., 'voice', 'markdown'),
# but if the API strictly returns type='record' for both, then handling via data structure
# or a more complex union of Data types is needed. Sticking to the original structure for now
# but removing the separate RecordMarkdownMessageSegment class as it shares the 'record' type
# and the distinction should be handled by the Data structure definition if needed.
# Assuming RecordMessageSegment covers the basic 'file' data for audio.

class VideoMessageSegment(BaseModel):
    type: Literal["video"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        file: str = Field(..., description="文件文件名或 URL")
    data: Data = Field(..., description="消息段数据")

# Define the union of all simple message segments
SimpleMessageSegment = (
    TextMessageSegment
    | AtMessageSegment
    | FaceMessageSegment
    | ImageMessageSegment
    | FileMessageSegment
    | ReplyMessageSegment
    | JsonMessageSegment
    | RecordMessageSegment
    | VideoMessageSegment
)

# Define the main response data model, allowing forward reference to ForwardMessageSegment
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
    message_type: Literal["group", "private"] = Field(..., description="消息类型，目前只有 group 或 private") # Use Literal for known types
    class Sender(BaseModel):
        user_id: int = Field(..., description="发送者 QQ 号")
        nickname: str = Field(..., description="昵称")
        sex: Literal["male", "female", "unknown"] | None = Field(None, description="性别，male 或 female 或 unknown")
        age: int | None = Field(None, description="年龄")
        card: str = Field(..., description="群名片／备注")
        role: Literal["owner", "admin", "member"] | None = Field(None, description="角色，owner 或 admin 或 member")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="消息子类型，群聊：normal, anonymous, notice，私聊：friend, group, other") # sub_type might also be literal but schema not precise
    # message field containing list of various message segments, including recursive forward
    message: list[SimpleMessageSegment | 'ForwardMessageSegment'] = Field(..., description="消息内容数组") 
    message_format: Literal["array"] = Field(..., description="消息格式，目前只有 array") # Use Literal
    post_type: Literal["message"] = Field(..., description="上报类型，目前只有 message") # Use Literal
    # Changed group_id to required int based on the original author's comment referencing schema
    group_id: int = Field(..., description="群号 (只有在群聊中有效)")

# Define ForwardMessageSegment with nested Data class referencing GetMsgResData
class ForwardMessageSegment(BaseModel):
    type: Literal["forward"] = Field(..., description="消息段类型")
    class Data(BaseModel):
        id: str = Field(..., description="合并转发消息 ID")
        # Recursively includes list of GetMsgResData
        content: list[GetMsgResData] = Field(..., description="合并转发消息内容列表")
    data: Data = Field(..., description="合并转发消息数据")

# Re-defining the union with ForwardMessageSegment included (optional, but good practice)
# MessageSegmentUnion = Union[SimpleMessageSegment, ForwardMessageSegment]
# The type hint in GetMsgResData already handles the forward reference correctly in Pydantic v2

class GetMsgRes(BaseModel):
    """
    获取消息详情响应参数
    """
    # Unified status field based on rule 2
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
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