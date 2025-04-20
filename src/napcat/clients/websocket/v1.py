from collections.abc import Awaitable, Callable
import logging
import functools
from typing import Any, TypeVar
import asyncio
import httpx
from httpx_ws import aconnect_ws, WebSocketDisconnect, AsyncWebSocketSession

logger = logging.getLogger(__name__)

# 定义类型变量用于装饰器
T = TypeVar('T')

class NapcatWebsocketClient:
    """Napcat WebSocket 客户端"""
    
    def __init__(self, base_uri: str, token: str | None = None, headers: dict[str, str] | None = None) -> None:
        """
        初始化 WebSocket 客户端
        
        Args:
            uri: WebSocket 服务器的 URI
            token: 可选的认证令牌
            headers: 可选的额外 HTTP 头信息
        """
        self.base_uri = base_uri
        self.token = token
        self.headers = headers or {}
        self.exit = asyncio.Event()
        self.connected = asyncio.Event()  # 连接状态事件
        self.running = False  # 运行状态标志
        self._lock = asyncio.Lock()  # WebSocket操作锁
        self.ws : AsyncWebSocketSession | None = None  # WebSocket连接对象
        self.client = None  # HTTP客户端
        
        # 消息和错误处理器
        self._message_handlers: list[Callable[[str], Awaitable[Any]]] = []
        self._error_handlers: list[Callable[[Exception], Awaitable[Any]]] = []

    @property
    def uri(self) -> str:
        """获取 WebSocket URI"""
        uri = f"{self.base_uri}?token={self.token}" if self.token else self.base_uri
        return uri
    
    @property
    def is_connected(self) -> bool:
        """检查WebSocket是否已连接"""
        return self.connected.is_set() and self.ws is not None
    
    def on_message(self, func: Callable[[str], Awaitable[T]]) -> Callable[[str], Awaitable[T]]:
        """
        装饰器: 注册一个消息处理函数
        
        Args:
            func: 处理消息的异步函数
            
        Returns:
            传入的函数，使其可以作为装饰器使用
            
        Example:
            ```python
            client = NapcatWebsocketClient(...)
            
            @client.on_message
            async def handle_message(message: str):
                print(f"收到消息: {message}")
            ```
        """
        @functools.wraps(func)
        async def wrapper(message: str) -> T:
            return await func(message)
            
        self._message_handlers.append(wrapper)
        return func
        
    def on_error(self, func: Callable[[Exception], Awaitable[T]]) -> Callable[[Exception], Awaitable[T]]:
        """
        装饰器: 注册一个错误处理函数
        
        Args:
            func: 处理错误的异步函数
            
        Returns:
            传入的函数，使其可以作为装饰器使用
            
        Example:
            ```python
            client = NapcatWebsocketClient(...)
            
            @client.on_error
            async def handle_error(error: Exception):
                print(f"发生错误: {error}")
            ```
        """
        @functools.wraps(func)
        async def wrapper(error: Exception) -> T:
            return await func(error)
            
        self._error_handlers.append(wrapper)
        return func
    
    async def _handle_message(self, message: str) -> None:
        """内部方法: 处理接收到的消息"""
        if not self._message_handlers:
            logger.warning(f"接收到消息: {message} , 但是未设置消息处理器")
            return
            
        for handler in self._message_handlers:
            try:
                await handler(message)
            except Exception as e:
                logger.error(f"执行消息处理器出错: {e}")
                await self._handle_error(e)
    
    async def _handle_error(self, error: Exception) -> None:
        """内部方法: 处理发生的错误"""
        if not self._error_handlers:
            logger.error(f"捕获到错误: {error}, 但是未设置错误处理器")
            return
            
        for handler in self._error_handlers:
            try:
                await handler(error)
            except Exception as e:
                # 避免递归调用
                logger.error(f"执行错误处理器时出错: {e}")
    
    async def send(self, message: str):
        """
        发送消息到WebSocket服务器
        
        Args:
            message: 要发送的消息
            
        Raises:
            RuntimeError: 当WebSocket未连接或已关闭时
        """
        if self.ws:
            async with self._lock:  # 使用锁保证并发安全
                if not self.is_connected:
                    raise RuntimeError("WebSocket 未连接或已关闭")
                await self.ws.send_text(message)
    
    async def disconnect(self):
        """关闭WebSocket连接"""
        async with self._lock:
            self.exit.set()
            self.running = False
            # 直接在这里重置连接状态，避免等待连接循环退出
            self.connected.clear()
            
    async def connect(self, 
                     message_handler: Callable[[str], Awaitable[Any]] | None = None,
                     error_handler: Callable[[Exception], Awaitable[Any]] | None = None,
                     timeout: int = 60) -> asyncio.Task[None]:
        """
        连接到 WebSocket 服务器并在后台任务中处理消息

        Args:
            message_handler: 处理接收到的消息的异步回调函数，也可以使用装饰器 @on_message 设置
            error_handler: 处理错误的异步回调函数，也可以使用装饰器 @on_error 设置
            timeout: 连接超时时间(秒)

        Returns:
            asyncio.Task: 处理连接和消息的后台任务
        """
        # 如果提供了处理函数，添加到处理器列表中
        if message_handler:
            self._message_handlers.append(message_handler)
        
        if error_handler:
            self._error_handlers.append(error_handler)
            
        # 创建一个内部处理连接的协程
        async def _handle_connection():
            self.client = httpx.AsyncClient(timeout=timeout)
            try:
                async with aconnect_ws(self.uri, self.client, headers=self.headers) as ws:
                    self.ws = ws
                    self.running = True
                    self.exit.clear()  # 确保退出事件是清除状态
                    self.connected.set()  # 设置连接状态

                    logger.info(f"WebSocket 连接成功: {self.uri}")

                    # 消息处理循环
                    while self.running:
                        try:
                            # 只等待接收消息，不阻塞在exit事件上
                            message = await ws.receive_text()
                            await self._handle_message(message)
                        except WebSocketDisconnect:
                            logger.info("WebSocket 连接已关闭")
                            break
                        except asyncio.CancelledError:
                            logger.info("WebSocket 连接任务被取消")
                            break
                        except Exception as e:
                            logger.error(f"处理消息时出错: {e}")
                            await self._handle_error(e)

                        # 检查是否收到退出信号
                        if self.exit.is_set():
                            logger.info("收到退出信号，关闭WebSocket连接")
                            break
                        
            except httpx.ConnectError as e:
                logger.error(f"连接失败: {e}")
                await self._handle_error(e)
            finally:
                self.running = False
                self.connected.clear()  # 清除连接状态
                if self.client:
                    await self.client.aclose()

        # 创建并返回后台任务
        connection_task: asyncio.Task[None] = asyncio.create_task(_handle_connection())
        return connection_task