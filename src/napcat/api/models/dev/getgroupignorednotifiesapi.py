# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659323e0
@llms.txt: https://napcat.apifox.cn/226659323e0.md
@last_update: 2025-05-28 01:34:10

@description:

summary:获取群过滤系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_ignored_notifies"
__id__ = "226659323e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
class Result(BaseModel):
    status: Literal["ok"] = Field("ok", description="Status of the operation, typically 'ok' for success.")
    retcode: float = Field(0.0, description="Return code indicating the result of the operation.")
    data: dict = Field(default_factory=dict, description="Generic data payload for the result.")
    message: str = Field("", description="A descriptive message about the operation's result.")
    wording: str = Field("", description="User-friendly wording for the operation's result.")
    echo: str | None = Field(None, description="Optional echo field for request correlation.")

    model_config = {
        "extra": "allow",
    }

class SystemInfo(BaseModel):
    request_id: float = Field(description="Request ID for the system message.")
    invitor_uin: float = Field(description="UIN of the invitor.")
    invitor_nick: str = Field(description="Nickname of the invitor.")
    group_id: float = Field(description="ID of the group.")
    message: str = Field(description="The content of the system message.")
    group_name: str = Field(description="Name of the group.")
    checked: bool = Field(description="Indicates if the message has been checked.")
    actor: float = Field(description="Actor UIN involved in the message.")
    requester_nick: str = Field(description="Nickname of the requester.")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupIgnoredNotifiesReq(BaseModel):
    """获取群过滤系统消息请求模型"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupIgnoredNotifiesRes(BaseModel):
    """获取群过滤系统消息响应模型"""
    class Data(BaseModel):
        """响应数据类型"""
        InvitedRequest: list[SystemInfo] = Field([], description="List of invited requests.")
        join_requests: list[SystemInfo] = Field([], description="List of join requests.")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="Status of the operation, typically 'ok' for success.")
    retcode: float = Field(0.0, description="Return code indicating the result of the operation.")
    data: Data = Field(default_factory=Data, description="Detailed data payload for the response.")
    message: str = Field("", description="A descriptive message about the operation's result.")
    wording: str = Field("", description="User-friendly wording for the operation's result.")
    echo: str | None = Field(None, description="Optional echo field for request correlation.")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupIgnoredNotifiesAPI(BaseModel):
    """get_group_ignored_notifies接口数据模型"""
    endpoint: str = "get_group_ignored_notifies"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupIgnoredNotifiesReq
    Res: type[BaseModel] = GetGroupIgnoredNotifiesRes

# region api/
# endregion code
