"""
获取在线客户端 API
用于获取当前账号在线的客户端列表信息
接口地址: https://napcat.apifox.cn/226657379e0.md

参数：
- no_cache: 是否不使用缓存(可选)

返回：
- 包含当前账号所有在线客户端信息的列表，包括设备类型、设备名称、登录IP和在线状态等

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetOnlineClientsReq(TypedDict, total=False):
    """
    获取在线客户端 API 请求参数
    """
    no_cache: bool  # 是否不使用缓存

class ClientInfo(TypedDict):
    """
    客户端信息
    """
    app_id: str        # 客户端ID
    device_name: str   # 设备名称
    device_kind: str   # 设备类型
    login_time: int    # 登录时间戳
    ip_address: str    # 登录IP地址
    status: str        # 在线状态

class GetOnlineClientsRes(BaseHttpResponse[list[ClientInfo]]):
    """
    获取在线客户端 API 响应参数
    """
    pass