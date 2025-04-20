"""
获取CSRF Token API
用于获取CSRF令牌，此令牌用于防止跨站请求伪造攻击，保证API请求的安全性
接口地址: https://napcat.apifox.cn/226657044e0.md

参数：
无需参数

返回：
- 包含CSRF令牌的对象，此令牌在执行修改操作的API调用中必须提供

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetCsrfTokenReq(TypedDict):
    """
    获取CSRF Token API 请求参数
    """
    pass  # 无请求参数

class CsrfTokenData(TypedDict):
    """
    CSRF令牌数据
    """
    token: str           # CSRF令牌字符串
    expires_in: int      # 令牌有效期(秒)
    created_at: int      # 创建时间戳

class GetCsrfTokenRes(BaseHttpResponse[CsrfTokenData]):
    """
    获取CSRF Token API 响应参数
    """
    pass