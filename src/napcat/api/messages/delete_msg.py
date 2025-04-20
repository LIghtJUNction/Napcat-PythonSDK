"""
撤回消息 API
用于撤回已发送的消息
接口地址: https://napcat.apifox.cn/227228898e0.md

参数：
- message_id: 消息ID

返回：
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.types import BaseHttpResponse

class DeleteMsgReq(TypedDict):
    """
    撤回消息 API 请求参数
    """
    message_id: int  # 消息ID

class DeleteMsgRes(BaseHttpResponse[dict[str, bool]]):
    """
    撤回消息 API 响应参数
    """
    pass