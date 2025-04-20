"""
获取rkey服务 API
用于获取专门提供rkey的服务信息，包括服务地址、访问方式等
接口地址: https://napcat.apifox.cn/283136236e0.md

参数：
无需参数

返回：
- 包含rkey服务相关信息的对象，可用于配置和访问rkey服务

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetRkeyServerReq(BaseModel):
    """
    获取rkey服务 API 请求参数
    """
    pass  # 无请求参数

class ServerEndpoint(BaseModel):
    """
    服务端点信息
    """
    url: str            # 服务URL地址
    protocol: str       # 通信协议
    priority: int       # 优先级

class RkeyServerInfo(BaseModel):
    """
    Rkey服务信息
    """
    service_name: str                # 服务名称
    endpoints: list[ServerEndpoint]  # 服务端点列表
    timeout: int                     # 超时时间(毫秒)
    retry_count: int                 # 重试次数

class GetRkeyServerRes(BaseHttpResponse[RkeyServerInfo]):
    """
    获取rkey服务 API 响应参数
    """
    pass