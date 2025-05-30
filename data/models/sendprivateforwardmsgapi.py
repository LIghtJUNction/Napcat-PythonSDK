# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657399e0
@llms.txt: https://napcat.apifox.cn/226657399e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:发送私聊合并转发消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_private_forward_msg"
__id__ = "226657399e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class 视频消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class 语音消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class JSON消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class 回复消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class 图片消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class 表情消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class 艾特消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class 文本消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class user_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class SendPrivateForwardMsgReq(BaseModel):
    """发送私聊合并转发消息"""
    user_id: user_id
    messages: list[MessagesItem]

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SendPrivateForwardMsgRes(BaseModel):
    """发送私聊合并转发消息"""
    class Data(BaseModel):
        """响应数据类型"""
        message_id: float = Field(default=None, description="message_id字段")
        res_id: str = Field(default=None, description="res_id字段")

        model_config = {
            "extra": "allow",
        }

    class MessagesItem(BaseModel):
        """MessagesItem类型"""
        type: str = Field(default=None, description="type字段")
        data: ResponseData = Field(default=None, description="data字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class SendPrivateForwardMsgAPI(BaseModel):
    """send_private_forward_msg接口数据模型"""
    endpoint: str = "send_private_forward_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendPrivateForwardMsgReq
    Res: type[BaseModel] = SendPrivateForwardMsgRes

# region api/
# endregion code

