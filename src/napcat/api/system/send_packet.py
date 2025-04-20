"""
发送自定义组包 API
用于发送自定义的网络数据包
接口地址: https://napcat.apifox.cn/250286903e0.md

参数：
- cmd: 指令名称或代码
- body: 请求体数据，包含要发送的具体内容
- timeout: 超时时间(毫秒)，可选

返回：
- 发送结果对象，包含服务器响应的数据

注意：
- 此API为高级功能，需要对协议有深入理解
- 不正确的数据包可能导致连接问题或服务异常
- 建议只在特殊场景下使用此功能
- 使用前请确保了解相关风险

# NapCat 开发中
"""

from typing import Any
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SendPacketReq(BaseModel):
    """
    发送自定义组包 API 请求参数
    """
    cmd: str          # 指令名称或代码
    body: dict[str, Any]  # 请求体数据
    timeout: int | None = None      # 超时时间(毫秒)，可选

class PacketResponse(BaseModel):
    """
    数据包响应详情
    """
    data: Any         # 服务器响应数据
    status: int       # 响应状态码
    message: str      # 响应消息

class SendPacketRes(BaseHttpResponse[PacketResponse]):
    """
    发送自定义组包 API 响应参数
    """
    pass