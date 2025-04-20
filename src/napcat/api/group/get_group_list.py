# -*- coding: utf-8 -*-
"""
获取群列表 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取群列表请求参数
    """
    no_cache: bool = Field(default=False, description="是否不使用缓存，默认为False")


class GroupInfo(BaseModel):
    """
    群信息数据模型
    """
    group_id: int = Field(default=0, description="群号")
    group_name: str = Field(default="", description="群名称")
    member_count: int = Field(default=0, description="成员数量")
    max_member_count: int = Field(default=0, description="最大成员数量")
    owner_id: int | str = Field(default="", description="群主ID")
    admin_flag: bool = Field(default=False, description="是否为管理员")
    owner_flag: bool = Field(default=False, description="是否为群主")
    create_time: int = Field(default=0, description="创建时间")
    level: int = Field(default=0, description="群等级")
    avatar: str = Field(default="", description="群头像URL")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[list[GroupInfo]]):
    """
    获取群列表响应参数
    """
    pass


class GetGroupListAPI(BaseHttpAPI):
    """
    获取群列表 API
    用于获取当前登录账号加入的群列表
    接口地址: https://napcat.apifox.cn/226659184e0.md

    参数：
    {
      "no_cache": false
    }

    返回：
    - 群列表，包含群号、群名称、成员数量等信息
    """

    api: str = "/get_group_list"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[list[GroupInfo]] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.get_group_list
    test_model(Request)
    test_model(GroupInfo)
    test_model(Response)