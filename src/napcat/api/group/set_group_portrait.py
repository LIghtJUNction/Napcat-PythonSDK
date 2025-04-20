# -*- coding: utf-8 -*-
"""
设置群头像 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置群头像请求参数
    """
    group_id: int = Field(description="群号")
    file: str = Field(description="图片文件路径或URL地址")
    cache: bool = Field(default=True, description="是否使用已缓存的文件，默认为true")
    is_base64: bool = Field(default=False, description="是否为base64编码的图片，默认为false")


class ResponseData(BaseModel):
    """
    设置群头像响应数据模型
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
    设置群头像响应参数
    """
    pass


class SetGroupPortraitAPI(BaseHttpAPI):
    """
    设置群头像 API
    用于修改群聊的头像
    接口地址: https://napcat.apifox.cn/226659190e0.md

    参数：
    {
      "group_id": 123456789,
      "file": "https://example.com/image.jpg", // 或本地路径 /path/to/image.jpg
      "cache": true,  // 是否使用已缓存的文件，默认为true
      "is_base64": false  // 是否为base64编码的图片，默认为false
    }

    返回：
    - 设置群头像的结果状态，包含是否成功和相关消息
    """

    api: str = "/set_group_portrait"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.set_group_portrait
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)