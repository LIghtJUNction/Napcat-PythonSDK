# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657396e0
@llms.txt: https://napcat.apifox.cn/226657396e0.md
@last_update: 2025-04-25 23:00:49

@description: 

summary:发送群合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_forward_msg"
__id__ = "226657396e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)


# region component_models
class TextMessage(BaseModel):
    type: str = Field(default='text', const=True, description="Type字段，固定为'text'")
    data: dict[str, str] = Field(description="文本消息内容")


class FaceMessage(BaseModel):
    type: str = Field(default='face', const=True, description="Type字段，固定为'face'")
    data: dict[str, int] = Field(description="表情消息内容")


class ImageMessage(BaseModel):
    type: str = Field(default='image', const=True, description="Type字段，固定为'image'")
    data: dict[str, str] = Field(description="图片消息内容")


class ReplyMessage(BaseModel):
    type: str = Field(default='reply', const=True, description="Type字段，固定为'reply'")
    data: dict[str, str | int] = Field(description="回复消息内容")


class JSONMessage(BaseModel):
    type: str = Field(default='json', const=True, description="Type字段，固定为'json'")
    data: dict[str, str] = Field(description="JSON消息内容")


class VideoMessage(BaseModel):
    type: str = Field(default='video', const=True, description="Type字段，固定为'video'")
    data: dict[str, str] = Field(description="视频消息内容")


class FileMessage(BaseModel):
    type: str = Field(default='file', const=True, description="Type字段，固定为'file'")
    data: dict[str, str] = Field(description="文件消息内容")


class MarkdownMessage(BaseModel):
    type: str = Field(default='record', const=True, description="Type字段，固定为'record'")
    data: dict[str, str] = Field(description="Markdown消息内容")


class SendForward(BaseModel):
    type: str = Field(default='node', const=True, description="Type字段，固定为'node'")
    data: dict[str, str] = Field(description="发送forward内容")


class SecondForwardMessage(BaseModel):
    type: str = Field(default='node', const=True, description="Type字段，固定为'node'")
    data: dict[str, str] = Field(description="二级合并转发消息内容")


class UserId(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")


FirstForwardMessageContent = TextMessage | FaceMessage | ImageMessage | ReplyMessage | JSONMessage | VideoMessage | FileMessage | MarkdownMessage | SendForward | SecondForwardMessage


class FirstForwardMessage(BaseModel):
    type: str = Field(default='node', const=True, description="Type字段，固定为'node'")
    data: dict[str, str | int | list[FirstForwardMessageContent]] = Field(description="一级合并转发消息内容")


GroupId = str | int
UserIdType = str | int


class ResultData(BaseModel):
    message_id: float = Field(description="message_id字段")
    res_id: str = Field(description="res_id字段")


class Result(BaseModel):
    status: str = Field(default='ok', const=True, description="状态码，固定为'ok'")
    retcode: float = Field(description="返回码")
    data: ResultData = Field(description="返回数据")
    message: str = Field(description="消息内容")
    wording: str = Field(description="提示语")
    echo: str | None = Field(None, description="Echo字段")


# region component_models/

# region req
class SendGroupForwardMsgReq(BaseModel):
    """发送群合并转发消息"""
    group_id: GroupId = Field(description="群ID")
    messages: list[FirstForwardMessage] = Field(description="一级合并转发消息列表")
    news: list[dict[str, str]] = Field(description="外显消息列表")
    prompt: str = Field(description="外显")
    summary: str = Field(description="底下文本")
    source: str = Field(description="内容")


# region req/


# region res
class SendGroupForwardMsgRes(BaseModel):
    """发送群合并转发消息"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        message_id: float | None = Field(default=None, description="message_id字段")
        res_id: str | None = Field(default=None, description="res_id字段")

    class NewsItem(BaseModel):
        """NewsItem类型"""
        text: str = Field(description="text字段")

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=ResponseData, description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")


# region res/

# region api
# class SendGroupForwardMsgAPI(BaseModel):
#     """send_group_forward_msg接口数据模型"""
#     endpoint: str = "send_group_forward_msg"
#     method: str = "POST"
#     Req: type[BaseModel] = SendGroupForwardMsgReq
#     Res: type[BaseModel] = SendGroupForwardMsgRes
#     logger = logging.getLogger(__name__)
#
#     def __init__(self) -> None:
#         super().__init__()
#         self.logger.debug("初始化 SendGroupForwardMsgAPI")
#
#     def __call__(self, req: SendGroupForwardMsgReq) -> SendGroupForwardMsgRes:
#         """
#         调用API的方法（仅作为接口定义，不包含实际请求逻辑）
#
#         Args:
#             req: 请求参数对象
#
#         Returns:
#             响应对象
#         """
#         # 调试日志
#         self.logger.debug(f"调用 SendGroupForwardMsgAPI API")
#         self.logger.debug(f"请求参数: {req.model_dump_json()}")
#
#         # 注意：这里不应该包含实际的请求逻辑
#         # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
#         raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/