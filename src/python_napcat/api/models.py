"""
API模型定义模块

该模块包含了API相关的数据模型和枚举类型
"""

import enum
from typing import ClassVar, Literal, Optional, TypeAlias, Any
from pydantic import BaseModel
from pydantic_core import Url
import logging
import aiohttp

from websockets.legacy.server import serve

# 使用Any作为类型注解，避免循环导入
NapcatHttpServer: TypeAlias = Any

logger = logging.getLogger(__name__)

class NapcatPort(enum.Enum):
    """Napcat 端口枚举类"""
    HTTP_CLIENT = 10143
    HTTP_SSE_CLIENT = 10144
    WS_CLIENT = 10145
    HTTP_SERVER = 10146
    WS_SERVER = 10147
    
    @classmethod
    def update(cls, name: str, port: int) -> None:
        """
        更新指定名称的端口号
        
        :param name: 端口名称
        :param port: 新的端口号
        :raises ValueError: 如果端口名称不存在
        """
        if hasattr(cls, name):
            setattr(cls, name, port)
            logger.info(f"更新端口: {name} = {port}")
        else:
            logger.warning(f"端口名称 {name} 不存在，无法更新")
            raise ValueError(f"端口名称 {name} 不存在，无法更新")

class NapcatHost(enum.Enum):
    """Napcat HOST枚举类"""
    HTTP_CLIENT = "127.0.0.1"
    HTTP_SSE_CLIENT = "127.0.0.1"
    WS_CLIENT = "127.0.0.1"
    HTTP_SERVER = "127.0.0.1"
    WS_SERVER = "127.0.0.1"

    @classmethod
    def update(cls, name: str, host: str) -> None:
        """
        更新指定名称的主机地址
        
        :param name: 主机名称
        :param host: 新的主机地址
        :raises ValueError: 如果主机名称不存在
        """
        if hasattr(cls, name):
            setattr(cls, name, host)
            logger.info(f"更新主机: {name} = {host}")
        else:
            logger.warning(f"主机名称 {name} 不存在，无法更新")
            raise ValueError(f"主机名称 {name} 不存在，无法更新")

class NapcatType(enum.Enum):    
    """Napcat 类型枚举类"""
    HTTP_CLIENT = "HTTP/CLIENT"
    HTTP_SSE_CLIENT = "HTTP/CLIENT/SSE"
    WS_CLIENT = "WS/CLIENT"
    HTTP_SERVER = "HTTP/SERVER"
    WS_SERVER = "WS/SERVER"

class NapcatAPI(BaseModel):
    """
    提供基本对象，API低级封装
    
    请调用类方法创建实例：
    - NapcatAPI.NapcatHttpClient()
    - NapcatAPI.NapcatHttpSSEClient()
    - NapcatAPI.NapcatHttpServer()
    - NapcatAPI.NapcatWebSocketClient()
    - NapcatAPI.NapcatWebSocketServer()
    """
    # 类变量
    WS_CLIENT: ClassVar[str] = "WS/CLIENT"
    HTTP_CLIENT: ClassVar[str] = "HTTP/CLIENT"
    
    # 实例属性
    name: str                                         # 实例名称，用于在metadata中索引
    host: str                                         # 主机地址，用于服务器绑定或客户端连接
    port: int                                         # 端口号，指定服务运行的端口
    ws_path: str                                      # WebSocket路径，默认为"/aivk/qq"
    token: str | None = None                       # 认证令牌，用于安全验证，可为None
    msgtype: Literal["Array", "String"] = "Array"     # 消息格式，可选值为"Array"或"String"
    cors: bool = True                                 # 是否启用跨域资源共享
    ws: bool = True                                   # 是否启用WebSocket
    type_: NapcatType | None = None                # 实例类型，会在创建实例时设置
    http_url: Url | None = None                    # HTTP URL
    ws_url: Url | None = None                      # WebSocket URL
    
    # 动态创建的字段
    http_client: aiohttp.ClientSession | None = None  # HTTP客户端实例
    http_server: NapcatHttpServer | None = None     # HTTP服务器实例
    ws_client_url: str | None = None                # WebSocket client connection URL
    ws_server: serve | None = None                  # WebSocket服务器实例
    sse_session: aiohttp.ClientSession | None = None  # SSE会话实例
    sse_response: aiohttp.ClientResponse | None = None  # SSE响应实例
    
    # 静态属性，保存所有实例的引用
    metadata: ClassVar[dict[str, "NapcatAPI"]] = {}
    
    class Config:
        arbitrary_types_allowed = True  # 允许使用非Pydantic原生支持的类型

    def __init__(
        self, 
        HOST: str, 
        PORT: int, 
        WS_PATH: str, 
        TOKEN: str | None, 
        NAME: str, 
        MSGTYPE: Literal["Array", "String"] = "Array", 
        CORS: bool = True, 
        WS: bool = True,
        **kwargs
    ) -> None:
        """初始化NapcatAPI对象"""
        # 调用父类初始化方法，将参数传递给Pydantic的BaseModel
        super().__init__(
            name=NAME, 
            host=HOST, 
            port=PORT, 
            ws_path=WS_PATH,
            token=TOKEN,
            msgtype=MSGTYPE,
            cors=CORS,
            ws=WS,
            **kwargs
        )
    
    def _TYPE_CHECK(self, type_: NapcatType) -> None:
        """
        检查实例类型是否匹配预期类型
        
        :param type_: 预期的类型
        :raises ValueError: 如果类型不匹配
        """
        if self.type_ != type_:
            raise ValueError(f"类型不匹配: {self.type_.value if self.type_ else None} != {type_.value}")

    @classmethod
    def NapcatHttpClient(cls, **kwargs) -> "NapcatAPI":
        """创建HTTP客户端实例"""
        instance = cls(**kwargs)
        instance.type_ = NapcatType.HTTP_CLIENT
        return instance  # type: ignore[return-value]

    @classmethod
    def NapcatHttpSSEClient(cls, **kwargs) -> "NapcatAPI":
        """创建HTTP SSE客户端实例"""
        instance = cls(**kwargs)
        instance.type_ = NapcatType.HTTP_SSE_CLIENT
        return instance  # type: ignore[return-value]

    @classmethod
    def NapcatWebSocketClient(cls, **kwargs) -> "NapcatAPI":
        """创建WebSocket客户端实例"""
        instance = cls(**kwargs)
        instance.type_ = NapcatType.WS_CLIENT
        return instance  # type: ignore[return-value]

    @classmethod
    def NapcatHttpServer(cls, **kwargs) -> "NapcatAPI":
        """创建HTTP服务器实例"""
        instance = cls(**kwargs)
        instance.type_ = NapcatType.HTTP_SERVER
        return instance  # type: ignore[return-value]

    @classmethod
    def NapcatWebSocketServer(cls, **kwargs) -> "NapcatAPI":
        """创建WebSocket服务器实例"""
        instance = cls(**kwargs)
        instance.type_ = NapcatType.WS_SERVER
        return instance  # type: ignore[return-value]
