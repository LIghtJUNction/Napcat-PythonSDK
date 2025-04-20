"""
发布群公告 API
用于在指定群发布新的群公告
接口地址: https://napcat.apifox.cn/227380871e0.md

参数：
- group_id: 群号
- title: 公告标题
- content: 公告内容
- is_top: 是否置顶
- is_all_confirm: 是否需要确认

返回：
- 发布结果状态

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class SendGroupNoticeReq(TypedDict):
    """
    发布群公告 API 请求参数
    """
    group_id: int       # 群号
    title: str          # 公告标题
    content: str        # 公告内容
    is_top: bool        # 是否置顶
    is_all_confirm: bool # 是否需要确认

class SendGroupNoticeRes(BaseHttpResponse[dict[str, bool]]):
    """
    发布群公告 API 响应参数
    """
    pass