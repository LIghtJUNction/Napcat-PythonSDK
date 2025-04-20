"""
标记全部已读 API
用于将所有未读消息标记为已读状态
接口地址: https://napcat.apifox.cn/226659182e0.md

参数：
无需参数

返回：
- 标记全部已读的结果状态

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class MarkAllAsReadReq(BaseModel):
    """
    标记全部已读 API 请求参数
    """
    pass  # 无请求参数

class MarkAllAsReadRes(BaseHttpResponse):
    """
    标记全部已读 API 响应参数
    """
    class Data(BaseModel):
        """标记全部已读的结果数据"""
        success: bool               # 是否标记成功
        message: str                # 结果消息
        marked_count: int           # 已标记已读的消息数量
