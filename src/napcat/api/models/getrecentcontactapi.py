# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659190e0
@llms.txt: https://napcat.apifox.cn/226659190e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取的最新消息是每个会话最新的消息

summary:最近消息列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_recent_contact"
__id__ = "226659190e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
import logging
from enum import Enum

logger = logging.getLogger(__name__)

# region component_models
class ForwardMessage(BaseModel):
    type: str = Field("forward", const=True, description="type字段,固定值为 forward")
    data: "ForwardMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        id: str = Field(description="消息ID")
        content: list["消息详情"] = Field(description="消息内容列表")

    model_config = {
        "extra": "allow",
    }


class MarkdownMessage(BaseModel):
    type: str = Field("markdown", const=True, description="type字段,固定值为 markdown")
    data: "MarkdownMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        content: str = Field(description="Markdown 内容")

    model_config = {
        "extra": "allow",
    }


class VideoMessage(BaseModel):
    type: str = Field("video", const=True, description="type字段,固定值为 video")
    data: "VideoMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        file: str = Field(description="视频文件路径")

    model_config = {
        "extra": "allow",
    }


class RecordMessage(BaseModel):
    type: str = Field("record", const=True, description="type字段,固定值为 record")
    data: "RecordMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        file: str = Field(description="语音文件路径")

    model_config = {
        "extra": "allow",
    }


class JSONMessage(BaseModel):
    type: str = Field("json", const=True, description="type字段,固定值为 json")
    data: "JSONMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        data: str = Field(description="JSON 数据")

    model_config = {
        "extra": "allow",
    }


class ReplyMessage(BaseModel):
    type: str = Field("reply", const=True, description="type字段,固定值为 reply")
    data: "ReplyMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        id: str | int = Field(description="回复的消息ID")

    model_config = {
        "extra": "allow",
    }


class FileMessage(BaseModel):
    type: str = Field("file", const=True, description="type字段,固定值为 file")
    data: "FileMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        file: str = Field(description="文件路径")
        name: str = Field(description="文件名")

    model_config = {
        "extra": "allow",
    }


class ImageMessage(BaseModel):
    type: str = Field("image", const=True, description="type字段,固定值为 image")
    data: "ImageMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        file: str = Field(description="图片路径")
        summary: str = Field("[图片]", description="图片摘要")

    model_config = {
        "extra": "allow",
    }


class FaceMessage(BaseModel):
    type: str = Field("face", const=True, description="type字段,固定值为 face")
    data: "FaceMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        id: int = Field(description="表情ID")

    model_config = {
        "extra": "allow",
    }


class AtMessage(BaseModel):
    type: str = Field("at", const=True, description="type字段,固定值为 at")
    data: "AtMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        qq: str | int | str = Field(description="被艾特用户的QQ号, all表示全体成员")
        name: str = Field(description="被艾特用户的昵称")

    model_config = {
        "extra": "allow",
    }


class TextMessage(BaseModel):
    type: str = Field("text", const=True, description="type字段,固定值为 text")
    data: "TextMessage.Data" = Field(description="data字段")

    class Data(BaseModel):
        text: str = Field(description="文本内容")

    model_config = {
        "extra": "allow",
    }


class SexEnum(str, Enum):
    male = "male"
    female = "female"
    unknown = "unknown"


class RoleEnum(str, Enum):
    owner = "owner"
    admin = "admin"
    member = "member"


class Sender(BaseModel):
    user_id: float = Field(description="user_id字段")
    nickname: str = Field(description="nickname字段")
    sex: SexEnum | None = Field(None, description="性别")
    age: float | None = Field(None, description="年龄")
    card: str | None = Field(None, description="card字段")
    role: RoleEnum | None = Field(None, description="角色")

    model_config = {
        "extra": "allow",
    }


class Result(BaseModel):
    status: str = Field("ok", const=True, description="status字段,固定值为 ok")
    retcode: float = Field(description="retcode字段")
    data: list[dict[str, any]] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


class 消息详情(BaseModel):
    self_id: float = Field(description="self_id字段")
    user_id: float = Field(description="user_id字段")
    time: float = Field(description="time字段")
    message_id: float | None = Field(None, description="message_id字段")
    message_seq: float | None = Field(None, description="message_seq字段")
    real_id: float | None = Field(None, description="real_id字段")
    real_seq: str = Field(description="real_seq字段")
    message_type: str = Field(description="message_type字段")
    sender: Sender = Field(description="sender字段")
    raw_message: str = Field(description="raw_message字段")
    font: float = Field(description="font字段")
    sub_type: str = Field(description="sub_type字段")
    message: list[TextMessage | AtMessage | FaceMessage | ImageMessage | FileMessage | ReplyMessage | JSONMessage | RecordMessage | VideoMessage | MarkdownMessage | ForwardMessage] = Field(description="message字段")
    message_format: str = Field(description="message_format字段")
    post_type: str = Field(description="post_type字段")
    group_id: float | None = Field(None, description="group_id字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetRecentContactReq(BaseModel):
    """最近消息列表"""
    count: float = Field(description="会话数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetRecentContactRes(BaseModel):
    """最近消息列表"""

    class ResponseData(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: ResponseData = Field(default_factory=lambda: GetRecentContactRes.ResponseData(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetRecentContactAPI(BaseModel):
    """get_recent_contact接口数据模型"""
    endpoint: str = "get_recent_contact"
    method: str = "POST"
    Req: type[BaseModel] = GetRecentContactReq
    Res: type[BaseModel] = GetRecentContactRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetRecentContactAPI")

    def __call__(self, req: GetRecentContactReq) -> GetRecentContactRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）
        
        Args:
            req: 请求参数对象
            
        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetRecentContactAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")
        
        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")

# region api/
# region code/