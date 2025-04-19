"""
设置所有消息已读 API
用于将所有未读消息（包括私聊和群聊）标记为已读状态
接口地址: https://napcat.apifox.cn/226659194e0.md

参数：
无需参数

返回：
- 设置所有消息已读的结果信息

# NapCat 开发中
"""

from typing import TypedDict
from python_napcat.api.base.types import BaseHttpResponse

class MarkAllAsReadReq(TypedDict):
    """
    设置所有消息已读的请求参数
    空字典表示不需要任何参数
    """
    pass

class MarkAllAsReadRes(BaseHttpResponse[None]):
    """
    设置所有消息已读的结果信息
    """
    pass
