# -*- coding: utf-8 -*-
from __future__ import annotations
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/226657396e0
@llms.txt: https://napcat.apifox.cn/226657396e0.md
@last_update: 2025-04-26 01:17:44

@description: 
功能：发送群合并转发消息
实现了递归嵌套的转发消息数据结构，支持一层嵌套
支持文本、表情、图片等多种消息类型
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

# 转发外显消息项模型
class ForwardNewsItem(BaseModel):
    """转发外显消息项模型"""
    text: str = Field(..., description="外显内容")

# Define basic message types
class TextMessage(BaseModel):
    """文本消息数据模型"""
    class TextMessageData(BaseModel):
        text: str = Field(..., description="文本内容")
    
    type: Literal['text'] = Field("text", description="消息类型，固定为 text")
    data: TextMessageData = Field(..., description="文本消息数据")

class FaceMessage(BaseModel):
    """表情消息数据模型"""
    class FaceMessageData(BaseModel):
        id: int = Field(..., description="表情 ID")
    
    type: Literal['face'] = Field("face", description="消息类型，固定为 face")
    data: FaceMessageData = Field(..., description="表情消息数据")

class ImageMessage(BaseModel):
    """图片消息数据模型"""
    class ImageMessageData(BaseModel):
        file: str = Field(..., description="图片文件路径或 URL 或 Base64")
        summary: str = Field('[图片]', description="图片消息摘要")
    
    type: Literal['image'] = Field("image", description="消息类型，固定为 image")
    data: ImageMessageData = Field(..., description="图片消息数据")

class ReplyMessage(BaseModel):
    """回复消息数据模型"""
    class ReplyMessageData(BaseModel):
        id: str | int = Field(..., description="回复消息的 ID")
    
    type: Literal['reply'] = Field("reply", description="消息类型，固定为 reply")
    data: ReplyMessageData = Field(..., description="回复消息数据")

class JsonMessage(BaseModel):
    """JSON消息数据模型"""
    class JsonMessageData(BaseModel):
        data: str = Field(..., description="JSON 字符串")
        
    type: Literal['json'] = Field("json", description="消息类型，固定为 json")
    data: JsonMessageData = Field(..., description="JSON 消息数据")

class VideoMessage(BaseModel):
    """视频消息数据模型"""
    class VideoMessageData(BaseModel):
        file: str = Field(..., description="视频文件路径或 URL 或 Base64")

    type: Literal['video'] = Field("video", description="消息类型，固定为 video")
    data: VideoMessageData = Field(..., description="视频消息数据")

class FileMessage(BaseModel):
    """文件消息数据模型"""
    class FileMessageData(BaseModel):
        file: str = Field(..., description="文件路径或 URL 或 Base64")
        name: str = Field('', description="文件名")
    
    type: Literal['file'] = Field("file", description="消息类型，固定为 file")
    data: FileMessageData = Field(..., description="文件消息数据")

class MarkdownMessage(BaseModel):
    """Markdown消息数据模型"""
    class MarkdownMessageData(BaseModel):
        content: str = Field(..., description="Markdown 内容")
    
    type: Literal['record'] = Field("record", description="消息类型，固定为 record")
    data: MarkdownMessageData = Field(..., description="Markdown 消息数据")

class SendForwardMessage(BaseModel):
    """发送已有转发消息的模型"""
    class SendForwardMessageData(BaseModel):
        class SendForwardMessageContent(BaseModel):
            class SendForwardMessageContentData(BaseModel):
                id: str = Field(..., description="转发消息的 res_id")

            type: Literal['forward'] = Field("forward", description="内容类型，固定为 forward")
            data: SendForwardMessageContentData = Field(..., description="转发内容数据")

        user_id: int | str = Field(..., description="用户 ID")
        nickname: str = Field(..., description="用户昵称")
        content: SendForwardMessageContent = Field(..., description="转发消息内容")

    type: Literal['node'] = Field("node", description="消息类型，固定为 node")
    data: SendForwardMessageData = Field(..., description="转发消息数据")


type BasicMessageType = TextMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage | VideoMessage | FileMessage | MarkdownMessage | SendForwardMessage

# 定义合并转发消息（使用Self支持递归嵌套）
class ForwardMessage(BaseModel):
    """合并转发消息模型
    
    使用Self来表示递归结构，支持消息的嵌套转发
    当作为二级转发消息时，content内容应仅包含基础消息类型
    当作为一级转发消息时，content可包含基础消息类型和其他转发消息
    """
    class ForwardMessageData(BaseModel):
        user_id: int | str = Field(..., description="用户 ID")
        nickname: str = Field(..., description="用户昵称")
        # 使用Self表示递归类型，可以包含基础消息和ForwardMessage自身
        content: list[BasicMessageType | ForwardMessage ] = Field(..., description="转发消息内容列表")

        news: list[ForwardNewsItem] | None = Field(None, description="外显新闻列表")
        prompt: str | None = Field(None, description="外显")
        summary: str | None = Field(None, description="底下文本")
        source: str | None = Field(None, description="标题")

    type: Literal['node'] = Field("node", description="消息类型，固定为 node")
    data: ForwardMessageData = Field(..., description="转发消息数据")

# 定义发送群合并转发消息的请求模型
class SendGroupForwardMsgReq(BaseModel):
    """发送群合并转发消息请求数据
    
    messages数组中的元素是一级转发消息
    一级转发消息的content可以包含基础消息类型和二级转发消息
    二级转发消息的content只能包含基础消息类型，不能再嵌套转发消息
    """
    group_id: int | str = Field(..., description="群号")
    messages: list[ForwardMessage] = Field(..., description="转发消息列表")
    news: list[ForwardNewsItem] = Field(..., description="外显新闻列表")
    prompt: str = Field(..., description="外显")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="内容")

# endregion req

# region res

class SendGroupForwardMsgRes(BaseModel):
    """发送群合并转发消息响应数据"""
    class SendGroupForwardMsgResData(BaseModel):
        message_id: int = Field(..., description="消息 ID")
        res_id: str = Field(..., description="资源 ID")

    status: Literal['ok'] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: SendGroupForwardMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="Echo")
    
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
