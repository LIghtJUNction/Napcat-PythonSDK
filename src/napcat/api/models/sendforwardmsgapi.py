# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659136e0
@llms.txt: https://napcat.apifox.cn/226659136e0.md
@last_update: 2025-04-27 01:21:00

@description:
功能：发送合并转发消息
支持递归嵌套的转发消息结构
支持文本、表情、图片等多种消息类型
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.18"
__endpoint__ = "send_forward_msg"
__id__ = "226659136e0"
__method__ = "POST"
# endregion METADATA

# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal, Any

logger = logging.getLogger(__name__)

# 定义消息项用于外显消息
class NewsItem(BaseModel):
    """外显消息项"""
    text: str = Field(..., description="外显内容文本")

# 基础消息类型定义
class TextMsg(BaseModel):
    """文本消息"""
    class TextMsgData(BaseModel):
        """文本消息数据"""
        text: str = Field(..., description="文本内容")
    
    type: Literal["text"] = Field("text", description="消息类型，固定为 'text'")
    data: TextMsgData = Field(..., description="消息数据")

class FaceMsg(BaseModel):
    """表情消息"""
    class FaceMsgData(BaseModel):
        """表情消息数据"""
        id: int = Field(..., description="表情ID")
    
    type: Literal["face"] = Field("face", description="消息类型，固定为 'face'")
    data: FaceMsgData = Field(..., description="消息数据")

class ImageMsg(BaseModel):
    """图片消息"""
    class ImageMsgData(BaseModel):
        """图片消息数据"""
        file: str = Field(..., description="图片文件路径或URL")
        summary: str = Field("[图片]", description="图片消息摘要")
    
    type: Literal["image"] = Field("image", description="消息类型，固定为 'image'")
    data: ImageMsgData = Field(..., description="消息数据")

class ReplyMsg(BaseModel):
    """回复消息"""
    class ReplyMsgData(BaseModel):
        """回复消息数据"""
        id: int | str = Field(..., description="回复消息ID")
    
    type: Literal["reply"] = Field("reply", description="消息类型，固定为 'reply'")
    data: ReplyMsgData = Field(..., description="消息数据")

class JsonMsg(BaseModel):
    """JSON消息"""
    class JsonMsgData(BaseModel):
        """JSON消息数据"""
        data: str = Field(..., description="JSON字符串")
    
    type: Literal["json"] = Field("json", description="消息类型，固定为 'json'")
    data: JsonMsgData = Field(..., description="消息数据")

class VideoMsg(BaseModel):
    """视频消息"""
    class VideoMsgData(BaseModel):
        """视频消息数据"""
        file: str = Field(..., description="视频文件路径或URL")
    
    type: Literal["video"] = Field("video", description="消息类型，固定为 'video'")
    data: VideoMsgData = Field(..., description="消息数据")

class FileMsg(BaseModel):
    """文件消息"""
    class FileMsgData(BaseModel):
        """文件消息数据"""
        file: str = Field(..., description="文件路径或URL")
        name: str = Field(..., description="文件名")
    
    type: Literal["file"] = Field("file", description="消息类型，固定为 'file'")
    data: FileMsgData = Field(..., description="消息数据")

class MarkdownMsg(BaseModel):
    """Markdown消息"""
    class MarkdownMsgData(BaseModel):
        """Markdown消息数据"""
        content: str = Field(..., description="Markdown文本内容")
    
    type: Literal["record"] = Field("record", description="消息类型，固定为 'record'") 
    data: MarkdownMsgData = Field(..., description="消息数据")

# 发送已有转发消息的模型
class SendForwardMsg(BaseModel):
    """发送已有转发消息节点"""
    class SendForwardMsgData(BaseModel):
        """转发消息数据"""
        user_id: int | str = Field(..., description="用户ID")
        nickname: str = Field(..., description="昵称")
        content: SendForwardMsgContent = Field(..., description="转发消息内容")
        
        class SendForwardMsgContent(BaseModel):
            """转发消息内容"""
            type: Literal["forward"] = Field("forward", description="消息类型，固定为 'forward'")
            data: SendForwardMsgDataInner = Field(..., description="内层转发数据")
            
            class SendForwardMsgDataInner(BaseModel):
                """内层转发数据"""
                id: str = Field(..., description="资源ID (res_id)")
    
    type: Literal["node"] = Field("node", description="节点类型，固定为 'node'")
    data: SendForwardMsgData = Field(..., description="节点数据")

# 定义合并转发消息节点
class NodeMsg(BaseModel):
    """合并转发消息节点"""
    class NodeMsgData(BaseModel):
        """合并转发消息数据"""
        user_id: int | str = Field(..., description="用户ID")
        nickname: str = Field(..., description="昵称")
        # 使用递归类型，支持包含多种消息类型和嵌套转发
        content: list[TextMsg | FaceMsg | ImageMsg | ReplyMsg | JsonMsg | VideoMsg | FileMsg | MarkdownMsg | SendForwardMsg | NodeMsg] = Field(
            ..., description="消息内容列表，支持多种类型"
        )
        # 以下字段在一级节点中可选，二级节点中必填
        news: list[NewsItem] | None = Field(None, description="外显新闻列表")
        prompt: str | None = Field(None, description="外显文本")
        summary: str | None = Field(None, description="底下文本")
        source: str | None = Field(None, description="内容/标题")
    
    type: Literal["node"] = Field("node", description="节点类型，固定为 'node'")
    data: NodeMsgData = Field(..., description="节点数据")

# region req
class SendForwardMsgReq(BaseModel):
    """发送合并转发消息请求"""
    group_id: int | str | None = Field(None, description="群ID")
    user_id: int | str | None = Field(None, description="用户ID")
    messages: list[NodeMsg] = Field(..., description="合并转发消息列表")
    news: list[NewsItem] = Field(..., description="外显新闻列表")
    prompt: str = Field(..., description="外显文本")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="内容/标题")
# endregion req

# region res
class SendForwardMsgRes(BaseModel):
    """发送合并转发消息响应"""
    class SendForwardMsgResData(BaseModel):
        """响应数据体"""
        message_id: int = Field(..., description="消息ID")
        forward_id: str | None = Field(None, description="转发ID")
    
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: SendForwardMsgResData | dict[str, Any] = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="回显字段")
# endregion res

# region api
class SendForwardMsgAPI(BaseModel):
    """send_forward_msg接口数据模型"""
    endpoint: Literal["send_forward_msg"] = "send_forward_msg"
    method: Literal["POST"] = "POST"
    Req: type[BaseModel] = SendForwardMsgReq
    Res: type[BaseModel] = SendForwardMsgRes
# endregion api

logger.debug("加载 SendForwardMsgAPI 模型")
# endregion code
