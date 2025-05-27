"""
SSE客户端模块
提供Server-Sent Events事件流客户端实现
"""

from .v1 import AsyncSSEClient

__all__ = [
    "AsyncSSEClient",
]