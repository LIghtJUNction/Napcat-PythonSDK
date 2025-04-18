"""
HTTP SSE客户端实现模块

提供基于HTTP Server-Sent Events的客户端连接实现
"""

import asyncio
import json
import logging
from typing import Optional

from pydantic import PrivateAttr


from .base import ClientBase

logger = logging.getLogger(__name__)

class SSEClient(ClientBase):
    """
    HTTP SSE客户端实现
    
    提供基于Server-Sent Events的事件接收功能
    """
    # 公共属性
    is_running: bool = False
    
    # 私有属性
    _sse_task: asyncio.Task | None = PrivateAttr(default=None)
"""
HTTP SSE客户端实现模块

提供基于HTTP Server-Sent Events的客户端连接实现
"""

import asyncio
import json
import logging
from typing import Optional

from pydantic import PrivateAttr


from .base import ClientBase

logger = logging.getLogger(__name__)

class SSEClient(ClientBase):
    """
    HTTP SSE客户端实现
    
    提供基于Server-Sent Events的事件接收功能
    """
    # 私有属性
    _sse_task: asyncio.Task | None = PrivateAttr(default=None)
    
    async def _start_sse_client(self):
        """
        启动HTTP SSE客户端
        
        连接SSE服务并开始接收事件
        """
        # 如果已有任务在运行，先停止
        if self._sse_task and not self._sse_task.done():
            await self._stop_sse_client()
            
        # 连接SSE服务
        await self._connect_sse()
        
        # 创建新任务
        self._sse_task = asyncio.create_task(self._sse_listener())
        logger.info("SSE监听任务已启动")
    
    async def _stop_sse_client(self):
        """
        停止HTTP SSE客户端
        
        取消监听任务并关闭连接
        """
        if self._sse_task and not self._sse_task.done():
            self._sse_task.cancel()
            try:
                await self._sse_task
            except asyncio.CancelledError:
                pass
                
        self._sse_task = None
        
        # 关闭SSE连接
        if self.api.sse_response:
            try:
                self.api.sse_response.close()
            except Exception as e:
                logger.error(f"关闭SSE响应时出错: {e}")
                
        if self.api.sse_session:
            try:
                await self.api.sse_session.close()
                self.api.sse_session = None
            except Exception as e:
                logger.error(f"关闭SSE会话时出错: {e}")
                
        logger.info("SSE监听任务已停止")
    
    async def _connect_sse(self):
        """
        连接到SSE服务
        
        建立HTTP连接并准备接收事件流
        """
        # 调用API的SSE连接方法
        await self.api.HTTP_CLIENT_SSE_CONNECT()
        
    async def _sse_listener(self):
        """
        SSE监听循环，接收服务器推送的事件
        
        解析事件流并分发事件
        """
        if not self.api.sse_response:
            logger.error("SSE响应对象未初始化，请先调用HTTP_CLIENT_SSE_CONNECT")
            return
            
        try:
            # 接收并处理SSE事件流
            async for raw_event in self._parse_sse():
                # 解析事件数据
                if raw_event.get("event") == "message":
                    try:
                        data_str = raw_event.get("data", "{}")
                        data = json.loads(data_str)
                        
                        # 将事件交给分发器处理
                        if self._dispatcher:
                            await self._dispatcher.process_response(data)
                    except json.JSONDecodeError:
                        logger.error(f"SSE事件数据格式错误: {raw_event.get('data')}")
                        
        except asyncio.CancelledError:
            logger.info("SSE监听任务被取消")
            raise
        except Exception as e:
            logger.error(f"SSE监听过程中出错: {e}")
        finally:
            # 任务结束，确保关闭所有连接
            await self._stop_sse_client()
            
    async def _parse_sse(self):
        """
        解析SSE事件流
        
        :yields: 解析后的SSE事件字典，包含event和data字段
        """
        if not self.api.sse_response:
            raise RuntimeError("SSE响应对象未初始化")
            
        # SSE事件解析状态
        event_type = None
        data_buffer = []
        
        try:
            # 按行读取响应内容
            async for line_bytes in self.api.sse_response.content:
                line = line_bytes.decode('utf-8').rstrip()
                
                # 空行表示事件结束
                if not line:
                    if data_buffer:
                        data = '\n'.join(data_buffer)
                        yield {
                            'event': event_type or 'message',
                            'data': data
                        }
                        # 重置缓冲区
                        event_type = None
                        data_buffer = []
                    continue
                    
                # 处理事件行
                if line.startswith('event:'):
                    event_type = line[6:].strip()
                elif line.startswith('data:'):
                    data_buffer.append(line[5:].strip())
                # 忽略其他行类型如id:和retry:
                
        except Exception as e:
            logger.error(f"处理SSE事件流时出错: {e}")
            raise
