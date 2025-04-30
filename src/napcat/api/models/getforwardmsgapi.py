# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226656712e0
@llms.txt: https://napcat.apifox.cn/226656712e0.md
@last_update: 2025-04-30 00:00:00

@description: 
功能：获取合并转发消息
从消息ID获取合并转发消息的具体内容，包含发送者信息和多种消息类型
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_forward_msg"
__id__ = "226656712e0"
__method__ = "POST"
# endregion METADATA

# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.debug("加载 GetForwardMsgAPI 模型")

# region req
class GetForwardMsgReq(BaseModel):
    """获取合并转发消息请求模型"""
    message_id: str = Field(..., description="合并转发消息ID")
# endregion req

# region res
class GetForwardMsgRes(BaseModel):
    """获取合并转发消息响应模型"""
    class Data(BaseModel):
        """响应数据详情"""
        # 先定义基础类型，避免循环引用
        class Sender(BaseModel):
            """消息发送者信息"""
            user_id: int = Field(..., description="发送者QQ号")
            nickname: str = Field(..., description="发送者昵称")
            sex: Literal["male", "female", "unknown"] = Field(..., description="性别")
            age: int | None = Field(None, description="年龄")
            card: str = Field(..., description="群名片")
            role: Literal["owner", "admin", "member"] | None = Field(None, description="群角色")
            
        class TextMessage(BaseModel):
            """文本消息"""
            class TextMessageData(BaseModel):
                """文本消息数据"""
                text: str = Field(..., description="文本内容")
            
            type: Literal["text"] = Field("text", description="消息类型：文本")
            data: TextMessageData = Field(..., description="消息数据")
        
        class AtMessage(BaseModel):
            """at消息"""
            class AtMessageData(BaseModel):
                """at消息数据"""
                qq: int | str = Field(..., description="被艾特用户的QQ号，或者all")
                name: str | None = Field(None, description="被艾特用户的群名片或昵称")
            
            type: Literal["at"] = Field("at", description="消息类型：at")
            data: AtMessageData = Field(..., description="消息数据")
        
        class FaceMessage(BaseModel):
            """表情消息"""
            class FaceMessageData(BaseModel):
                """表情消息数据"""
                id: int = Field(..., description="表情ID")
            
            type: Literal["face"] = Field("face", description="消息类型：表情")
            data: FaceMessageData = Field(..., description="消息数据")
        
        class ImageMessage(BaseModel):
            """图片消息"""
            class ImageMessageData(BaseModel):
                """图片消息数据"""
                file: str = Field(..., description="图片文件名或链接")
                summary: str = Field("[图片]", description="外显")
            
            type: Literal["image"] = Field("image", description="消息类型：图片")
            data: ImageMessageData = Field(..., description="消息数据")
        
        class ReplyMessage(BaseModel):
            """回复消息"""
            class ReplyMessageData(BaseModel):
                """回复消息数据"""
                id: int | str = Field(..., description="回复消息的ID")
            
            type: Literal["reply"] = Field("reply", description="消息类型：回复")
            data: ReplyMessageData = Field(..., description="消息数据")
        
        class JsonMessage(BaseModel):
            """JSON消息"""
            class JsonMessageData(BaseModel):
                """JSON消息数据"""
                data: str = Field(..., description="JSON字符串")
            
            type: Literal["json"] = Field("json", description="消息类型：JSON")
            data: JsonMessageData = Field(..., description="消息数据")
        
        class VoiceMessage(BaseModel):
            """语音消息 (使用record类型)"""
            class VoiceMessageData(BaseModel):
                """语音消息数据"""
                file: str = Field(..., description="语音文件名或链接")
            
            type: Literal["record"] = Field("record", description="消息类型：语音")
            data: VoiceMessageData = Field(..., description="消息数据")
        
        class MarkdownMessage(BaseModel):
            """Markdown消息 (也使用record类型)"""
            class MarkdownMessageData(BaseModel):
                """Markdown消息数据"""
                content: str = Field(..., description="Markdown内容")
            
            type: Literal["record"] = Field("record", description="消息类型：Markdown")
            data: MarkdownMessageData = Field(..., description="消息数据")
        
        class VideoMessage(BaseModel):
            """视频消息"""
            class VideoMessageData(BaseModel):
                """视频消息数据"""
                file: str = Field(..., description="视频文件名或链接")
            
            type: Literal["video"] = Field("video", description="消息类型：视频")
            data: VideoMessageData = Field(..., description="消息数据")
        
        class FileMessage(BaseModel):
            """文件消息"""
            class FileMessageData(BaseModel):
                """文件消息数据"""
                file: str = Field(..., description="文件名或链接")
                name: str | None = Field(None, description="文件名")
            
            type: Literal["file"] = Field("file", description="消息类型：文件")
            data: FileMessageData = Field(..., description="消息数据")
        
        # 声明ForwardMessage向前引用，处理循环引用问题
        class ForwardMessage(BaseModel):
            """转发消息"""
            class ForwardMessageData(BaseModel):
                """转发消息数据"""
                id: str = Field(..., description="合并转发消息ID")
                # 使用字符串类型注解引用还未定义的类型
                content: list["GetForwardMsgRes.Data.MessageDetail"] = Field(..., description="合并转发消息内容")
            
            type: Literal["forward"] = Field("forward", description="消息类型：转发")
            data: ForwardMessageData = Field(..., description="消息数据")
        
        # 定义MessageDetail类型，去掉之前的占位声明
        class MessageDetail(BaseModel):
            """消息详情"""
            self_id: int = Field(..., description="机器人QQ号")
            user_id: int = Field(..., description="消息发送者QQ号")
            time: int = Field(..., description="消息发送时间 (Unix timestamp)")
            message_id: int = Field(..., description="消息ID")
            message_seq: int = Field(..., description="消息序列号")
            real_id: int = Field(..., description="真实消息ID")
            real_seq: str = Field(..., description="真实消息序列号")
            message_type: str = Field(..., description="消息类型，如private, group")
            # 使用字符串类型注解引用已定义的类型
            sender: "GetForwardMsgRes.Data.Sender" = Field(..., description="发送者信息")
            raw_message: str = Field(..., description="原始CQ码消息")
            font: int = Field(..., description="字体")
            sub_type: str = Field(..., description="消息子类型")
            # 引用已定义的消息类型
            message: list[
                GetForwardMsgRes.Data.TextMessage |
                GetForwardMsgRes.Data.AtMessage |
                GetForwardMsgRes.Data.FaceMessage |
                GetForwardMsgRes.Data.ImageMessage |
                GetForwardMsgRes.Data.ReplyMessage |
                GetForwardMsgRes.Data.JsonMessage |
                GetForwardMsgRes.Data.VoiceMessage |
                GetForwardMsgRes.Data.VideoMessage |
                GetForwardMsgRes.Data.FileMessage |
                GetForwardMsgRes.Data.MarkdownMessage |
                GetForwardMsgRes.Data.ForwardMessage
            ] = Field(..., description="消息内容，数组形式，每个元素是不同的消息段")
            message_format: str = Field(..., description="消息格式，如array")
            post_type: str = Field(..., description="上报类型")
            group_id: int | None = Field(None, description="群号 (仅群消息)")
        
        # 响应的主数据结构
        message: list[MessageDetail] = Field(..., description="合并转发消息的详细内容列表")
    
    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(0, description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field("", description="响应消息")
    wording: str = Field("", description="中文描述")
    echo: str | None = Field(None, description="Echo回显")
# endregion res

# region api
class GetForwardMsgAPI(BaseModel):
    """get_forward_msg接口数据模型"""
    endpoint: str = "get_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetForwardMsgReq
    Res: type[BaseModel] = GetForwardMsgRes
# endregion api
# endregion code