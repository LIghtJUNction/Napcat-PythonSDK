"""
设置个性签名 API
用于设置当前登录账号的个性签名
接口地址: https://napcat.apifox.cn/226659186e0.md

参数：
- content: 要设置的个性签名内容，支持文本和特殊符号
- cookie: Cookie信息(可选)

返回：
- 设置个性签名的结果信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class SetSelfLongnickReq(TypedDict):
    """
    设置个性签名 API 请求参数
    """
    content: str              # 要设置的个性签名内容
    cookie: str | None     # Cookie信息(可选)

class LongnickResult(TypedDict):
    """
    设置个性签名的结果信息
    """
    success: bool            # 是否设置成功
    message: str             # 结果消息

class SetSelfLongnickRes(BaseHttpResponse[LongnickResult]):
    """
    设置个性签名 API 响应参数
    """
    pass