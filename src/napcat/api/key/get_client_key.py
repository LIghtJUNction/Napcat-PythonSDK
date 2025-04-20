# -*- coding: utf-8 -*-
"""
获取Client Key API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取Client Key请求参数
    """
    pass  # 无需参数


class ResponseData(BaseModel):
    """
    Client Key响应数据模型
    """
    client_key: str = Field(default="", description="客户端密钥字符串")
    expires_in: int = Field(default=0, description="密钥有效期(秒)")
    created_at: int = Field(default=0, description="创建时间戳")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取Client Key响应参数
    """
    pass


class GetClientKeyAPI(BaseHttpAPI):
    """
    获取Client Key API
    用于获取客户端密钥，此密钥用于身份验证和部分敏感操作
    接口地址: https://napcat.apifox.cn/250286915e0.md

    参数：
    无需参数

    返回：
    - 包含clientkey的对象，用于后续API调用的身份验证
    """

    api: str = "/get_client_key"
    method: Literal['POST', 'GET'] = "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.key.get_client_key
    test_model(Request)
    test_model(ResponseData)
    test_model(Response)