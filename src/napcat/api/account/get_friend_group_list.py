# -*- coding: utf-8 -*-
"""
获取好友分组列表 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取好友分组列表请求参数
    """
    pass  # 无需参数


class FriendGroup(BaseModel):
    """
    好友分组信息
    """
    group_id: int = Field(default=0, description="分组ID")
    group_name: str = Field(default="", description="分组名称")
    friend_count: int = Field(default=0, description="分组内好友数量")
    online_friend_count: int = Field(default=0, description="在线好友数量")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class ResponseData(BaseModel):
    """
    好友分组列表数据模型
    """
    # 使用list[FriendGroup]表示分组列表
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[list[FriendGroup]]):
    """
    获取好友分组列表响应参数
    """
    pass


class GetFriendGroupListAPI(BaseHttpAPI):
    """
    获取好友分组列表 API
    用于获取QQ好友分组列表信息
    接口地址: https://napcat.apifox.cn/226659159e0.md

    参数：
    无需参数

    返回：
    - 包含所有好友分组信息的列表，每个分组包含分组ID、名称和好友数量等信息
    """

    api: str = "/get_friend_group_list"
    method: Literal['POST', 'GET'] = "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[list[FriendGroup]] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.get_friend_group_list
    test_model(Request)
    test_model(FriendGroup)
    test_model(Response)