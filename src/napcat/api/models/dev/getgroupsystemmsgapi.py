# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658660e0
@llms.txt: https://napcat.apifox.cn/226658660e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_system_msg"
__id__ = "226658660e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupSystemMsgReq(BaseModel):
    """
    获取群系统消息请求模型
    """
    group_id: str | int = Field(..., description="群号")

# endregion req



# region res

class InvitedRequestItem(BaseModel):
    """
    被邀请入群请求项
    """
    request_id: str = Field(..., description="请求ID")
    invitor_uin: str = Field(..., description="邀请者QQ号")
    invitor_nick: str = Field(..., description="邀请者昵称")
    group_id: str = Field(..., description="群号")
    group_name: str = Field(..., description="群名")
    checked: bool = Field(..., description="是否已处理")
    actor: str | int = Field(..., description="处理者QQ号") # Note: The OpenAPI spec has actor as string or number, but common usage is QQ number which can be string or number. Assuming it's the processing bot/user QQ.

class JoinRequestItem(BaseModel):
    """
    加群请求项
    """
    request_id: str = Field(..., description="请求ID")
    requester_uin: str = Field(..., description="申请者QQ号")
    requester_nick: str = Field(..., description="申请者昵称")
    group_id: str = Field(..., description="群号")
    group_name: str = Field(..., description="群名")
    checked: bool = Field(..., description="是否已处理")
    actor: str | int = Field(..., description="处理者QQ号") # Similar assumption as InvitedRequestItem


class GetGroupSystemMsgResData(BaseModel):
    """
    获取群系统消息响应数据模型
    """
    InvitedRequest: list[InvitedRequestItem] = Field(..., description="被邀请入群请求列表")
    join_requests: list[JoinRequestItem] = Field(..., description="加群请求列表")


class GetGroupSystemMsgRes(BaseModel):
    """
    获取群系统消息响应模型
    """
    status: str = Field(..., description="响应状态") # Should be 'ok' according to spec
    retcode: int = Field(..., description="响应码")
    data: GetGroupSystemMsgResData = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="回显") # Nullable

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
