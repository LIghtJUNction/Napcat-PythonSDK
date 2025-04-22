"""
@作者：LIghtJUNction
@日期：2025/04/20
HTTP Client V1
"""
import httpx
from typing import Any, TypeVar
from types import TracebackType
from pydantic import BaseModel
import logging
import sys

from napcat.base.models import BaseHttpResponse

from napcat.base.models import BaseHttpAPI

# 配置日志记录器
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

logger = logging.getLogger("napcat.http")

T = TypeVar('T', bound=BaseModel)
Treq = TypeVar('Treq', bound=BaseModel)

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
    
    async def send(
            self,
            API : BaseHttpAPI,
        ) -> BaseHttpResponse[Any]:
        """ 
        发送POST请求
        
        Args:
            api: API对象，包含请求和响应模型 
            
        Returns:
            响应数据
        """
        url = f"{self.base_url}{API.api}"
        logger.info(f"发送{API.method}请求: {url}")
        
        async with self.client as client:
            if API.method == "POST":
                response = await client.post(
                    url,
                    json=API.request.model_dump(by_alias=True),
                )

                logger.debug(f"响应数据: {response.text}")
                # 将响应文本解析为 JSON 字典，然后传递给 model_validate
                response_data = response.json()
                logger.info("验证响应"+"="*20)
                # 设置 by_alias=True 和 from_attributes=False 以更好地处理字段名称映射
                # 同时添加 from_attributes=False 以防止尝试从非对象属性中获取数据
                API.response = API.response.model_validate(
                    response_data,
                    from_attributes=False,
                    by_alias=True
                )
                return API.response
            elif API.method == "GET":
                response = await client.get(
                    url,
                    params=API.request.model_dump(by_alias=True),
                )

                logger.debug(f"响应数据: {response.text}")
                # 将响应文本解析为 JSON 字典，然后传递给 model_validate
                response_data = response.json()
                logger.info("验证响应"+"="*20)
                # 设置 by_alias=True 和 from_attributes=False 以更好地处理字段名称映射
                # 同时添加 from_attributes=False 以防止尝试从非对象属性中获取数据
                API.response = API.response.model_validate(
                    response_data,
                    from_attributes=False,
                    by_alias=True
                )
                return API.response
            else:
                raise ValueError(f"不支持的请求方法: {API.method}")