# -*- coding: utf-8 -*-
"""
获取版本信息 API
开发完毕
@作者：GitHub Copilot
@日期：2025/04/20
"""

from typing import Literal

from pydantic import ConfigDict, Field
from ..base.models import BaseHttpAPI, BaseHttpRequest, BaseHttpResponse, BaseModel


class Request(BaseHttpRequest):
    """
    获取版本信息请求参数
    """
    pass  # 无需参数


class VersionInfo(BaseModel):
    """
    版本详细信息
    """
    name: str = Field(default="", description="应用名称")
    version: str = Field(default="", description="版本号")
    build_time: str = Field(default="", description="构建时间")
    repository: str = Field(default="", description="代码仓库地址")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class ImplementInfo(BaseModel):
    """
    实现信息
    """
    name: str = Field(default="", description="实现名称")
    version: str = Field(default="", description="实现版本")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class ResponseData(BaseModel):
    """
    版本信息响应数据模型
    """
    app: VersionInfo = Field(default_factory=VersionInfo, description="应用版本信息")
    protocol: VersionInfo = Field(default_factory=VersionInfo, description="协议版本信息")
    implements: list[ImplementInfo] = Field(default_factory=list, description="实现信息列表")
    
    model_config = ConfigDict(
        extra="allow",  # 允许额外字段
        frozen=False,   # 不冻结模型
        populate_by_name=True,  # 通过名称填充字段
        arbitrary_types_allowed=True,  # 允许任意类型
    )


class Response(BaseHttpResponse[ResponseData]):
    """
    获取版本信息响应参数
    """
    pass


class GetVersionInfoAPI(BaseHttpAPI):
    """
    获取版本信息 API
    用于获取当前Napcat实例的版本信息和协议信息
    接口地址: https://napcat.apifox.cn/227493562e0.md

    参数：
    无需参数

    返回：
    - 包含应用版本、协议版本和实现信息的详细数据
    """

    api: str = "/get_version_info"
    method: Literal['POST', 'GET'] = "GET"
    request: BaseHttpRequest = Request()
    response: BaseHttpResponse[ResponseData] = Response()

if __name__ == "__main__":
    from ..base.utils import test_model
    # uv pip install -e . 
    # python -m napcat.api.system.get_version_info
    test_model(Request)
    test_model(VersionInfo)
    test_model(ImplementInfo)
    test_model(ResponseData)
    test_model(Response)