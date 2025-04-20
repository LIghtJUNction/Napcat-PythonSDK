"""
获取登录号信息 API
用于获取当前登录的QQ账号信息
接口地址: https://napcat.apifox.cn/226964801e0.md

参数：
无需参数

返回：
- 当前登录账号的信息，包括QQ号和昵称

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.types import BaseHttpResponse
# region TypedDicts
class GetLoginInfoReq(TypedDict):
    """
    获取登录号信息 API 请求参数
    """
    pass  # 无需参数

class LoginInfo(TypedDict):
    """
    登录账号信息
    """
    user_id: int  # QQ号
    nickname: str  # 昵称

class GetLoginInfoRes(BaseHttpResponse[LoginInfo]):
    """
    获取登录号信息 API 响应参数
    """
    pass
