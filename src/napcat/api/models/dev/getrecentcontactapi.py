# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659190e0
@llms.txt: https://napcat.apifox.cn/226659190e0.md
@last_update: 2025-04-26 01:17:44

@description: 获取的最新消息是每个会话最新的消息

summary:最近消息列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_recent_contact"
__id__ = "226659190e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Use Literal for const string values

logger = logging.getLogger(__name__)

# region req
class GetRecentContactReq(BaseModel):
    """
    最近消息列表请求模型
    """

    count: int = Field(..., description="会话数量")
# endregion req



# region res

# Define nested message component models first
class TextMessageData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextMessage(BaseModel):
    type: Literal["text"] = Field(..., description="消息类型")
    data: TextMessageData = Field(..., description="消息数据")

class AtMessageData(BaseModel):
    qq: str | int | Literal["all"] = Field(..., description="艾特对象的QQ或all")
    name: str = Field(..., description="艾特对象的名称")

class AtMessage(BaseModel):
    type: Literal["at"] = Field(..., description="消息类型")
    data: AtMessageData = Field(..., description="消息数据")

class FaceMessageData(BaseModel):
    id: int = Field(..., description="表情ID")

class FaceMessage(BaseModel):
    type: Literal["face"] = Field(..., description="消息类型")
    data: FaceMessageData = Field(..., description="消息数据")

class ImageMessageData(BaseModel):
    file: str = Field(..., description="图片文件信息")
    summary: str = Field("[图片]", description="图片消息摘要") # Default value from schema

class ImageMessage(BaseModel):
    type: Literal["image"] = Field(..., description="消息类型")
    data: ImageMessageData = Field(..., description="消息数据")

class FileMessageData(BaseModel):
    file: str = Field(..., description="文件信息")
    name: str | None = Field(None, description="文件名") # Name is not required in schema

class FileMessage(BaseModel):
    type: Literal["file"] = Field(..., description="消息类型")
    data: FileMessageData = Field(..., description="消息数据")

class ReplyMessageData(BaseModel):
    id: str | int = Field(..., description="回复的消息ID")

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field(..., description="消息类型")
    data: ReplyMessageData = Field(..., description="消息数据")

class JsonMessageData(BaseModel):
    data: str = Field(..., description="JSON字符串")

class JsonMessage(BaseModel):
    type: Literal["json"] = Field(..., description="消息类型")
    data: JsonMessageData = Field(..., description="消息数据")

class VoiceMessageData(BaseModel):
    file: str = Field(..., description="语音文件信息")

class VoiceMessage(BaseModel):
    type: Literal["record"] = Field(..., description="消息类型") # Schema uses 'record' for voice
    data: VoiceMessageData = Field(..., description="消息数据")

class VideoMessageData(BaseModel):
    file: str = Field(..., description="视频文件信息")

class VideoMessage(BaseModel):
    type: Literal["video"] = Field(..., description="消息类型")
    data: VideoMessageData = Field(..., description="消息数据")

class MarkdownMessageData(BaseModel):
    content: str = Field(..., description="Markdown内容")

class MarkdownMessage(BaseModel):
    type: Literal["record"] = Field(..., description="消息类型") # Schema uses 'record' for markdown
    data: MarkdownMessageData = Field(..., description="消息数据")

