"""
获取cookies API
用于获取会话Cookie信息，这些信息在与服务器交互时用于维持用户会话状态
接口地址: https://napcat.apifox.cn/226657041e0.md

参数：
无需参数

返回：
- 包含当前会话cookies的对象，可用于其他需要身份验证的API调用

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetCookiesReq(TypedDict):
    """
    获取cookies API 请求参数
    """
    pass  # 无请求参数

class CookieInfo(TypedDict):
    """
    单个Cookie信息
    """
    name: str           # Cookie名称
    value: str          # Cookie值
    domain: str         # 所属域名
    path: str           # 路径
    expires: int        # 过期时间戳
    httpOnly: bool      # 是否仅HTTP访问
    secure: bool        # 是否只在HTTPS下传输

class CookiesData(TypedDict):
    """
    Cookies数据
    """
    cookies: dict[str, CookieInfo]  # 所有Cookie的映射
    raw_cookie_str: str             # 原始Cookie字符串

class GetCookiesRes(BaseHttpResponse[CookiesData]):
    """
    获取cookies API 响应参数
    """
    pass