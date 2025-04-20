"""
获取packet状态 API
用于获取当前网络包的状态信息，帮助诊断网络连接情况
接口地址: https://napcat.apifox.cn/226659280e0.md

参数：
无需参数

返回：
- 包含网络包状态的对象，通常包含发送/接收统计、网络延迟信息等
- 可能包含连接质量、丢包率等网络性能指标

注意：
- 此API可用于监控和诊断网络连接问题
- 状态信息反映了底层网络通信的实时情况
- 在网络连接不稳定时，可通过此API获取详细的故障信息

# NapCat 开发中
"""

from napcat.api.base.models import BaseHttpResponse
from pydantic import BaseModel

class NcGetPacketStatusReq(BaseModel):
    """
    获取packet状态 API 请求参数
    """
    pass  # 无需参数

class PacketStatistics(BaseModel):
    """
    网络包统计信息
    """
    total_sent: int           # 发送的包总数
    total_received: int       # 接收的包总数
    bytes_sent: int           # 发送的总字节数
    bytes_received: int       # 接收的总字节数
    packets_lost: int         # 丢失的包数量
    packet_loss_rate: float   # 丢包率

class NetworkMetrics(BaseModel):
    """
    网络性能指标
    """
    average_latency: float    # 平均延迟(毫秒)
    max_latency: float        # 最大延迟(毫秒)
    jitter: float             # 抖动值(毫秒)
    connection_quality: str   # 连接质量评级(如"good", "fair", "poor")

class PacketStatus(BaseModel):
    """
    网络包状态信息
    """
    statistics: PacketStatistics  # 包统计信息
    metrics: NetworkMetrics       # 网络性能指标
    connection_stable: bool       # 连接是否稳定
    last_activity: int            # 最后活动时间戳(毫秒)

class NcGetPacketStatusRes(BaseHttpResponse[PacketStatus]):
    """
    获取packet状态 API 响应参数
    """
    pass