# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/保留
@homepage: https://napcat.apifox.cn/226656652e0
@llms.txt: https://napcat.apifox.cn/226656652e0.md
@last_update: 2025-04-26 01:17:44

@description:

summary:send_msg

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_msg"
__id__ = "226656652e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req definitions (Message Segments)
# https://napcat.apifox.cn/226656652e0#/components/schemas/%E6%96%87%E6%9C%AC%E6%B6%88%E6%81%AF
class TextSegmentData(BaseModel):
    text: str = Field(..., description="文本内容")

class TextSegment(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型")
    data: TextSegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/%E8%89%BE%E7%89%B9%E6%B6%88%E6%81%AF
class AtSegmentData(BaseModel):
    qq: int | str | Literal["all"] = Field(..., description="艾特目标QQ号, all 表示艾特全体")
    name: str | None = Field(None, description="昵称，通常不填，留给客户端自行查询")

class AtSegment(BaseModel):
    type: Literal["at"] = Field("at", description="消息类型")
    data: AtSegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/%E8%A1%A8%E6%83%85%E6%B6%88%E6%81%AF
class FaceSegmentData(BaseModel):
    id: int = Field(..., description="表情ID")

class FaceSegment(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型")
    data: FaceSegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/%E5%9B%BE%E7%89%87%E6%B6%88%E6%81%AF
class ImageSegmentData(BaseModel):
    file: str = Field(..., description="图片文件路径或URL或base64")
    summary: str = Field("[图片]", description="图片摘要，可选，默认为'[图片]'")

class ImageSegment(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型")
    data: ImageSegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/%E5%9B%9E%E5%A4%8D%E6%B6%88%E6%81%AF
class ReplySegmentData(BaseModel):
    id: int | str = Field(..., description="要回复的消息ID")

class ReplySegment(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型")
    data: ReplySegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/JSON%E6%B6%88%E6%81%AF
class JsonSegmentData(BaseModel):
    data: str = Field(..., description="JSON字符串内容")

class JsonSegment(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型")
    data: JsonSegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/%E8%AF%AD%E9%9F%B3%E6%B6%88%E6%81%AF
class RecordSegmentData(BaseModel):
    file: str = Field(..., description="语音文件路径或URL或base64")

class RecordSegment(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型")
    data: RecordSegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/%E8%A7%86%E9%A2%91%E6%80%BB%E6%80%BB
class VideoSegmentData(BaseModel):
    file: str = Field(..., description="视频文件路径或URL或base64")

class VideoSegment(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型")
    data: VideoSegmentData = Field(..., description="消息数据")

# https://napcat.apifox.cn/226656652e0#/components/schemas/markdown%E6%B6%88%E6%81%AF
# NOTE: OpenAPI spec defines this with type 'record', which seems unusual for markdown.
# Following the spec literally here.
class MarkdownSegmentData(BaseModel):
    content: str = Field(..., description="Markdown内容")

class MarkdownSegment(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型 (as per spec)")
    data: MarkdownSegmentData = Field(..., description="消息数据")

# Union of all possible message segment types
MessageSegment = TextSegment | AtSegment | FaceSegment | ImageSegment | ReplySegment | JsonSegment | RecordSegment | VideoSegment | MarkdownSegment


# https://napcat.apifox.cn/226656652e0#/paths/~1send_msg/post/requestBody
class SendMsgReq(BaseModel):
    """
    发送消息请求模型
    """
    message_type: Literal["group", "private"] = Field(..., description="消息类型: group 或 private")
    group_id: int | str | None = Field(None, description="群ID (message_type为group时填写)")
    user_id: int | str | None = Field(None, description="用户ID (message_type为private时填写)")
    message: list[MessageSegment] = Field(..., description="消息内容列表")

# endregion req


# region res definitions
# https://napcat.apifox.cn/226656652e0#/components/schemas/result
class ResultBase(BaseModel):
    """
    基础响应模型
    """
    status: str = Field(..., description="状态码")
    retcode: int = Field(..., description="返回码")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="echo")

# https://napcat.apifox.cn/226656652e0#/paths/~1send_msg/post/responses/200/content/application~json/schema/properties/data
class SendMsgResData(BaseModel):
    """
    发送消息响应数据详情
    """
    message_id: int = Field(..., description="消息ID")

# https://napcat.apifox.cn/226656652e0#/paths/~1send_msg/post/responses/200
class SendMsgRes(ResultBase):
    """
    发送消息响应模型
    """
    data: SendMsgResData = Field(..., description="响应数据")

# endregion res

# region api
class SendMsgAPI(BaseModel):
    """send_msg接口数据模型"""
    endpoint: str = "send_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendMsgReq
    Res: type[BaseModel] = SendMsgRes
# endregion api


# endregion code
