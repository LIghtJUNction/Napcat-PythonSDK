# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659136e0
@llms.txt: https://napcat.apifox.cn/226659136e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:发送合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_forward_msg"
__id__ = "226659136e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal, Union

# region req

# Simple Message Data Models
class TextMessageData(BaseModel):
    text: str = Field(..., description="文本内容")

class FaceMessageData(BaseModel):
    id: int = Field(..., description="表情ID")

class ImageMessageData(BaseModel):
    file: str = Field(..., description="图片文件名")
    summary: str = Field('[图片]', description="外显")

class ReplyMessageData(BaseModel):
    id: str | int = Field(..., description="被回复消息ID")

class JsonMessageData(BaseModel):
    data: str = Field(..., description="JSON字符串")

class VideoMessageData(BaseModel):
    file: str = Field(..., description="视频文件名")

class FileMessageData(BaseModel):
    file: str = Field(..., description="文件文件名")
    name: str = Field(..., description="文件名称")

class MarkdownMessageData(BaseModel):
    content: str = Field(..., description="Markdown内容")

# Simple Message Component Models (wrappers)
class TextMessage(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型：文本")
    data: TextMessageData

class FaceMessage(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型：表情")
    data: FaceMessageData

class ImageMessage(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型：图片")
    data: ImageMessageData

class ReplyMessage(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型：回复")
    data: ReplyMessageData

class JsonMessage(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型：JSON")
    data: JsonMessageData

class VideoMessage(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型：视频")
    data: VideoMessageData

class FileMessage(BaseModel):
    type: Literal["file"] = Field("file", description="消息类型：文件")
    data: FileMessageData

class MarkdownMessage(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型：Markdown (OpenAPI spec indicates 'record')")
    data: MarkdownMessageData

# News Item Model
class NewsItem(BaseModel):
    text: str = Field(..., description="新闻内容文本")

# Forward Message Component Models
class ForwardContentData(BaseModel):
    id: str = Field(..., description="res_id")

class ForwardContent(BaseModel):
    type: Literal["forward"] = Field("forward", description="消息类型：转发内部内容")
    data: ForwardContentData

class ForwardWrapperData(BaseModel):
    user_id: str | int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    content: ForwardContent

class ForwardWrapper(BaseModel):
    type: Literal["node"] = Field("node", description="消息类型：转发节点 (OpenAPI spec indicates 'node')")
    data: ForwardWrapperData

# Declare the Union components list for forward reference
MessageComponentTypes = (
    TextMessage,
    FaceMessage,
    ImageMessage,
    ReplyMessage,
    JsonMessage,
    VideoMessage,
    FileMessage,
    MarkdownMessage,
    ForwardWrapper,
    # SecondLevelForwardMessage will be added below
)

# Second Level Forward Message Models (requires NewsItem and the Union)
class SecondLevelForwardData(BaseModel):
    user_id: str | int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    # Use string annotation for recursive type
    content: list['AnyOfMessageComponent'] = Field(..., description="构建")
    news: list[NewsItem] | None = Field(None, description="外显新闻列表")
    prompt: str | None = Field(None, description="外显文本")
    summary: str | None = Field(None, description="底下文本")
    source: str | None = Field(None, description="内容来源")

class SecondLevelForwardMessage(BaseModel):
    type: Literal["node"] = Field("node", description="消息类型：二级转发节点")
    data: SecondLevelForwardData

# Define the full Union including SecondLevelForwardMessage
AnyOfMessageComponent = Union[
    TextMessage,
    FaceMessage,
    ImageMessage,
    ReplyMessage,
    JsonMessage,
    VideoMessage,
    FileMessage,
    MarkdownMessage,
    ForwardWrapper,
    SecondLevelForwardMessage,
]

# Pydantic v2 handles string forward references automatically within the same module
# SecondLevelForwardData.model_rebuild() # Explicit rebuild usually not needed in v2

# First Level Forward Message Models (requires the Union)
class FirstLevelForwardData(BaseModel):
    user_id: str | int = Field(..., description="发送者用户ID")
    nickname: str = Field(..., description="发送者昵称")
    content: list[AnyOfMessageComponent] = Field(..., description="构建")

class FirstLevelForwardMessage(BaseModel):
    type: Literal["node"] = Field("node", description="消息类型：一级转发节点")
    data: FirstLevelForwardData

# Top-level Request Model
class SendForwardMsgReq(BaseModel):
    """
    请求模型：发送合并转发消息
    """
    group_id: str | int | None = Field(None, description="群号")
    user_id: str | int | None = Field(None, description="用户ID")
    messages: list[FirstLevelForwardMessage] = Field(..., description="一级合并转发消息列表")
    news: list[NewsItem] = Field(..., description="外显新闻列表 (需在所有客户端显示)")
    prompt: str = Field(..., description="外显文本 (显示在消息顶部的引导)")
    summary: str = Field(..., description="底部文本 (显示在消息底部的摘要)")
    source: str = Field(..., description="来源信息 (显示在消息底部的来源)")

# endregion req



# region res
# Top-level Response Data Model
class SendForwardMsgResData(BaseModel):
    """
    响应数据模型 (为空)
    """
    pass # Empty object as per spec

# Top-level Response Model
class SendForwardMsgRes(BaseModel):
    """
    响应模型：发送合并转发消息
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: SendForwardMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误信息（针对用户）")
    echo: str | None = Field(None, description="Echo回显")

# endregion res

# region api
class SendForwardMsgAPI(BaseModel):
    """send_forward_msg接口数据模型"""
    endpoint: str = "send_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendForwardMsgReq
    Res: type[BaseModel] = SendForwardMsgRes
# endregion api




# endregion code
