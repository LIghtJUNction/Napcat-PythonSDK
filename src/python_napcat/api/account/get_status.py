"""
获取账号状态 API
用于查询当前账号的在线状态
接口地址: https://napcat.apifox.cn/227233981e0.md

参数：
无需参数

返回：
- 在线状态、设备类型、最后在线时间等信息
"""

from typing import TypedDict
from datetime import datetime
from python_napcat.api.base.types import BaseHttpResponse

class GetStatusReq(TypedDict):
    """
    获取账号状态 API 请求参数
    """
    pass  # 无请求参数

class OnlineStatus(TypedDict):
    """
    在线状态详情
    """
    online: bool           # 是否在线
    device_type: str       # 设备类型 (手机/电脑/平板)
    last_active: datetime  # 最后活动时间

class GetStatusRes(BaseHttpResponse[OnlineStatus]):
    """
    获取账号状态 API 响应参数
    """
    pass
