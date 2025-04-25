# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/226657396e0
@llms.txt: https://napcat.apifox.cn/226657396e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:发送群合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_forward_msg"
__id__ = "226657396e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req

# Define basic message types
class TextMessageData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextMessage(BaseModel):
    type: Literal['text'] = Field(..., description="消息类型，固定为 text")
    data: TextMessageData = Field(..., description="文本消息数据")

class FaceMessageData(BaseModel):
    id: int = Field(..., description="表情 ID")

class FaceMessage(BaseModel):
    type: Literal['face'] = Field(..., description="消息类型，固定为 face")
    data: FaceMessageData = Field(..., description="表情消息数据")

class ImageMessageData(BaseModel):
    file: str = Field(..., description="图片文件路径或 URL 或 Base64")
    summary: str = Field('[图片]', description="图片消息摘要，通常不需要")

class ImageMessage(BaseModel):
    type: Literal['image'] = Field(..., description="消息类型，固定为 image")
    data: ImageMessageData = Field(..., description="图片消息数据")

class ReplyMessageData(BaseModel):
    id: str | int = Field(..., description="回复消息的 ID")

class ReplyMessage(BaseModel):
    type: Literal['reply'] = Field(..., description="消息类型，固定为 reply")
    data: ReplyMessageData = Field(..., description="回复消息数据")

class JsonMessageData(BaseModel):
    data: str = Field(..., description="JSON 字符串")

class JsonMessage(BaseModel):
    type: Literal['json'] = Field(..., description="消息类型，固定为 json")
    data: JsonMessageData = Field(..., description="JSON 消息数据")

class VideoMessageData(BaseModel):
    file: str = Field(..., description="视频文件路径或 URL 或 Base64")

class VideoMessage(BaseModel):
    type: Literal['video'] = Field(..., description="消息类型，固定为 video")
    data: VideoMessageData = Field(..., description="视频消息数据")

class FileMessageData(BaseModel):
    file: str = Field(..., description="文件路径或 URL 或 Base64")
    name: str = Field(..., description="文件名")

class FileMessage(BaseModel):
    type: Literal['file'] = Field(..., description="消息类型，固定为 file")
    data: FileMessageData = Field(..., description="文件消息数据")

class MarkdownMessageData(BaseModel):
    content: str = Field(..., description="Markdown 内容")

class MarkdownMessage(BaseModel):
    type: Literal['record'] = Field(..., description="消息类型，固定为 record") # Note: OpenAPI says 'record' for Markdown
    data: MarkdownMessageData = Field(..., description="Markdown 消息数据")

# Forward message types (can be nested)
class SendForwardMessageContentData(BaseModel):
    id: str = Field(..., description="转发消息的 res_id")

class SendForwardMessageContent(BaseModel):
    type: Literal['forward'] = Field(..., description="内容类型，固定为 forward")
    data: SendForwardMessageContentData = Field(..., description="转发内容数据")

class SendForwardMessageData(BaseModel):
    user_id: int | str = Field(..., description="用户 ID")
    nickname: str = Field(..., description="用户昵称")
    content: SendForwardMessageContent = Field(..., description="转发消息内容")

class SendForwardMessage(BaseModel):
     type: Literal['node'] = Field(..., description="消息类型，固定为 node")
     data: SendForwardMessageData = Field(..., description="转发消息数据")

# Define the union of all possible message types *within* the content array of a node
AnyInnerMessageType = (
    TextMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage |
    VideoMessage | FileMessage | MarkdownMessage | SendForwardMessage | 'Level2ForwardMessage'
) # Use string forward reference for recursive type

class ForwardNewsItem(BaseModel):
    text: str = Field(..., description="外显内容")

class Level2ForwardMessageData(BaseModel):
    user_id: int | str = Field(..., description="用户 ID")
    nickname: str = Field(..., description="用户昵称")
    content: list[AnyInnerMessageType] = Field(..., description="合并转发消息内容列表")
    news: list[ForwardNewsItem] = Field(..., description="外显新闻列表")
    prompt: str = Field(..., description="外显")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="标题")

class Level2ForwardMessage(BaseModel):
    type: Literal['node'] = Field(..., description="消息类型，固定为 node")
    data: Level2ForwardMessageData = Field(..., description="二级合并转发消息数据")

# Update the union to include the defined Level2ForwardMessage model
AnyInnerMessageType = (
    TextMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage |
    VideoMessage | FileMessage | MarkdownMessage | SendForwardMessage | Level2ForwardMessage
)

# Level 1 Forward Message (the top-level message item in the request list)
class Level1ForwardMessageData(BaseModel):
    user_id: int | str = Field(..., description="用户 ID")
    nickname: str = Field(..., description="用户昵称")
    content: list[AnyInnerMessageType] = Field(..., description="合并转发消息内容列表")

class Level1ForwardMessage(BaseModel):
    type: Literal['node'] = Field(..., description="消息类型，固定为 node")
    data: Level1ForwardMessageData = Field(..., description="一级合并转发消息数据")


class SendGroupForwardMsgReq(BaseModel):
    """
    发送群合并转发消息请求数据
    """
    group_id: int | str = Field(..., description="群号")
    messages: list[Level1ForwardMessage] = Field(..., description="一级合并转发消息列表")
    news: list[ForwardNewsItem] = Field(..., description="外显新闻列表")
    prompt: str = Field(..., description="外显")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="内容") # Note: OpenAPI says "标题" for source in L2, but "内容" in Req. Using "内容" for Req.

# endregion req



# region res
class SendGroupForwardMsgResData(BaseModel):
    message_id: int = Field(..., description="消息 ID")
    res_id: str = Field(..., description="资源 ID")

class SendGroupForwardMsgRes(BaseModel):
    """
    发送群合并转发消息响应数据
    """
    status: Literal['ok'] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: SendGroupForwardMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="Echo") # echo is nullable
# endregion res

# region api
class SendGroupForwardMsgAPI(BaseModel):
    """send_group_forward_msg接口数据模型"""
    endpoint: str = "send_group_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupForwardMsgReq
    Res: type[BaseModel] = SendGroupForwardMsgRes
# endregion api




# endregion code
