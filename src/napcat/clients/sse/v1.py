from collections.abc import AsyncGenerator, Callable
import httpx
import json
import asyncio
from typing import Any, TypeVar

from types import TracebackType
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class AsyncSSEClient:
    """
    SSE（Server-Sent Events）客户端，处理与API的服务器推送事件通信，
    支持Pydantic模型的序列化和反序列化。
    """
    def __init__(
        self,
        base_url: str,
        token: str,
        timeout: float = 60.0,
    ):
        """
        初始化SSE客户端
        
        Args:
            base_url: API基础URL
            token: 认证令牌
            timeout: 连接超时时间（秒）
        """
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.timeout = timeout
        self._client = None
    
    def _get_headers(self) -> dict[str, str]:
        """获取请求头，包括认证信息"""
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    
    @property
    def client(self) -> httpx.AsyncClient:
        """懒加载异步HTTP客户端实例"""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                headers=self._get_headers(),
            )
        return self._client
    
    async def close(self) -> None:
        """关闭SSE客户端连接"""
        if self._client is not None:
            await self._client.aclose()
            self._client = None
    
    async def __aenter__(self) -> "AsyncSSEClient":
        return self
    
    async def __aexit__(
        self, 
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None:
        await self.close()
        
    @staticmethod
    def _parse_sse_line(line: str) -> dict[str, str] | None:
        """解析SSE事件行"""
        if not line or line.startswith(':'):
            return None
            
        if ':' not in line:
            return {line: ''}
            
        field, value = line.split(':', 1)
        if value.startswith(' '):
            value = value[1:]
        
        return {field: value}
    
    async def _process_sse_stream(
        self, 
        response: httpx.Response,
        model: type[T] | None = None
    ) -> AsyncGenerator[T | dict[str, Any]]:
        """处理SSE响应流"""
        event_data = ""
        event_id = None
        event_type = None
        
        async for line in response.aiter_lines():
            line = line.rstrip('\n')
            
            if not line:  # 空行表示事件结束
                if event_data:
                    try:
                        data = json.loads(event_data)
                        if model:
                            yield model.model_validate(data)
                        else:
                            yield data
                    except json.JSONDecodeError:
                        # 非JSON数据，返回原始文本
                        yield {"data": event_data, "id": event_id, "event": event_type}
                    
                    # 重置事件数据
                    event_data = ""
                    event_id = None
                    event_type = None
                continue
                
            # 解析事件行
            parsed = self._parse_sse_line(line)
            if not parsed:
                continue
                
            # 处理各种字段
            if 'data' in parsed:
                event_data += parsed['data']
            elif 'id' in parsed:
                event_id = parsed['id']
            elif 'event' in parsed:
                event_type = parsed['event']
    
    async def connect(
        self,
        endpoint: str,
        response_model: type[T] | None = None,
        **kwargs: Any
    ) -> AsyncGenerator[T | dict[str, Any]]:
        """
        连接到SSE端点并返回事件流
        
        Args:
            endpoint: SSE API端点
            response_model: 响应数据的Pydantic模型类
            **kwargs: 传递给httpx.stream的其他参数
            
        Returns:
            异步生成器，生成解析后的事件数据
        """
        url = f"{endpoint}"
        
        try:
            async with self.client.stream("GET", url, **kwargs) as response:
                response.raise_for_status()
                async for event in self._process_sse_stream(response, response_model):
                    yield event
        except httpx.RequestError as e:
            # 连接错误处理
            raise ConnectionError(f"SSE连接失败: {str(e)}")
    
    async def subscribe(
        self,
        endpoint: str,
        callback: Callable[[T | dict[str, Any]], Any],
        response_model: type[T] | None = None,
        reconnect_interval: float = 3.0,
        max_retries: int | None = None,
        **kwargs: Any
    ) -> None:
        """
        订阅SSE端点，并在收到事件时调用回调函数
        
        Args:
            endpoint: SSE API端点
            callback: 事件回调函数
            response_model: 响应数据的Pydantic模型类
            reconnect_interval: 重连间隔（秒）
            max_retries: 最大重试次数，为None则无限重试
            **kwargs: 传递给connect的其他参数
        """
        retries = 0
        
        while max_retries is None or retries < max_retries:
            try:
                async for event in self.connect(endpoint, response_model, **kwargs):
                    # 正确处理同步和异步回调
                    result = callback(event)
                    if asyncio.iscoroutine(result):
                        await result
                    retries = 0  # 成功接收事件后重置重试计数
                    
            except (httpx.RequestError, ConnectionError):
                retries += 1
                await asyncio.sleep(reconnect_interval)
                continue
                
            except Exception:
                # 其他异常不尝试重连
                raise
                
            # 如果没有异常且事件流结束，也尝试重连
            await asyncio.sleep(reconnect_interval)
