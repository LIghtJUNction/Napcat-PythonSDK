"""
NapcatClient功能：统一的Napcat客户端接口，集成HTTP、SSE、WebSocket功能
"""
from __future__ import annotations

import logging
from types import TracebackType
from typing import Any
from collections.abc import AsyncGenerator, Callable, Awaitable

from pydantic import BaseModel

from .http import AsyncHttpClient, HttpClient
from .sse import AsyncSSEClient
from .websocket import NapcatWebsocketClient

logger = logging.getLogger("napcat.client")


class NapcatClient:
    """
    统一的Napcat客户端，集成多种通信方式
    """
    
    def __init__(
        self,
        base_url: str,
        token: str,
        timeout: float = 60.0,
        debug: bool = False,
    ):
        """
        初始化Napcat客户端
        
        Args:
            base_url: API基础URL
            token: 认证令牌
            timeout: 请求超时时间（秒）
            debug: 是否启用调试模式
        """
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.timeout = timeout
        self.debug = debug
        
        # 初始化各种客户端（懒加载）
        self._http_client: HttpClient | None = None
        self._async_http_client: AsyncHttpClient | None = None
        self._sse_client: AsyncSSEClient | None = None
        self._websocket_client: NapcatWebsocketClient | None = None
        
        logger.info(f"初始化Napcat客户端: {self.base_url}")
    
    # region HTTP客户端
    @property
    def http(self) -> HttpClient:
        """获取同步HTTP客户端"""
        if self._http_client is None:
            self._http_client = HttpClient(
                base_url=self.base_url,
                token=self.token,
                timeout=self.timeout,
                debug=self.debug
            )
        return self._http_client
    
    @property
    def async_http(self) -> AsyncHttpClient:
        """获取异步HTTP客户端"""
        if self._async_http_client is None:
            self._async_http_client = AsyncHttpClient(
                base_url=self.base_url,
                token=self.token,
                timeout=self.timeout,
                debug=self.debug
            )
        return self._async_http_client
    
    def send(self, api_class: type, request_data: BaseModel) -> BaseModel:
        """同步发送HTTP请求"""
        return self.http.send(api_class, request_data)
    
    async def async_send(self, api_class: type, request_data: BaseModel) -> BaseModel:
        """异步发送HTTP请求"""
        return await self.async_http.send(api_class, request_data)
    # endregion
    
    # region SSE客户端
    @property
    def sse(self) -> AsyncSSEClient:
        """获取SSE客户端"""
        if self._sse_client is None:
            self._sse_client = AsyncSSEClient(
                base_url=self.base_url,
                token=self.token,
                timeout=self.timeout
            )
        return self._sse_client
    
    async def sse_connect(
        self,
        endpoint: str,
        response_model: type[BaseModel] | None = None,
        **kwargs: Any
    ) -> AsyncGenerator[BaseModel | dict[str, Any]]:
        """连接到SSE端点"""
        async for event in self.sse.connect(endpoint, response_model, **kwargs):
            yield event
    
    async def sse_subscribe(
        self,
        endpoint: str,
        callback: Callable[[BaseModel | dict[str, Any]], Any],
        response_model: type[BaseModel] | None = None,
        **kwargs: Any
    ) -> None:
        """订阅SSE端点"""
        await self.sse.subscribe(endpoint, callback, response_model, **kwargs)
    # endregion
    
    # region WebSocket客户端
    @property
    def websocket(self) -> NapcatWebsocketClient:
        """获取WebSocket客户端"""
        if self._websocket_client is None:
            # 将HTTP URL转换为WebSocket URL
            ws_url = self.base_url.replace('http://', 'ws://').replace('https://', 'wss://')
            self._websocket_client = NapcatWebsocketClient(
                base_uri=ws_url,
                token=self.token
            )
        return self._websocket_client
    
    async def ws_connect(
        self,
        message_handler: Callable[[str], Awaitable[Any]] | None = None,
        error_handler: Callable[[Exception], Awaitable[Any]] | None = None,
    ) -> None:
        """连接WebSocket"""
        await self.websocket.connect(message_handler, error_handler)
    
    async def ws_send(self, message: str) -> None:
        """发送WebSocket消息"""
        await self.websocket.send(message)
    
    async def ws_disconnect(self) -> None:
        """断开WebSocket连接"""
        await self.websocket.disconnect()
    # endregion
    
    # region 资源管理
    def close(self) -> None:
        """关闭所有客户端连接"""
        if self._http_client:
            self._http_client.close()
            self._http_client = None
        
        logger.info("所有客户端连接已关闭")
    
    async def async_close(self) -> None:
        """异步关闭所有客户端连接"""
        if self._async_http_client:
            await self._async_http_client.close()
            self._async_http_client = None
        
        if self._sse_client:
            await self._sse_client.close()
            self._sse_client = None
        
        if self._websocket_client:
            await self._websocket_client.disconnect()
            self._websocket_client = None
        
        logger.info("所有异步客户端连接已关闭")
    
    def __enter__(self) -> "NapcatClient":
        return self
    
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        self.close()
    
    async def __aenter__(self) -> "NapcatClient":
        return self
    
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        await self.async_close()
    # endregion