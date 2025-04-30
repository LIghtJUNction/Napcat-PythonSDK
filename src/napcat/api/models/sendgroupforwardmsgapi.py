# -*- coding: utf-8 -*-
from __future__ import annotations
# region METADATA
"""
@tags: 消息相关/发送群聊消息
@homepage: https://napcat.apifox.cn/226657396e0
@llms.txt: https://napcat.apifox.cn/226657396e0.md
@last_update: 2025-04-30 00:53:40

@description: 

summary:发送群合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_group_forward_msg"
__id__ = "226657396e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SendGroupForwardMsgReq(BaseModel):
    """发送群合并转发消息请求"""

    # 定义各种消息类型
    class TextMessage(BaseModel):
        """文本消息"""
        type: Literal["text"] = Field("text", description="消息类型，固定为 'text'")
        data: dict[str, str] = Field(..., description="文本消息数据")
    
    class FaceMessage(BaseModel):
        """表情消息"""
        type: Literal["face"] = Field("face", description="消息类型，固定为 'face'")
        data: dict[str, int] = Field(..., description="表情消息数据")
    
    class ImageMessage(BaseModel):
        """图片消息"""
        type: Literal["image"] = Field("image", description="消息类型，固定为 'image'")
        data: dict[str, str] = Field(..., description="图片消息数据")
    
    class ReplyMessage(BaseModel):
        """回复消息"""
        type: Literal["reply"] = Field("reply", description="消息类型，固定为 'reply'")
        data: dict[str, int | str] = Field(..., description="回复消息数据")
    
    class JsonMessage(BaseModel):
        """JSON消息"""
        type: Literal["json"] = Field("json", description="消息类型，固定为 'json'")
        data: dict[str, str] = Field(..., description="JSON消息数据")
    
    class VideoMessage(BaseModel):
        """视频消息"""
        type: Literal["video"] = Field("video", description="消息类型，固定为 'video'")
        data: dict[str, str] = Field(..., description="视频消息数据")
    
    class FileMessage(BaseModel):
        """文件消息"""
        type: Literal["file"] = Field("file", description="消息类型，固定为 'file'")
        data: dict[str, str] = Field(..., description="文件消息数据")
    
    class MarkdownMessage(BaseModel):
        """Markdown消息"""
        type: Literal["record"] = Field("record", description="消息类型，固定为 'record'")
        data: dict[str, str] = Field(..., description="Markdown消息数据")
    
    class ForwardMessage(BaseModel):
        """转发消息"""
        class ForwardMessageData(BaseModel):
            """转发消息数据"""
            id: str = Field(..., description="转发消息ID (res_id)")
        
        type: Literal["forward"] = Field("forward", description="消息类型，固定为 'forward'")
        data: ForwardMessageData = Field(..., description="转发消息数据")

    class NewsItem(BaseModel):
        """外显文本条目"""
        text: str = Field(..., description="外显文本内容")

    # 二级合并转发消息节点（可在一级节点内包含）
    class SecondLevelForwardNode(BaseModel):
        """二级合并转发消息节点"""
        class SecondLevelNodeData(BaseModel):
            """二级合并转发消息数据"""
            user_id: int | str = Field(..., description="用户ID")
            nickname: str = Field(..., description="用户昵称")
            content: list[SendGroupForwardMsgReq.TextMessage | SendGroupForwardMsgReq.FaceMessage | SendGroupForwardMsgReq.ImageMessage | SendGroupForwardMsgReq.ReplyMessage | SendGroupForwardMsgReq.JsonMessage | SendGroupForwardMsgReq.VideoMessage | SendGroupForwardMsgReq.FileMessage | SendGroupForwardMsgReq.MarkdownMessage | SendGroupForwardMsgReq.ForwardMessage] = Field(..., description="消息内容列表")
            news: list[SendGroupForwardMsgReq.NewsItem] | None = Field(default=None, description="外显文本列表")
            prompt: str | None = Field(default=None, description="外显")
            summary: str | None = Field(default=None, description="底部文本")
            source: str | None = Field(default=None, description="标题")
        
        type: Literal["node"] = Field("node", description="消息类型，固定为 'node'")
        data: SecondLevelNodeData = Field(..., description="二级合并转发消息数据")

    class ForwardMessageNode(BaseModel):
        """一级合并转发消息节点"""
        class ForwardMessageNodeData(BaseModel):
            """一级合并转发消息数据"""
            user_id: int | str = Field(..., description="用户ID")
            nickname: str = Field(..., description="用户昵称")
            content: list[SendGroupForwardMsgReq.TextMessage | SendGroupForwardMsgReq.FaceMessage | SendGroupForwardMsgReq.ImageMessage | SendGroupForwardMsgReq.ReplyMessage | SendGroupForwardMsgReq.JsonMessage | SendGroupForwardMsgReq.VideoMessage | SendGroupForwardMsgReq.FileMessage | SendGroupForwardMsgReq.MarkdownMessage | SendGroupForwardMsgReq.ForwardMessage | SendGroupForwardMsgReq.SecondLevelForwardNode] = Field(..., description="消息内容列表")

        type: Literal["node"] = Field("node", description="消息类型, 固定为 'node'")
        data: ForwardMessageNodeData = Field(..., description="合并转发消息数据")

    group_id: int | str = Field(..., description="群组 ID")
    messages: list[ForwardMessageNode] = Field(..., description="合并转发消息节点列表")
    news: list[NewsItem] = Field([], description="外显文本列表")
    prompt: str = Field("", description="外显文本")
    summary: str = Field("", description="底部文本")
    source: str = Field("", description="内容标题")

# endregion req



# region res
class SendGroupForwardMsgRes(BaseModel):
    """发送群合并转发消息响应"""
    class SendGroupForwardMsgResData(BaseModel):
        """发送群合并转发消息响应数据"""
        message_id: int = Field(..., description="消息 ID")
        res_id: str = Field(..., description="响应 ID")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应返回码")
    data: SendGroupForwardMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应文案")
    echo: str | None = Field(None, description="Echo 参数")

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
