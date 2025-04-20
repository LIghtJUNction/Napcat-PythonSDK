# -*- coding: utf-8 -*-
"""
群禁言 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    群禁言请求参数
    """
    group_id: int = Field(description="群号")
    user_id: int | str = Field(description="要禁言的用户ID")
    duration: int = Field(default=30 * 60, description="禁言时长，单位为秒，0表示解除禁言")


class ResponseData(BaseModel):
    """
    群禁言响应数据模型
    """
    success: bool = Field(default=False, description="是否设置成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    群禁言响应参数
    """
    pass


class SetGroupBanAPI(BaseHttpAPI):
    """
    群禁言 API
    用于禁言群内指定成员
    接口地址: https://napcat.apifox.cn/226659190e0.md

    参数：
    {
      "group_id": 123456789,
      "user_id": 987654321,
      "duration": 1800  // 禁言时长，单位为秒，0表示解除禁言
    }

    返回：
    - 设置群禁言的结果状态，包含是否成功和相关消息
    """

    api: str = "/set_group_ban"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.set_group_ban
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)