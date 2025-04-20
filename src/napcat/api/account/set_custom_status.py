# -*- coding: utf-8 -*-
"""
设置自定义在线状态 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置自定义在线状态请求参数
    """
    status_text: str = Field(description="自定义状态文本")
    emoji_id: str | None = Field(default=None, description="状态表情ID(可选)")
    emoji_url: str | None = Field(default=None, description="表情URL(可选)")
    duration: int | None = Field(default=None, description="显示持续时间，单位秒，不设置则为永久(可选)")


class ResponseData(BaseModel):
    """
    设置自定义在线状态响应数据模型
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
    设置自定义在线状态响应参数
    """
    pass


class SetCustomStatusAPI(BaseHttpAPI):
    """
    设置自定义在线状态 API
    用于设置当前账号的自定义在线状态
    接口地址: https://napcat.apifox.cn/226659198e0.md

    参数：
    {
      "status_text": "正在学习Python",
      "emoji_id": "128218",  // 可选
      "emoji_url": "https://example.com/emoji.png",  // 可选
      "duration": 3600  // 可选，单位秒，不设置则为永久
    }

    返回：
    - 设置自定义在线状态的结果信息，包含是否成功和相关消息
    """

    api: str = "/set_custom_status"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.set_custom_status
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)