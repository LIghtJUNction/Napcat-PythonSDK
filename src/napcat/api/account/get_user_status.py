# -*- coding: utf-8 -*-
"""
获取用户状态 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取用户状态请求参数
    """
    user_id: int = Field(description="要查询的用户QQ号")


class UserStatus(BaseModel):
    """
    用户状态信息
    """
    online: bool = Field(default=False, description="是否在线")
    status: str = Field(default="", description="在线状态类型")
    client_type: int = Field(default=0, description="客户端类型")
    device_name: str = Field(default="", description="设备名称")
    custom_status: str = Field(default="", description="自定义状态")
    online_time: int = Field(default=0, description="在线时长（秒）")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class ResponseData(BaseModel):
    """
    用户状态响应数据模型
    """
    user_id: int = Field(default=0, description="查询的用户QQ号")
    nickname: str = Field(default="", description="用户昵称")
    status: UserStatus = Field(default_factory=UserStatus, description="用户状态信息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取用户状态响应参数
    """
    pass


class GetUserStatusAPI(BaseHttpAPI):
    """
    获取用户状态 API
    用于获取指定QQ用户的在线状态
    接口地址: https://napcat.apifox.cn/226659292e0.md

    参数：
    {
      "user_id": 123456789  // 要查询的用户QQ号
    }

    返回：
    - 用户在线状态信息，包括是否在线、在线类型、设备信息等
    """

    api: str = "/get_user_status"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.get_user_status
    test_model(Request)
    test_model(UserStatus)
    test_model(ResponseData)
    test_model(Response)