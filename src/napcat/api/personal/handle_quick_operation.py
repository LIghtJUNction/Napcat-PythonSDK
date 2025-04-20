"""
对事件执行快速操作 API
用于对接收到的事件进行快速响应处理
接口地址: https://napcat.apifox.cn/228954032e0.md

参数：
- context: 事件上下文对象，包含事件的相关信息
- operation: 要执行的操作对象，包含操作类型和参数

返回：
- 操作执行结果，包含是否成功及相关信息

注意：
- 此API用于简化事件处理流程，将常用操作封装为快速响应
- 支持对消息、请求等多种事件类型的快速操作
- 不同事件类型支持的操作可能不同，请参考具体事件文档

# NapCat 开发中
"""

from typing import Any
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class EventContext(BaseModel):
    """
    事件上下文信息
    """
    event_id: str             # 事件ID
    event_type: str           # 事件类型
    detail_type: str          # 详细类型
    sub_type: str             # 子类型
    time: int                 # 事件发生的时间戳
    self_id: int              # 收到事件的机器人QQ号

class Operation(BaseModel):
    """
    快速操作内容
    """
    type: str                 # 操作类型
    reply: str | None = None                # 回复内容(可选)
    at_sender: bool | None = None           # 是否@发送者(可选)
    delete: bool | None = None              # 是否撤回消息(可选)
    kick: bool | None = None                # 是否踢出群员(可选)
    ban: bool | None = None                 # 是否禁言(可选)
    ban_duration: int | None = None         # 禁言时长(可选)
    approve: bool | None = None             # 是否同意请求(可选)
    reason: str | None = None               # 拒绝理由(可选)
    # 其他可能的操作参数...

class HandleQuickOperationReq(BaseModel):
    """
    对事件执行快速操作 API 请求参数
    """
    context: EventContext     # 事件上下文
    operation: Operation      # 操作内容

class OperationResult(BaseModel):
    """
    操作执行结果
    """
    success: bool             # 是否成功
    message: str              # 结果消息
    detail: dict[str, Any]    # 详细结果信息(如果有)

class HandleQuickOperationRes(BaseHttpResponse[OperationResult]):
    """
    对事件执行快速操作 API 响应参数
    """
    pass