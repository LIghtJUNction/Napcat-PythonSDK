"""
处理加群请求 API
用于处理他人加群请求或邀请入群请求
接口地址: https://napcat.apifox.cn/227425684e0.md

参数：
- flag: 加群请求标识，事件中收到
- sub_type: 请求类型，add为加群请求，invite为邀请入群
- approve: 是否同意请求
- reason: 拒绝理由，仅在拒绝时有效

返回：
- 操作结果

# NapCat 开发中
"""

from typing import Literal
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class SetGroupAddRequestReq(BaseModel):
    """
    处理加群请求 API 请求参数
    """
    flag: str      # 加群请求标识，事件中收到
    sub_type: Literal["add", "invite"]  # 请求类型，add为加群请求，invite为邀请入群
    approve: bool  # 是否同意请求
    reason: str    # 拒绝理由，仅在拒绝时有效

class SetGroupAddRequestRes(BaseHttpResponse[dict[str, bool]]):
    """
    处理加群请求 API 响应参数
    """
    pass