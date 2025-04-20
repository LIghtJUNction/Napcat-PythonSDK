# -*- coding: utf-8 -*-
"""
设置群成员名片 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置群成员名片请求参数
    """
    group_id: int = Field(description="群号")
    user_id: int | str = Field(description="要设置的成员QQ号")
    card: str = Field(description="新的群名片内容，设置为空字符串表示清除群名片")


class ResponseData(BaseModel):
    """
    设置群成员名片响应数据模型
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
    设置群成员名片响应参数
    """
    pass


class SetGroupCardAPI(BaseHttpAPI):
    """
    设置群成员名片 API
    用于设置群成员在群内显示的昵称
    接口地址: https://napcat.apifox.cn/226659185e0.md

    参数：
    {
      "group_id": 123456789,
      "user_id": 987654321,
      "card": "新名片"  // 群名片内容，不填或空字符串表示清除群名片
    }

    返回：
    - 设置群成员名片的结果状态，包含是否成功和相关消息
    """

    api: str = "/set_group_card"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.set_group_card
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)