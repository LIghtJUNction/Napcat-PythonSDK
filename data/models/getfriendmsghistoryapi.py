# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659174e0
@llms.txt: https://napcat.apifox.cn/226659174e0.md
@last_update: 2025-05-28 01:34:10

@description: 

summary:获取好友历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_friend_msg_history"
__id__ = "226659174e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class message_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

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

class 消息详情(BaseModel):
    self_id: float = Field(description="self_id字段")
    user_id: float = Field(description="user_id字段")
    time: float = Field(description="time字段")
    message_id: float = Field(description="message_id字段")
    message_seq: float = Field(description="message_seq字段")
    real_id: float = Field(description="real_id字段")
    real_seq: str = Field(description="real_seq字段")
    message_type: str = Field(description="message_type字段")
    sender: sender = Field(description="sender字段")
    raw_message: str = Field(description="raw_message字段")
    font: float = Field(description="font字段")
    sub_type: str = Field(description="sub_type字段")
    message: list[str] = Field(description="message字段")
    message_format: str = Field(description="message_format字段")
    post_type: str = Field(description="post_type字段")
    group_id: float | None = Field(None, description="group_id字段")

    model_config = {
        "extra": "allow",
    }

class 消息forward(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

class markdown消息(BaseModel):
    type: str = Field(description="type字段")
    data: ResponseData = Field(description="data字段")

    model_config = {
        "extra": "allow",
    }

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

class 文件消息(BaseModel):
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

class sender(BaseModel):
    user_id: float = Field(description="user_id字段")
    nickname: str = Field(description="nickname字段")
    sex: str | None = Field(None, description="sex字段")
    age: float | None = Field(None, description="age字段")
    card: str = Field(description="card字段")
    role: str | None = Field(None, description="role字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetFriendMsgHistoryReq(BaseModel):
    """获取好友历史消息"""
    user_id: user_id
    message_seq: message_id | None = Field(None, description="0为最新")
    count: float | None = Field(None, description="数量")
    reverseOrder: bool | None = Field(None, description="倒序")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFriendMsgHistoryRes(BaseModel):
    """获取好友历史消息"""
    class Data(BaseModel):
        """响应数据类型"""
        messages: list[MessagesItem] = Field(default=None, description="messages字段")

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
class GetFriendMsgHistoryAPI(BaseModel):
    """get_friend_msg_history接口数据模型"""
    endpoint: str = "get_friend_msg_history"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendMsgHistoryReq
    Res: type[BaseModel] = GetFriendMsgHistoryRes

# region api/
# endregion code

