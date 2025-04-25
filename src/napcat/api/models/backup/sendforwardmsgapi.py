# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226659136e0
@llms.txt: https://napcat.apifox.cn/226659136e0.md
@last_update: 2025-04-26 01:17:44

@description:
summary:发送合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_forward_msg"
__id__ = "226659136e0"
__method__ = "POST"

# endregion METADATA

# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal, Any, TypeAlias

logger = logging.getLogger(__name__)

# Define base message types Data classes first
class ReqTextMsgData(BaseModel):
    """文本消息 data"""
    text: str = Field(..., description="文本内容")

class ReqFaceMsgData(BaseModel):
    """表情消息 data"""
    id: int = Field(..., description="表情ID")

class ReqImageMsgData(BaseModel):
    """图片消息 data"""
    file: str = Field(..., description="图片文件路径或URL")
    summary: str = Field("[图片]", description="图片消息的摘要，默认为'[图片]'")

class ReqReplyMsgData(BaseModel):
    """回复消息 data"""
    id: int | str = Field(..., description="回复消息的ID")

class ReqJsonMsgData(BaseModel):
    """JSON消息 data"""
    data: str = Field(..., description="JSON字符串")

class ReqVideoMsgData(BaseModel):
    """视频消息 data"""
    file: str = Field(..., description="视频文件路径或URL")

class ReqFileMsgData(BaseModel):
    """文件消息 data"""
    file: str = Field(..., description="文件路径或URL")
    name: str = Field(..., description="文件名")

class ReqMarkdownMsgData(BaseModel):
    """Markdown消息 data"""
    content: str = Field(..., description="Markdown文本内容")

# Define nested forward message data classes
class ReqForwardMsgDataInner(BaseModel):
    """发送forward data 内层"""
    id: str = Field(..., description="资源ID (res_id)")

class ReqForwardMsgContent(BaseModel):
    """发送forward content"""
    type: Literal["forward"] = Field("forward", description="消息类型，固定为 'forward'")
    data: ReqForwardMsgDataInner = Field(..., description="内层 forward data")

class ReqForwardMsgData(BaseModel):
    """发送forward data 外层"""
    user_id: int | str = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    content: ReqForwardMsgContent = Field(..., description="Forward消息内容")

# Define news item for 二级合并转发消息 (also used for top-level news)
class ReqNewsItem(BaseModel):
    """新闻 item (用于二级合并转发消息和顶级请求)"""
    text: str = Field(..., description="新闻内容文本")

# Define a recursive type alias for message content
# Forward reference types that are defined later
MessageContent: TypeAlias = "ReqTextMsg | ReqFaceMsg | ReqImageMsg | ReqReplyMsg | ReqJsonMsg | ReqVideoMsg | ReqFileMsg | ReqMarkdownMsg | ReqForwardMsg | ReqNodeMsgV2"

# Define message component models (type + data)
class ReqTextMsg(BaseModel):
    """文本消息"""
    type: Literal["text"] = Field("text", description="消息类型，固定为 'text'")
    data: ReqTextMsgData = Field(..., description="消息数据")

class ReqFaceMsg(BaseModel):
    """表情消息"""
    type: Literal["face"] = Field("face", description="消息类型，固定为 'face'")
    data: ReqFaceMsgData = Field(..., description="消息数据")

class ReqImageMsg(BaseModel):
    """图片消息"""
    type: Literal["image"] = Field("image", description="消息类型，固定为 'image'")
    data: ReqImageMsgData = Field(..., description="消息数据")

class ReqReplyMsg(BaseModel):
    """回复消息"""
    type: Literal["reply"] = Field("reply", description="消息类型，固定为 'reply'")
    data: ReqReplyMsgData = Field(..., description="消息数据")

class ReqJsonMsg(BaseModel):
    """JSON消息"""
    type: Literal["json"] = Field("json", description="消息类型，固定为 'json'")
    data: ReqJsonMsgData = Field(..., description="消息数据")

class ReqVideoMsg(BaseModel):
    """视频消息"""
    type: Literal["video"] = Field("video", description="消息类型，固定为 'video'")
    data: ReqVideoMsgData = Field(..., description="消息数据")

class ReqFileMsg(BaseModel):
    """文件消息"""
    type: Literal["file"] = Field("file", description="消息类型，固定为 'file'")
    data: ReqFileMsgData = Field(..., description="消息数据")

class ReqMarkdownMsg(BaseModel):
    """Markdown消息"""
    type: Literal["record"] = Field("record", description="消息类型，固定为 'record'") # Note: OpenAPI spec says 'record' for markdown
    data: ReqMarkdownMsgData = Field(..., description="消息数据")

# Define the '发送forward' model
class ReqForwardMsg(BaseModel):
    """发送forward 消息节点"""
    type: Literal["node"] = Field("node", description="节点类型，固定为 'node'")
    data: ReqForwardMsgData = Field(..., description="节点数据")

# Define 二级合并转发消息 (can contain other messages, news, prompt, summary, source)
class ReqNodeMsgV2Data(BaseModel):
    """二级合并转发消息 data"""
    user_id: int | str = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    content: list[MessageContent] = Field(..., description="构建消息列表，可包含多种消息类型")
    news: list[ReqNewsItem] = Field(..., description="外显新闻列表")
    prompt: str = Field(..., description="外显文本")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="内容/标题")

class ReqNodeMsgV2(BaseModel):
    """二级合并转发消息节点"""
    type: Literal["node"] = Field("node", description="节点类型，固定为 'node'")
    data: ReqNodeMsgV2Data = Field(..., description="节点数据")

# Define 一级合并转发消息 (can contain other messages, including 二级合并转发消息 and 发送forward)
class ReqNodeMsgV1Data(BaseModel):
    """一级合并转发消息 data"""
    user_id: int | str = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    content: list[MessageContent] = Field(..., description="构建消息列表，可包含多种消息类型") # Reuses MessageContent

class ReqNodeMsgV1(BaseModel):
    """一级合并转发消息节点"""
    type: Literal["node"] = Field("node", description="节点类型，固定为 'node'")
    data: ReqNodeMsgV1Data = Field(..., description="节点数据")

# Ensure Pydantic handles the recursive type alias by updating forward refs
ReqNodeMsgV2Data.model_rebuild()
ReqNodeMsgV1Data.model_rebuild()

# region req
class SendForwardMsgReq(BaseModel):
    """
    发送合并转发消息 请求参数
    """
    group_id: int | str | None = Field(None, description="群ID")
    user_id: int | str | None = Field(None, description="用户ID")
    messages: list[ReqNodeMsgV1] = Field(..., description="一级合并转发消息列表")
    news: list[ReqNewsItem] = Field(..., description="外显新闻列表") # Corresponds to top-level news field
    prompt: str = Field(..., description="外显文本")
    summary: str = Field(..., description="底下文本")
    source: str = Field(..., description="内容/标题")
# endregion req



# region res
class SendForwardMsgRes(BaseModel):
    """
    发送合并转发消息 响应数据
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: dict[str, Any] = Field(..., description="响应数据体，通常为空对象 {}") # OpenAPI says empty object, use dict[str, Any]
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误信息")
    echo: str | None = Field(None, description="echo字段") # Nullable field, but required by schema

# endregion res

# region api
class SendForwardMsgAPI(BaseModel):
    """send_forward_msg接口数据模型"""
    endpoint: Literal["send_forward_msg"] = "send_forward_msg"
    method: Literal["POST"] = "POST"
    Req: type[BaseModel] = SendForwardMsgReq
    Res: type[BaseModel] = SendForwardMsgRes
# endregion api




# endregion code
