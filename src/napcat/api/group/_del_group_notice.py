"""
删除群公告 API
用于删除指定群的某条公告
接口地址: https://napcat.apifox.cn/227380871e0.md

参数：
- group_id: 群号
- notice_id: 公告ID

返回：
- 删除结果状态

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

# region TypedDicts
class DelGroupNoticeReq(TypedDict):
    """
    删除群公告 API 请求参数
    """
    group_id: int   # 群号
    notice_id: str  # 公告ID

class DelGroupNoticeRes(BaseHttpResponse[dict[str, bool]]):
    """
    删除群公告 API 响应参数
    """
    pass