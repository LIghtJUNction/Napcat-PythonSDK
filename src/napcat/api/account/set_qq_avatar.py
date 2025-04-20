# -*- coding: utf-8 -*-
"""
设置头像 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置头像请求参数
    """
    file: str = Field(description="头像图片文件路径，支持本地文件路径或图片URL")
    cache: bool = Field(default=True, description="是否使用缓存，默认为true")


class ResponseData(BaseModel):
    """
    设置头像响应数据模型
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
    设置头像响应参数
    """
    pass


class SetQQAvatarAPI(BaseHttpAPI):
    """
    设置头像 API
    用于设置当前账号的个人头像
    接口地址: https://napcat.apifox.cn/226657373e0.md

    参数：
    {
      "file": "C:/Users/Admin/Pictures/avatar.jpg",  // 或 "http://example.com/avatar.jpg"
      "cache": true
    }

    返回：
    - 设置头像的结果状态，包含是否成功和相关消息
    """

    api: str = "/set_qq_avatar"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.set_qq_avatar
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)