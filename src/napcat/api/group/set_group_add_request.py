# -*- coding: utf-8 -*-
"""
处理加群请求 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    处理加群请求参数
    """
    flag: str = Field(description="加群请求的标识，收到的请求事件数据中的flag字段")
    sub_type: str = Field(default="add", description="请求类型，add或invite，默认为add")
    approve: bool = Field(default=True, description="是否同意请求，默认为true")
    reason: str = Field(default="", description="拒绝理由，仅在拒绝时有效")


class ResponseData(BaseModel):
    """
    处理加群请求响应数据模型
    """
    success: bool = Field(default=False, description="是否处理成功")
    message: str = Field(default="", description="结果消息")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    处理加群请求响应参数
    """
    pass


class SetGroupAddRequestAPI(BaseHttpAPI):
    """
    处理加群请求 API
    用于处理他人申请加群或被邀请加群的请求
    接口地址: https://napcat.apifox.cn/226659210e0.md

    参数：
    {
      "flag": "12345678",  // 加群请求的标识
      "sub_type": "add",   // 请求类型，add或invite
      "approve": true,     // 是否同意请求
      "reason": ""         // 拒绝理由，仅在拒绝时有效
    }

    返回：
    - 处理加群请求的结果状态，包含是否成功和相关消息
    """

    api: str = "/set_group_add_request"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.set_group_add_request
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)