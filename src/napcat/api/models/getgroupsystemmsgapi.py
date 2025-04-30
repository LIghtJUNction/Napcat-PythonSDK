# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226658660e0
@llms.txt: https://napcat.apifox.cn/226658660e0.md
@last_update: 2025-04-27 00:53:40

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
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


# region models
class SystemMessageItem(BaseModel):
    """系统信息模型"""
    request_id: int = Field(..., description="请求ID")
    invitor_uin: int = Field(..., description="邀请者QQ号")
    invitor_nick: str = Field(..., description="邀请者昵称")
    group_id: int = Field(..., description="群号")
    message: str = Field(..., description="请求消息")
    group_name: str = Field(..., description="群名")
    checked: bool = Field(..., description="是否已处理")
    actor: int = Field(..., description="处理者QQ号 (如果已处理)")
    requester_nick: str = Field(..., description="申请者昵称")


class GetGroupSystemMsgResData(BaseModel):
    """获取群系统消息响应数据模型"""
    InvitedRequest: list[SystemMessageItem] = Field(..., description="收到的邀请入群列表")
    join_requests: list[SystemMessageItem] = Field(..., description="收到的加群请求列表")

# endregion models


# region req
class GetGroupSystemMsgReq(BaseModel):
    """
    获取群系统消息的请求模型
    """
    pass
# endregion req



# region res
class GetGroupSystemMsgRes(BaseModel):
    """
    获取群系统消息的响应模型
    """
    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(..., description="状态码")
    data: GetGroupSystemMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class GetGroupSystemMsgAPI(BaseModel):
    """get_group_system_msg接口数据模型"""
    endpoint: str = "get_group_system_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupSystemMsgReq
    Res: type[BaseModel] = GetGroupSystemMsgRes
# endregion api




# endregion code