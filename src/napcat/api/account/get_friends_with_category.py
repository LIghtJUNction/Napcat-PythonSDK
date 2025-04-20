"""
获取好友分组列表 API
用于获取账号的好友分组信息及每个分组中的好友列表
接口地址: https://napcat.apifox.cn/226658978e0.md

参数：
- refresh_token: 是否刷新令牌(可选)

返回：
- 包含所有好友分组及其中好友信息的数据结构
- 每个分组包含分组ID、分组名称及组内好友列表

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetFriendsWithCategoryReq(TypedDict):
    """
    获取好友分组列表 API 请求参数
    """
    refresh_token: bool | None  # 是否刷新令牌(可选)

class FriendInfo(TypedDict):
    """
    好友信息
    """
    user_id: int             # 好友QQ号
    nickname: str            # 好友昵称
    remark: str              # 好友备注
    avatar: str              # 头像URL

class FriendCategory(TypedDict):
    """
    好友分组信息
    """
    category_id: int              # 分组ID
    category_name: str            # 分组名称
    friends: list[FriendInfo]     # 分组内的好友列表

class FriendCategoryResult(TypedDict):
    """
    好友分组列表结果
    """
    categories: list[FriendCategory]  # 分组列表

class GetFriendsWithCategoryRes(BaseHttpResponse[FriendCategoryResult]):
    """
    获取好友分组列表 API 响应参数
    """
    pass