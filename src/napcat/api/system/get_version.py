"""
获取版本信息 API
用于获取NapCat的版本信息
接口地址: https://napcat.apifox.cn/227230496e0.md

参数：
无需参数

返回：
- NapCat版本信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.types import BaseHttpResponse

class GetVersionReq(TypedDict):
    """
    获取版本信息 API 请求参数
    """
    pass  # 无需参数

class VersionInfo(TypedDict):
    """
    版本信息
    """
    app_name: str      # 应用名称
    app_version: str   # 应用版本号
    protocol_version: str  # 协议版本号

class GetVersionRes(BaseHttpResponse[VersionInfo]):
    """
    获取版本信息 API 响应参数
    """
    pass