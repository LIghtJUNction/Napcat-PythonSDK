"""
获取运行状态 API
用于获取NapCat的运行状态
接口地址: https://napcat.apifox.cn/227230473e0.md

参数：
无需参数

返回：
- NapCat运行状态

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetStatusReq(BaseModel):
    """
    获取运行状态 API 请求参数
    # 无需参数
    """
    pass  # 无需参数

class AppStatus(BaseModel):
    """
    应用状态信息
    """
    app_initialized: bool     # 程序是否初始化完成
    app_enabled: bool         # 程序是否启用
    plugins_good: list[str]   # 正常运行的插件
    plugins_bad: list[str]    # 运行异常的插件

class StatData(BaseModel):
    """
    统计数据
    """
    packet_received: int      # 接收数据包总数
    packet_sent: int          # 发送数据包总数
    packet_lost: int          # 数据包丢失总数
    message_received: int     # 接收消息总数
    message_sent: int         # 发送消息总数
    disconnect_times: int     # 断开连接次数
    lost_times: int           # 连接丢失次数

class RunningStatus(BaseModel):
    """
    运行状态信息
    """
    good: bool                # 程序运行状态是否正常
    online: bool              # 是否在线
    stat: StatData            # 统计数据
    app: AppStatus            # 应用状态

class GetStatusRes(BaseHttpResponse[RunningStatus]):
    """
    获取运行状态 API 响应参数
    """
    pass