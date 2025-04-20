"""
检查是否可以发送语音 API

用于检查当前是否有能力发送语音消息
接口地址: https://napcat.apifox.cn/226658533e0.md

参数：
无需参数

返回：
- 是否能够发送语音消息的状态信息

# NapCat 开发中
"""

from napcat.api.base.types import BaseHttpResponse
from pydantic import BaseModel

class CanSendRecordReq(BaseModel):
    """
    检查是否可以发送语音 API 请求参数
    """
    pass  # 无需参数

class RecordAbilityInfo(BaseModel):
    """
    语音发送能力信息
    """
    yes: bool        # 是否能发送语音
    reason: str      # 如果不能发送，提供原因说明

class CanSendRecordRes(BaseHttpResponse[RecordAbilityInfo]):
    """
    检查是否可以发送语音 API 响应参数
    """
    pass