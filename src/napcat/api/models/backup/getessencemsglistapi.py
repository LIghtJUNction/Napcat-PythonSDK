# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226658664e0
@llms.txt: https://napcat.apifox.cn/226658664e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_essence_msg_list"
__id__ = "226658664e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Need Literal for const types

logger = logging.getLogger(__name__)

# region req
class GetEssenceMsgListReq(BaseModel):
    """
    获取群精华消息请求体
    """
    group_id: int | str = Field(..., description="群号")
# endregion req


# region res
# Define message content models
class TextMessage(BaseModel):
    """文本消息"""
    class Data(BaseModel):
        text: str = Field(..., description="文本内容")
    type: Literal['text'] = Field('text', description="消息类型")
    data: Data = Field(..., description="文本消息数据")

class AtMessage(BaseModel):
    """艾特消息"""
    class Data(BaseModel):
        qq: int | str = Field(..., description="艾特的QQ号或'all'")
        name: str = Field(..., description="艾特的名字") # Required by spec
    type: Literal['at'] = Field('at', description="消息类型")
    data: Data = Field(..., description="艾特消息数据")

class FaceMessage(BaseModel):
    """表情消息"""
    class Data(BaseModel):
        id: int = Field(..., description="表情ID")
    type: Literal['face'] = Field('face', description="消息类型")
    data: Data = Field(..., description="表情消息数据")

class ImageMessage(BaseModel):
    """图片消息"""
    class Data(BaseModel):
        file: str = Field(..., description="图片文件路径或URL")
        summary: str = Field('[图片]', description="图片消息摘要")
    type: Literal['image'] = Field('image', description="消息类型")
    data: Data = Field(..., description="图片消息数据")

class ReplyMessage(BaseModel):
    """回复消息"""
    class Data(BaseModel):
        id: int | str = Field(..., description="回复的消息ID")
    type: Literal['reply'] = Field('reply', description="消息类型")
    data: Data = Field(..., description="回复消息数据")

class JsonMessage(BaseModel):
    """JSON消息"""
    class Data(BaseModel):
        data: str = Field(..., description="JSON字符串内容")
    type: Literal['json'] = Field('json', description="消息类型")
    data: Data = Field(..., description="JSON消息数据")

class RecordMessage(BaseModel):
    """语音消息"""
    class Data(BaseModel):
        file: str = Field(..., description="语音文件路径或URL")
    type: Literal['record'] = Field('record', description="消息类型")
    data: Data = Field(..., description="语音消息数据")

class VideoMessage(BaseModel):
    """视频消息"""
    class Data(BaseModel):
        file: str = Field(..., description="视频文件路径或URL")
    type: Literal['video'] = Field('video', description="消息类型")
    data: Data = Field(..., description="视频消息数据")

# Assuming markdown type is 'markdown', not 'record' as per OpenAPI schema inconsistency
class MarkdownMessage(BaseModel):
    """Markdown消息"""
    class Data(BaseModel):
        content: str = Field(..., description="Markdown文本内容")
    type: Literal['markdown'] = Field('markdown', description="消息类型") # Adjusted type based on name
    data: Data = Field(..., description="Markdown消息数据")


# Define the Union of possible message content types
MessageContent = TextMessage | AtMessage | FaceMessage | ImageMessage | ReplyMessage | JsonMessage | RecordMessage | VideoMessage | MarkdownMessage


class EssenceMessage(BaseModel):
    """单个精华消息详情"""
    msg_seq: int = Field(..., description="消息序列号")
    msg_random: int = Field(..., description="消息随机数")
    sender_id: int = Field(..., description="发送人账号")
    sender_nick: str = Field(..., description="发送人昵称")
    operator_id: int = Field(..., description="设精人账号")
    operator_nick: str = Field(..., description="设精人昵称")
    message_id: str = Field(..., description="消息ID")
    operator_time: str = Field(..., description="设精时间")
    content: list[MessageContent] = Field(..., description="消息内容")


class GetEssenceMsgListRes(BaseModel):
    """
    获取群精华消息响应体
    """
    status: Literal['ok'] = Field('ok', description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: list[EssenceMessage] = Field(..., description="精华消息列表")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="echo回显")

# endregion res

# region api
class GetEssenceMsgListAPI(BaseModel):
    """get_essence_msg_list接口数据模型"""
    endpoint: str = "get_essence_msg_list"
    method: str = "POST"
    Req: type[BaseModel] = GetEssenceMsgListReq
    Res: type[BaseModel] = GetEssenceMsgListRes
# endregion api


# endregion code