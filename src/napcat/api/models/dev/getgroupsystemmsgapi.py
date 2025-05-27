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
from typing import Literal
import logging

logger = logging.getLogger(__name__)

# region component_models

class 系统信息(BaseModel):
    """系统信息模型"""
    request_id: float = Field(description="请求ID")
    invitor_uin: float = Field(description="邀请者UIN")
    invitor_nick: str = Field(description="邀请者昵称")
    group_id: float = Field(description="群ID")
    message: str = Field(description="系统消息内容")
    group_name: str = Field(description="群名称")
    checked: bool = Field(description="是否已处理")
    actor: float = Field(description="处理者UIN")
    requester_nick: str = Field(description="请求者昵称")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupSystemMsgReq(BaseModel):
    """获取群系统消息请求"""
    # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupSystemMsgRes(BaseModel):
    """获取群系统消息响应"""
    class Data(BaseModel):
        """响应数据类型"""
        InvitedRequest: list[系统信息] = Field(default_factory=list, description="被邀请请求列表")
        join_requests: list[系统信息] = Field(default_factory=list, description="加入请求列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: float = Field(description="返回码")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field(default="", description="消息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显数据")

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
