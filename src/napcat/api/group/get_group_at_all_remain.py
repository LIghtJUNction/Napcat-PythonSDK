"""
获取群@全体成员剩余次数 API
用于查询群内@全体成员的剩余次数
接口地址: https://napcat.apifox.cn/227425447e0.md

参数：
- group_id: 群号

返回：
- 群内@全体成员剩余次数信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class GetGroupAtAllRemainReq(TypedDict):
    """
    获取群@全体成员剩余次数 API 请求参数
    """
    group_id: int  # 群号

class AtAllRemainInfo(TypedDict):
    """
    @全体成员剩余信息
    """
    can_at_all: bool  # 是否可以@全体成员
    remain_at_all_count_for_group: int  # 群内所有管理员剩余@全体成员次数
    remain_at_all_count_for_uin: int    # 当前用户剩余@全体成员次数

class GetGroupAtAllRemainRes(BaseHttpResponse[AtAllRemainInfo]):
    """
    获取群@全体成员剩余次数 API 响应参数
    """
    pass