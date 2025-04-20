"""
退出群组 API
用于机器人退出指定群组
接口地址: https://napcat.apifox.cn/226659329e0.md

参数：
- group_id: 群号
- is_dismiss: 是否解散群（如果是群主）

返回：
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class SetGroupLeaveReq(TypedDict):
    """
    退出群组 API 请求参数
    """
    group_id: int    # 群号
    is_dismiss: bool # 是否解散群（如果是群主）

class SetGroupLeaveRes(BaseHttpResponse[dict[str, bool]]):
    """
    退出群组 API 响应参数
    """
    pass