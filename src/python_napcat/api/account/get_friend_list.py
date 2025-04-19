"""
获取好友列表 API
用于获取当前账号的好友列表信息
接口地址: https://napcat.apifox.cn/227233981e0.md

参数：
- page: 分页页码 (可选，默认1)
- size: 每页数量 (可选，默认20)
- sort: 排序方式 (可选，默认按添加时间倒序)

返回：
- 好友列表数据及分页信息
"""

from typing import TypedDict, List
from python_napcat.api.base.types import BaseHttpResponse

class FriendListReq(TypedDict):
    """
    获取好友列表 API 请求参数
    """
    page: int   # 分页页码
    size: int   # 每页数量
    sort: str   # 排序方式 (add_time_desc/add_time_asc)

class FriendInfo(TypedDict):
    """
    好友信息
    """
    user_id: int      # 好友QQ号
    nickname: str     # 好友昵称
    remark: str       # 好友备注
    category: str     # 好友分组
    add_time: str     # 添加时间

class PaginationMeta(TypedDict):
    """
    分页元数据
    """
    total: int        # 总记录数
    current_page: int # 当前页码
    total_pages: int  # 总页数

class GetFriendListRes(BaseHttpResponse[List[FriendInfo]]):
    """
    获取好友列表 API 响应参数
    """
    meta: PaginationMeta  # 分页元数据
