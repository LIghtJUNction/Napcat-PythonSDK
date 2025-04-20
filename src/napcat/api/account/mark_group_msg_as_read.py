"""
标记群消息已读 API
用于将指定群的消息标记为已读状态
接口地址: https://napcat.apifox.cn/226656923e0.md

参数：
- group_id: 要标记消息已读的群号
- time: 标记此时间戳之前的消息为已读(可选)

返回：
- 标记群消息已读的结果状态

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class MarkGroupMsgAsReadReq(BaseModel):
    """
    标记群消息已读 API 请求参数
    """
    group_id: int               # 要标记消息已读的群号
    time: int | None = None         # 标记此时间戳之前的消息为已读(可选)

class GroupReadResult(BaseModel):
    """
    标记群消息已读的结果状态
    """
    success: bool               # 是否标记成功
    message: str                # 结果消息

class MarkGroupMsgAsReadRes(BaseHttpResponse[GroupReadResult]):
    """
    标记群消息已读 API 响应参数
    """
    pass