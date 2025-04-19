"""
获取登录信息 API
用于获取当前登录的QQ账号基本信息
接口地址: https://napcat.apifox.cn/227233981e0.md

参数：
无需参数

返回：
- 用户ID、昵称、等级等基础信息
"""

from typing import TypedDict
from python_napcat.api.base.types import BaseHttpResponse

class LoginInfoReq(TypedDict):
    """
    获取登录信息 API 请求参数
    """
    pass  # 无请求参数

class UserBasicInfo(TypedDict):
    """
    用户基础信息
    """
    user_id: int     # QQ号码
    nickname: str    # 昵称
    level: int       # QQ等级
    vip_type: int    # VIP类型

class GetLoginInfoRes(BaseHttpResponse[UserBasicInfo]):
    """
    获取登录信息 API 响应参数
    """
    pass
