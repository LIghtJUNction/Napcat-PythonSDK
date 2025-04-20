# -*- coding: utf-8 -*-
"""
获取群系统消息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal, Any

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取群系统消息请求参数
    """
    # 无需请求参数
    pass


class InvitedRequest(BaseModel):
    """
    邀请消息数据模型
    """
    request_id: int = Field(default=0, description="请求ID")
    invitor_uin: int = Field(default=0, description="邀请者QQ号")
    invitor_nick: str = Field(default="", description="邀请者昵称")
    group_id: int = Field(default=0, description="群号")
    group_name: str = Field(default="", description="群名称")
    checked: bool = Field(default=False, description="是否已被处理")
    actor: int = Field(default=0, description="处理者QQ号，为0表示未处理")
    
    model_config = ConfigDict(
        extra="allow",
        frozen=False,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class JoinRequest(BaseModel):
    """
    入群请求数据模型
    """
    request_id: int = Field(default=0, description="请求ID")
    requester_uin: int = Field(default=0, description="请求者QQ号")
    requester_nick: str = Field(default="", description="请求者昵称")
    message: str = Field(default="", description="验证消息")
    group_id: int = Field(default=0, description="群号")
    group_name: str = Field(default="", description="群名称")
    checked: bool = Field(default=False, description="是否已被处理")
    actor: int = Field(default=0, description="处理者QQ号，为0表示未处理")
    
    model_config = ConfigDict(
        extra="allow",
        frozen=False,
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class ResponseData(BaseModel):
    """
    获取群系统消息响应数据模型
    """
    invited_requests: list[InvitedRequest] = Field(default_factory=list, description="邀请消息列表")
    join_requests: list[JoinRequest] = Field(default_factory=list, description="进群请求列表")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取群系统消息响应参数
    """
    pass


class GetGroupSystemMsgAPI(BaseHttpAPI):
    """
    获取群系统消息 API
    用于获取群聊相关的系统消息，如加群请求、邀请入群等
    接口地址: https://napcat.apifox.cn/226659151e0.md

    参数：
    {} // 无参数

    返回：
    - 群系统消息列表，包含邀请消息和进群请求详情
    """

    api: str = "/get_group_system_msg"
    method: Literal['POST', 'GET'] = "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.get_group_system_msg
    test_model(Request)
    test_model(InvitedRequest)
    test_model(JoinRequest)
    test_model(ResponseData)
    test_model(Response)