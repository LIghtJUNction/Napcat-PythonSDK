# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 
@homepage: 
@llms.txt: 
@last_update: 2025-04-30 00:00:00

@description: 
功能：发送合并转发消息
支持多层嵌套的消息结构，包含一级转发节点和二级转发节点
支持文本、表情、图片、回复、JSON、视频、文件、Markdown等多种消息类型
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_forward_msg"
__id__ = "226659136e0"
__method__ = "POST"
# endregion METADATA

# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)
logger.debug("加载 SendForwardMsgAPI 模型")

# region req
class SendForwardMsgReq(BaseModel):
    """发送合并转发消息请求模型"""
    
    class NewsItem(BaseModel):
        """新闻项模型"""
        text: str = Field(..., description="新闻内容文本")
    
    class TextMessage(BaseModel):
        """文本消息模型"""
        class TextMessageData(BaseModel):
            """文本消息数据"""
            text: str = Field(..., description="文本内容")
        
        type: Literal["text"] = Field("text", description="消息类型：文本")
        data: TextMessageData = Field(..., description="消息数据")
    
    class FaceMessage(BaseModel):
        """表情消息模型"""
        class FaceMessageData(BaseModel):
            """表情消息数据"""
            id: int = Field(..., description="表情ID")
        
        type: Literal["face"] = Field("face", description="消息类型：表情")
        data: FaceMessageData = Field(..., description="消息数据")
    
    class ImageMessage(BaseModel):
        """图片消息模型"""
        class ImageMessageData(BaseModel):
            """图片消息数据"""
            file: str = Field(..., description="图片文件名")
            summary: str = Field('[图片]', description="外显")
        
        type: Literal["image"] = Field("image", description="消息类型：图片")
        data: ImageMessageData = Field(..., description="消息数据")
    
    class ReplyMessage(BaseModel):
        """回复消息模型"""
        class ReplyMessageData(BaseModel):
            """回复消息数据"""
            id: str | int = Field(..., description="被回复消息ID")
        
        type: Literal["reply"] = Field("reply", description="消息类型：回复")
        data: ReplyMessageData = Field(..., description="消息数据")
    
    class JsonMessage(BaseModel):
        """JSON消息模型"""
        class JsonMessageData(BaseModel):
            """JSON消息数据"""
            data: str = Field(..., description="JSON字符串")
        
        type: Literal["json"] = Field("json", description="消息类型：JSON")
        data: JsonMessageData = Field(..., description="消息数据")
    
    class VideoMessage(BaseModel):
        """视频消息模型"""
        class VideoMessageData(BaseModel):
            """视频消息数据"""
            file: str = Field(..., description="视频文件名")
        
        type: Literal["video"] = Field("video", description="消息类型：视频")
        data: VideoMessageData = Field(..., description="消息数据")
    
    class FileMessage(BaseModel):
        """文件消息模型"""
        class FileMessageData(BaseModel):
            """文件消息数据"""
            file: str = Field(..., description="文件文件名")
            name: str = Field(..., description="文件名称")
        
        type: Literal["file"] = Field("file", description="消息类型：文件")
        data: FileMessageData = Field(..., description="消息数据")
    
    class MarkdownMessage(BaseModel):
        """Markdown消息模型"""
        class MarkdownMessageData(BaseModel):
            """Markdown消息数据"""
            content: str = Field(..., description="Markdown内容")
        
        type: Literal["record"] = Field("record", description="消息类型：Markdown (OpenAPI spec indicates 'record')")
        data: MarkdownMessageData = Field(..., description="消息数据")
    
    class ForwardContent(BaseModel):
        """转发内容模型"""
        class ForwardContentData(BaseModel):
            """转发内容数据"""
            id: str = Field(..., description="res_id")
        
        type: Literal["forward"] = Field("forward", description="消息类型：转发内部内容")
        data: ForwardContentData = Field(..., description="内容数据")
    
    class ForwardWrapper(BaseModel):
        """转发包装消息模型"""
        class ForwardWrapperData(BaseModel):
            """转发包装数据"""
            user_id: str | int = Field(..., description="发送者用户ID")
            nickname: str = Field(..., description="发送者昵称")
            content: "SendForwardMsgReq.ForwardContent" = Field(..., description="转发内容")
        
        type: Literal["node"] = Field("node", description="消息类型：转发节点")
        data: ForwardWrapperData = Field(..., description="节点数据")
    
    class SecondLevelForwardMessage(BaseModel):
        """二级转发消息模型"""
        class SecondLevelForwardData(BaseModel):
            """二级转发数据"""
            user_id: str | int = Field(..., description="发送者用户ID")
            nickname: str = Field(..., description="发送者昵称")
            content: list["SendForwardMsgReq.MessageComponent"] = Field(..., description="消息内容列表")
            news: list["SendForwardMsgReq.NewsItem"] | None = Field(None, description="外显新闻列表")
            prompt: str | None = Field(None, description="外显文本")
            summary: str | None = Field(None, description="底下文本")
            source: str | None = Field(None, description="内容来源")
        
        type: Literal["node"] = Field("node", description="消息类型：二级转发节点")
        data: SecondLevelForwardData = Field(..., description="节点数据")
    
    class FirstLevelForwardMessage(BaseModel):
        """一级转发消息模型"""
        class FirstLevelForwardData(BaseModel):
            """一级转发数据"""
            user_id: str | int = Field(..., description="发送者用户ID")
            nickname: str = Field(..., description="发送者昵称")
            content: list["SendForwardMsgReq.MessageComponent"] = Field(..., description="消息内容列表")
        
        type: Literal["node"] = Field("node", description="消息类型：一级转发节点")
        data: FirstLevelForwardData = Field(..., description="节点数据")
    
    # 定义一个类型别名，包含所有可能的消息组件类型
    MessageComponent = TextMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage | VideoMessage | FileMessage | MarkdownMessage | ForwardWrapper | SecondLevelForwardMessage | FirstLevelForwardMessage
    
    # 请求字段定义
    group_id: str | int | None = Field(None, description="群号")
    user_id: str | int | None = Field(None, description="用户ID")
    messages: list[FirstLevelForwardMessage] = Field(..., description="一级合并转发消息列表")
    news: list[NewsItem] = Field(..., description="外显新闻列表 (需在所有客户端显示)")
    prompt: str = Field(..., description="外显文本 (显示在消息顶部的引导)")
    summary: str = Field(..., description="底部文本 (显示在消息底部的摘要)")
    source: str = Field(..., description="来源信息 (显示在消息底部的来源)")
# endregion req

# region res
class SendForwardMsgRes(BaseModel):
    """发送合并转发消息响应模型"""
    class SendForwardMsgResData(BaseModel):
        """响应数据模型"""
        message_id: int | None = Field(None, description="消息 ID")
        forward_id: str | None = Field(None, description="转发 ID")
    
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(0, description="返回码")
    data: SendForwardMsgResData = Field(..., description="响应数据")
    message: str = Field("", description="错误信息")
    wording: str = Field("", description="错误信息（针对用户）")
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