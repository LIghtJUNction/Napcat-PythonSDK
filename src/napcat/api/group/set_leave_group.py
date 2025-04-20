"""
退群 API
用于机器人退出指定群组
接口地址: https://napcat.apifox.cn/226656926e0.md

参数:
- group_id: int - 群号
- is_dismiss: bool - 是否解散群（如果是群主）

返回:
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class SetLeaveGroupReq(TypedDict):
    """
    退群 API 请求参数
    """
    group_id: int    # 群号
    is_dismiss: bool # 是否解散群（如果是群主）

class SetLeaveGroupRes(BaseHttpResponse[dict[str, bool]]):
    """
    退群 API 响应参数
    """
    pass