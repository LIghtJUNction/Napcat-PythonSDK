"""
获取用户在线状态 API
用于获取指定QQ用户的在线状态信息
接口地址: https://napcat.apifox.cn/227232854e0.md

参数：
- user_id: 要查询的用户QQ号

返回：
- 用户的在线状态、使用的客户端类型等信息

# NapCat 开发中
"""

from typing import TypedDict
from datetime import datetime
from napcat.api.base.models import BaseHttpResponse

class NcGetUserStatusReq(TypedDict):
    """
    获取用户在线状态 API 请求参数
    """
    user_id: int               # 要查询的用户QQ号

class ClientInfo(TypedDict):
    """
    客户端信息
    """
    client_type: str           # 客户端类型（如手机、电脑等）
    client_name: str           # 客户端名称
    device_name: str | None # 设备名称
    version: str | None     # 客户端版本号

class UserStatusInfo(TypedDict):
    """
    用户在线状态信息
    """
    user_id: int                    # 用户QQ号
    online: bool                    # 是否在线
    status_type: int                # 状态类型码
    status_text: str                # 状态文本描述
    last_active: datetime           # 最后活跃时间
    clients: list[ClientInfo]       # 用户登录的客户端列表

class NcGetUserStatusRes(BaseHttpResponse[UserStatusInfo]):
    """
    获取用户在线状态 API 响应参数
    """
    pass