"""
设置精华消息 API
用于将群消息设置为精华消息
接口地址: https://napcat.apifox.cn/227425418e0.md

参数：
- message_id: 消息ID

返回：
- 设置操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class SetEssenceMsgReq(TypedDict):
    """
    设置精华消息 API 请求参数
    """
    message_id: int  # 消息ID

class SetEssenceMsgRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置精华消息 API 响应参数
    """
    pass