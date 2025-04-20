"""
设置群管理员 API
用于设置或取消群管理员身份
接口地址: https://napcat.apifox.cn/227425594e0.md

参数：
- group_id: 群号
- user_id: 用户QQ号
- enable: 是否设置为管理员

返回：
- 操作结果

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class SetGroupAdminReq(TypedDict):
    """
    设置群管理员 API 请求参数
    """
    group_id: int  # 群号
    user_id: int   # 用户QQ号
    enable: bool   # 是否设置为管理员

class SetGroupAdminRes(BaseHttpResponse[dict[str, bool]]):
    """
    设置群管理员 API 响应参数
    """
    pass