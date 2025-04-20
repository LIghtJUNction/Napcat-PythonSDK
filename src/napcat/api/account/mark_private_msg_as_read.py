"""
标记私聊消息已读 API
用于将与指定用户的私聊消息标记为已读状态
接口地址: https://napcat.apifox.cn/226656924e0.md

参数：
- user_id: 要标记已读消息的用户QQ号
- time: 标记此时间戳之前的消息为已读(可选)

返回：
- 标记私聊消息已读的结果状态

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class MarkPrivateMsgAsReadReq(BaseModel):
    """
    标记私聊消息已读 API 请求参数
    """
    user_id: int                # 要标记已读消息的用户QQ号
    time: int | None = None         # 标记此时间戳之前的消息为已读(可选)

class ReadMarkResult(BaseModel):
    """
    标记私聊消息已读的结果状态
    """
    success: bool               # 是否标记成功
    message: str                # 结果消息

class MarkPrivateMsgAsReadRes(BaseHttpResponse[ReadMarkResult]):
    """
    标记私聊消息已读 API 响应参数
    """
    pass