# -*- coding: utf-8 -*-
"""
处理好友请求 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    处理好友请求参数
    """
    flag: str = Field(description="好友请求的标识，收到的请求事件数据中的flag字段")
    approve: bool = Field(default=True, description="是否同意请求，默认为true")
    remark: str = Field(default="", description="备注，仅在同意添加好友时有效")


class ResponseData(BaseModel):
    """
    处理好友请求响应数据模型
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
    处理好友请求响应参数
    """
    pass


class SetFriendAddRequestAPI(BaseHttpAPI):
    """
    处理好友请求 API
    用于处理他人申请添加自己为好友的请求
    接口地址: https://napcat.apifox.cn/226659173e0.md

    参数：
    {
      "flag": "12345678",  // 好友请求的标识
      "approve": true,     // 是否同意请求
      "remark": "备注名"    // 备注，仅在同意添加好友时有效
    }

    返回：
    - 处理好友请求的结果状态，包含是否成功和相关消息
    """

    api: str = "/set_friend_add_request"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.account.set_friend_add_request
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)