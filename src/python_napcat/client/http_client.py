"""
HTTP客户端实现模块

提供基于HTTP的客户端连接实现
"""

import asyncio
import logging
from typing import Optional

from pydantic import PrivateAttr

from aiohttp import ClientSession

from .base import ClientBase
from ..api.models import NapcatType
from ..utils.types import ApiResponseDict

logger = logging.getLogger(__name__)

class HttpClient(ClientBase):
    """
    HTTP客户端实现
    
    提供基于HTTP的API调用和轮询功能
    """
    # 私有属性
    _http_client: ClientSession | None = PrivateAttr(default=None)
    _poll_task: asyncio.Task | None = PrivateAttr(default=None)
    _poll_interval: float = PrivateAttr(default=3.0)  # 默认轮询间隔3秒
    
    async def start(self):
        """
        启动HTTP客户端
        
        初始化HTTP连接和事件分发器
        """
        # 调用父类的start方法，初始化事件分发器
        await super().start()
        
        # 确保API类型正确
        if self.api.type_ != NapcatType.HTTP_CLIENT:
            raise ValueError(f"API类型错误，期望HTTP_CLIENT，实际为 {self.api.type_}")
        
        # 初始化HTTP客户端
        await self._init_http_client()
    
    async def stop(self):
        """
        停止HTTP客户端
        
        关闭HTTP连接和轮询任务
        """
        # 停止轮询任务
        await self._stop_polling()
        
        # 关闭HTTP客户端
        await self._close_http_client()
        
        # 调用父类的stop方法，关闭事件分发器
        await super().stop()
        
        logger.info("HTTP客户端已停止")
    
    async def _init_http_client(self):
        """
        初始化HTTP客户端会话
        
        使用API中的配置，如URL、Token等
        """
        # 确保API调用已连接HTTP客户端
        if not self.api.http_client:
            # 创建HTTP连接
            await self.api.HTTP_CLIENT_CONNECT()
            
        # 检查连接是否成功
        if not self.api.http_client:
            raise RuntimeError("HTTP客户端初始化失败")
            
        # 保存客户端引用
        self._http_client = self.api.http_client
        logger.info(f"HTTP客户端已初始化，连接到 {self.api.host}:{self.api.port}")
    
    async def _close_http_client(self):
        """
        关闭HTTP客户端会话
        """
        if self._http_client:
            try:
                await self._http_client.close()
            except Exception as e:
                logger.error(f"关闭HTTP客户端时出错: {e}")
            self._http_client = None
            
        logger.info("HTTP客户端连接已关闭")
    
    async def call_api(self, action: str, **params) -> ApiResponseDict:
        """
        调用API接口
        
        封装底层的_call_action，提供更便捷的接口
        
        :param action: API动作名称
        :param params: API参数
        :return: API响应结果
        """
        return await self._call_action(action, params)
    
    def set_poll_interval(self, seconds: float) -> None:
        """
        设置事件轮询间隔
        
        :param seconds: 轮询间隔秒数
        """
        if seconds < 0.1:
            seconds = 0.1  # 最小轮询间隔0.1秒
        
        self._poll_interval = seconds
        logger.info(f"事件轮询间隔已设置为 {seconds} 秒")
    
    async def start_polling(self) -> None:
        """
        启动事件轮询
        
        通过定期调用get_latest_events API来获取事件
        """
        # 如果已有轮询任务，先停止
        await self._stop_polling()
        
        # 创建新的轮询任务
        self._poll_task = asyncio.create_task(self._polling_loop())
        logger.info(f"事件轮询已启动，间隔 {self._poll_interval} 秒")
    
    async def _stop_polling(self) -> None:
        """
        停止事件轮询
        """
        if self._poll_task and not self._poll_task.done():
            self._poll_task.cancel()
            try:
                await self._poll_task
            except asyncio.CancelledError:
                pass
            
            self._poll_task = None
            logger.info("事件轮询已停止")
    
    async def _polling_loop(self) -> None:
        """
        事件轮询循环
        
        定期调用API获取最新事件
        """
        try:
            while True:
                try:
                    # 调用获取最新事件的API
                    # 注意：根据实际API调整此处的接口名和参数
                    events = await self.call_api("get_latest_events", limit=10)
                    
                    # 处理返回的事件
                    if isinstance(events, dict) and "data" in events:
                        event_list = events.get("data")
                        if isinstance(event_list, list):
                            for event in event_list:
                                if self._dispatcher:
                                    await self._dispatcher.process_response(event)
                    
                except Exception as e:
                    logger.error(f"轮询事件时出错: {e}")
                
                # 等待下一次轮询
                await asyncio.sleep(self._poll_interval)
                
        except asyncio.CancelledError:
            logger.info("轮询任务被取消")
            raise