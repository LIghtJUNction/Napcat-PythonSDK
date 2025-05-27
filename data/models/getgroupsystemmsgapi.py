# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658660e0
@llms.txt: https://napcat.apifox.cn/226658660e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_system_msg"
__id__ = "226658660e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
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

class 系统信息(BaseModel):
    request_id: float = Field(description="request_id字段")
    invitor_uin: float = Field(description="invitor_uin字段")
    invitor_nick: str = Field(description="invitor_nick字段")
    group_id: float = Field(description="group_id字段")
    message: str = Field(description="message字段")
    group_name: str = Field(description="group_name字段")
    checked: bool = Field(description="checked字段")
    actor: float = Field(description="actor字段")
    requester_nick: str = Field(description="requester_nick字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupSystemMsgReq(BaseModel):
    """获取群系统消息"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupSystemMsgRes(BaseModel):
    """获取群系统消息"""
    class Data(BaseModel):
        """响应数据类型"""
        InvitedRequest: list[系统信息] = Field(default=None, description="InvitedRequest字段")
        join_requests: list[系统信息] = Field(default=None, description="join_requests字段")

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
class GetGroupSystemMsgAPI(BaseModel):
    """get_group_system_msg接口数据模型"""
    endpoint: str = "get_group_system_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupSystemMsgReq
    Res: type[BaseModel] = GetGroupSystemMsgRes

# region api/
# endregion code

