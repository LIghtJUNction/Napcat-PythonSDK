# -*- coding: utf-8 -*- 
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658664e0
@llms.txt: https://napcat.apifox.cn/226658664e0.md
@last_update: 2025-04-25 23:00:49

@description: 获取群精华消息

summary:获取群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_essence_msg_list"
__id__ = "226658664e0"
__method__ = "POST"

# region METADATA/


# region code
from pydantic import BaseModel, Field
from typing import Any, Literal
import logging

logger = logging.getLogger(__name__)

# region component_models
class GroupId(BaseModel):
    group_id: str | int

    model_config = {
        "extra": "allow",
    }


class Markdown消息Data(BaseModel):
    content: str = Field(..., description="Markdown内容")

    model_config = {
        "extra": "allow",
    }


class Markdown消息(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型")
    data: Markdown消息Data = Field(..., description="Markdown消息数据")

    model_config = {
        "extra": "allow",
    }


class 视频消息Data(BaseModel):
    file: str = Field(..., description="视频文件路径")

    model_config = {
        "extra": "allow",
    }


class 视频消息(BaseModel):
    type: Literal["video"] = Field("video", description="消息类型")
    data: 视频消息Data = Field(..., description="视频消息数据")

    model_config = {
        "extra": "allow",
    }


class 语音消息Data(BaseModel):
    file: str = Field(..., description="语音文件路径")

    model_config = {
        "extra": "allow",
    }


class 语音消息(BaseModel):
    type: Literal["record"] = Field("record", description="消息类型")
    data: 语音消息Data = Field(..., description="语音消息数据")

    model_config = {
        "extra": "allow",
    }


class JSON消息Data(BaseModel):
    data: str = Field(..., description="JSON数据")

    model_config = {
        "extra": "allow",
    }


class JSON消息(BaseModel):
    type: Literal["json"] = Field("json", description="消息类型")
    data: JSON消息Data = Field(..., description="JSON消息数据")

    model_config = {
        "extra": "allow",
    }


class 回复消息Data(BaseModel):
    id: str | int = Field(..., description="回复消息ID")

    model_config = {
        "extra": "allow",
    }


class 回复消息(BaseModel):
    type: Literal["reply"] = Field("reply", description="消息类型")
    data: 回复消息Data = Field(..., description="回复消息数据")

    model_config = {
        "extra": "allow",
    }


class 图片消息Data(BaseModel):
    file: str = Field(..., description="图片文件路径")
    summary: str = Field("[图片]", description="图片描述")

    model_config = {
        "extra": "allow",
    }


class 图片消息(BaseModel):
    type: Literal["image"] = Field("image", description="消息类型")
    data: 图片消息Data = Field(..., description="图片消息数据")

    model_config = {
        "extra": "allow",
    }


class 表情消息Data(BaseModel):
    id: int = Field(..., description="表情ID")

    model_config = {
        "extra": "allow",
    }


class 表情消息(BaseModel):
    type: Literal["face"] = Field("face", description="消息类型")
    data: 表情消息Data = Field(..., description="表情消息数据")

    model_config = {
        "extra": "allow",
    }


class 艾特消息Data(BaseModel):
    qq: str | int | Literal["all"] = Field(..., description="艾特QQ号，all表示全体成员")
    name: str = Field(..., description="艾特昵称")

    model_config = {
        "extra": "allow",
    }


class 艾特消息(BaseModel):
    type: Literal["at"] = Field("at", description="消息类型")
    data: 艾特消息Data = Field(..., description="艾特消息数据")

    model_config = {
        "extra": "allow",
    }


class 文本消息Data(BaseModel):
    text: str = Field(..., description="文本内容")

    model_config = {
        "extra": "allow",
    }


class 文本消息(BaseModel):
    type: Literal["text"] = Field("text", description="消息类型")
    data: 文本消息Data = Field(..., description="文本消息数据")

    model_config = {
        "extra": "allow",
    }


MessageType = 文本消息 | 艾特消息 | 表情消息 | 图片消息 | 回复消息 | JSON消息 | 语音消息 | 视频消息 | Markdown消息


class EssenceMessage(BaseModel):
    msg_seq: float = Field(..., description="消息序列号")
    msg_random: float = Field(..., description="消息随机数")
    sender_id: float = Field(..., description="发送人账号")
    sender_nick: str = Field(..., description="发送人昵称")
    operator_id: float = Field(..., description="设精人账号")
    operator_nick: str = Field(..., description="设精人昵称")
    message_id: str = Field(..., description="消息ID")
    operator_time: str = Field(..., description="设精时间")
    content: list[MessageType] = Field(..., description="消息内容")

    model_config = {
        "extra": "allow",
    }


# region component_models/

# region req
class GetEssenceMsgListReq(BaseModel):
    """获取群精华消息"""
    group_id: GroupId = Field(..., description="群ID")

    model_config = {
        "extra": "allow",
    }


# region req/

# region res
class GetEssenceMsgListRes(BaseModel):
    """获取群精华消息"""

    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(0, description="retcode字段")
    data: list[EssenceMessage] = Field(..., description="精华消息列表")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }


# region res/

# region api
class GetEssenceMsgListAPI(BaseModel):
    """get_essence_msg_list接口数据模型"""
    endpoint: str = "get_essence_msg_list"
    method: str = "POST"
    Req: type[BaseModel] = GetEssenceMsgListReq
    Res: type[BaseModel] = GetEssenceMsgListRes
    logger = logging.getLogger(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.logger.debug("初始化 GetEssenceMsgListAPI")

    def __call__(self, req: GetEssenceMsgListReq) -> GetEssenceMsgListRes:
        """
        调用API的方法（仅作为接口定义，不包含实际请求逻辑）

        Args:
            req: 请求参数对象

        Returns:
            响应对象
        """
        # 调试日志
        self.logger.debug(f"调用 GetEssenceMsgListAPI API")
        self.logger.debug(f"请求参数: {req.model_dump_json()}")

        # 注意：这里不应该包含实际的请求逻辑
        # 这个方法只是定义了接口，实际的请求应由适配器或客户端实现
        raise NotImplementedError("此方法需要由实际的API客户端实现")


# region api/
# region code/