# Forward message references 消息详情, which needs to be defined or referenced carefully.
# Based on the ref, 'content' is an array of 消息详情. Let's define 消息详情 as a generic type for now.
class MessageDetail(BaseModel):
    # This model is simplified based on the structure implied by the forward message ref.
    # The full 消息详情 schema is complex, but the 'forward' message seems to reference its content.
    # We'll define a placeholder or a partial structure if the full schema is not needed here.
    # Given the complexity and potential recursion, let's check the forward message definition.
    # The forward message definition shows 'content' is an array of 消息详情.
    # The '消息详情' schema includes 'message' which is an array of message components.
    # This can lead to recursive definitions.
    # Let's define a basic MessageDetail structure based on its properties in the OpenAPI.
    self_id: int = Field(..., description="自身账号")
    user_id: int = Field(..., description="消息发送者")
    time: int = Field(..., description="消息时间戳")
    message_id: int = Field(..., description="消息ID")
    message_seq: int = Field(..., description="消息序列号")
    real_id: int = Field(..., description="真实消息ID")
    real_seq: str = Field(..., description="真实消息序列号")
    message_type: str = Field(..., description="消息类型 (private/group)")
    sender: "Sender" = Field(..., description="发送者信息") # Forward reference to Sender
    raw_message: str = Field(..., description="原始消息内容")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="子类型")
    message: list[ "MessageComponent" ] = Field(..., description="消息内容列表") # Forward reference
    message_format: str = Field(..., description="消息格式")
    post_type: str = Field(..., description="上报类型")
    group_id: int | None = Field(None, description="群号 (私聊消息可能没有)")
    # Note: The schema for 'lastestMsg' in the response ignores some fields from '消息详情'.
    # We are defining MessageDetail based on the 'components/schemas/消息详情' ref.

class ForwardMessageData(BaseModel):
    id: str = Field(..., description="转发消息ID")
    content: list[MessageDetail] = Field(..., description="转发消息内容列表")

class ForwardMessage(BaseModel):
    type: Literal["forward"] = Field(..., description="消息类型")
    data: ForwardMessageData = Field(..., description="消息数据")

# Define the Union of all message components
MessageComponent = (TextMessage | AtMessage | FaceMessage | ImageMessage | FileMessage | ReplyMessage | JsonMessage | VoiceMessage | VideoMessage | MarkdownMessage | ForwardMessage)

# Update forward reference for MessageDetail
MessageDetail.model_rebuild()

class Sender(BaseModel):
    user_id: int = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    sex: Literal["male", "female", "unknown"] | None = Field(None, description="性别")
    age: int | None = Field(None, description="年龄")
    card: str | None = Field(None, description="群名片")
    role: Literal["owner", "admin", "member"] | None = Field(None, description="群成员角色")

# The 'lastestMsg' in the response has a simplified structure compared to the full '消息详情'.
# We will model 'lastestMsg' based on its specific properties listed in the response schema.
# It includes the same required fields as '消息详情' but also has its own ignore list, which is confusing.
# Let's stick to the properties listed *within* the 'lastestMsg' definition in the response.
class LastestMessage(BaseModel):
    """最新消息内容"""
    self_id: int = Field(..., description="自身账号")
    user_id: int = Field(..., description="消息发送者")
    time: int = Field(..., description="消息时间戳")
    real_seq: str = Field(..., description="真实消息序列号")
    message_type: str = Field(..., description="消息类型 (private/group)")
    sender: Sender = Field(..., description="发送者信息")
    raw_message: str = Field(..., description="原始消息内容")
    font: int = Field(..., description="字体")
    sub_type: str = Field(..., description="子类型")
    message: list[MessageComponent] = Field(..., description="消息内容列表")
    message_format: str = Field(..., description="消息格式")
    post_type: str = Field(..., description="上报类型")
    group_id: int | None = Field(None, description="群号 (私聊消息可能没有)") # Group ID is not marked required in the response schema, but is in 消息详情.

class RecentContactItem(BaseModel):
    """最近联系人列表项"""
    lastestMsg: LastestMessage = Field(..., description="最新消息内容")
    peerUin: str = Field(..., description="对方账号")
    remark: str = Field(..., description="备注")
    msgTime: str = Field(..., description="消息时间")
    chatType: int = Field(..., description="会话类型")
    msgId: str = Field(..., description="消息ID")
    sendNickName: str = Field(..., description="发送人昵称")
    sendMemberName: str = Field(..., description="发送人成员名")
    peerName: str = Field(..., description="对方昵称")

class GetRecentContactRes(BaseModel):
    """
    最近消息列表响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[RecentContactItem] = Field(..., description="最近联系人列表数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")


# endregion res

# region api
class GetRecentContactAPI(BaseModel):
    """get_recent_contact接口数据模型"""
    endpoint: str = "get_recent_contact"
    method: str = "POST"
    Req: type[BaseModel] = GetRecentContactReq
    Res: type[BaseModel] = GetRecentContactRes
# endregion api




# endregion code
