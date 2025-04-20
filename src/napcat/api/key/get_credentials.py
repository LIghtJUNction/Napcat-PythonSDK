"""
获取QQ相关接口凭证 API
用于获取QQ相关接口的身份验证凭证，这些凭证用于访问QQ相关的API服务
接口地址: https://napcat.apifox.cn/226657054e0.md

参数：
无需参数

返回：
- 包含QQ接口凭证的对象，可用于调用QQ相关API

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetCredentialsReq(TypedDict):
    """
    获取QQ相关接口凭证 API 请求参数
    """
    pass  # 无请求参数

class CredentialsData(TypedDict):
    """
    接口凭证数据
    """
    skey: str                     # S密钥
    pskey: str                    # P密钥
    superkey: str                 # 超级密钥
    pt4_token: str                # PT4令牌
    access_token: str             # 访问令牌
    refresh_token: str            # 刷新令牌
    domains: dict[str, str]       # 不同域名的凭证映射

class GetCredentialsRes(BaseHttpResponse[CredentialsData]):
    """
    获取QQ相关接口凭证 API 响应参数
    """
    pass