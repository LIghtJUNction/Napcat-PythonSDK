"""
标记消息已读 API
用于将指定的消息标记为已读状态
接口地址: https://napcat.apifox.cn/226659183e0.md

参数：
- message_id: 要标记为已读的消息ID

返回：
- 标记消息已读的结果状态

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class MarkMsgAsReadReq(BaseModel):
    """
    标记消息已读 API 请求参数
    """
    message_id: str             # 要标记为已读的消息ID

class MessageReadResult(BaseModel):
    """
    标记消息已读的结果状态
    """
    success: bool               # 是否标记成功
    message: str                # 结果消息

class MarkMsgAsReadRes(BaseHttpResponse[MessageReadResult]):
    """
    标记消息已读 API 响应参数
    """
    pass