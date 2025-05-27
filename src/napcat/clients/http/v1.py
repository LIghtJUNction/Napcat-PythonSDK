"""
AsyncHttpClient功能：提供异步HTTP请求客户端，支持Pydantic模型序列化
"""
from __future__ import annotations

import httpx
import logging
import sys
from types import TracebackType
from typing import Any, TypeVar
from pydantic import BaseModel

# 配置日志记录器
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

logger = logging.getLogger("napcat.http")

# 泛型类型变量
TReq = TypeVar('TReq', bound=BaseModel)
TRes = TypeVar('TRes', bound=BaseModel)

class AsyncHttpClient:
    """
    异步HTTP客户端，处理与API的异步通信，支持Pydantic模型的序列化和反序列化。
    """
    def __init__(
        self,
        base_url: str,
        token: str,
        timeout: float = 60.0,
        debug: bool = False,
    ):
        """
        初始化异步HTTP客户端
        
        Args:
            base_url: API基础URL
            token: 认证令牌
            timeout: 请求超时时间（秒）
        """
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.timeout = timeout
        self._client = None

        if debug:
            logger.setLevel(logging.DEBUG)

        logger.info(f"初始化HTTP客户端: base_url={self.base_url}")
        
    def _get_headers(self) -> dict[str, str]:
        """获取请求头，包括认证信息"""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        logger.debug(f"请求头: {headers}")
        return headers
    
    @property
    def client(self) -> httpx.AsyncClient:
        """懒加载异步HTTP客户端实例"""
        if self._client is None:
            logger.info(f"创建新的HTTP客户端连接: {self.base_url}")
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                headers=self._get_headers(),
            )
        return self._client
    
    async def close(self) -> None:
        """关闭异步HTTP客户端连接"""
        if self._client is not None:
            logger.info("关闭HTTP客户端连接")
            await self._client.aclose()
            self._client = None
      async def __aenter__(self) -> "AsyncHttpClient":
        return self
    
    async def __aexit__(
        self, 
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None
    ) -> None:
        await self.close()
    
    async def send(self, api_class: type, request_data: BaseModel) -> BaseModel:
        """ 
        发送HTTP请求
        
        Args:
            api_class: API类，包含endpoint, method, Req, Res等属性
            request_data: 请求数据模型实例
            
        Returns:
            响应数据模型实例
        """
        # 从API类中提取元数据
        endpoint = api_class.endpoint
        method = api_class.method
        response_class = api_class.Res
        
        url = f"{self.base_url}{endpoint}"
        logger.info(f"发送{method}请求: {url}")
        
        # 序列化请求数据
        request_payload = request_data.model_dump(by_alias=True)
        logger.debug(f"请求数据: {request_payload}")
        
        async with self.client as client:
            # 根据HTTP方法发送请求
            if method == "POST":
                response = await client.post(url, json=request_payload)
            elif method == "GET":
                response = await client.get(url, params=request_payload)
            else:
                raise ValueError(f"不支持的请求方法: {method}")

            # 检查HTTP状态码
            response.raise_for_status()
            
            logger.debug(f"响应状态码: {response.status_code}")
            logger.debug(f"响应数据: {response.text}")
            
            # 解析响应并验证
            response_data = response.json()
            logger.info("验证响应模型" + "=" * 20)
            
            # 使用响应类验证数据
            validated_response = response_class.model_validate(
                response_data,
                from_attributes=False,
                by_alias=True
            )
            
            logger.info("响应验证成功")
            return validated_response