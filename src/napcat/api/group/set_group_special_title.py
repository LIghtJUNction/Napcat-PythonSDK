# -*- coding: utf-8 -*-
"""
设置群头衔 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    设置群头衔请求参数
    """
    group_id: int = Field(description="群号")
    user_id: int | str = Field(description="要设置的成员QQ号")
    special_title: str = Field(description="专属头衔，不填或空字符串表示清除专属头衔")
    duration: int = Field(default=-1, description="专属头衔有效期，单位秒，-1表示永久，0表示取消")


class ResponseData(BaseModel):
    """
    设置群头衔响应数据模型
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
    设置群头衔响应参数
    """
    pass


class SetGroupSpecialTitleAPI(BaseHttpAPI):
    """
    设置群头衔 API
    用于设置群成员专属头衔
    接口地址: https://napcat.apifox.cn/226659187e0.md

    参数：
    {
      "group_id": 123456789,
      "user_id": 987654321,
      "special_title": "测试头衔",  // 专属头衔，不填或空字符串表示清除专属头衔
      "duration": -1  // 专属头衔有效期，单位秒，-1表示永久，0表示取消
    }

    返回：
    - 设置群头衔的结果状态，包含是否成功和相关消息
    """

    api: str = "/set_group_special_title"
    method: Literal['POST', 'GET'] = "POST"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.group.set_group_special_title
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)