"""
获取单向好友列表 API
用于获取单向好友列表（对方已将你加为好友，但你尚未添加对方）
接口地址: https://napcat.apifox.cn/266151878e0.md

参数：
无需参数

返回：
- 单向好友的列表数据，包含单向好友的QQ号、昵称等基本信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse

class GetUnidirectionalFriendListReq(TypedDict):
    """
    获取单向好友列表 API 请求参数
    """
    pass  # 无请求参数

class UnidirectionalFriend(TypedDict):
    """
    单向好友信息
    """
    user_id: int            # 好友QQ号
    nickname: str           # 好友昵称
    sex: str                # 好友性别
    age: int                # 好友年龄
    add_time: int           # 添加时间戳

class GetUnidirectionalFriendListRes(BaseHttpResponse[list[UnidirectionalFriend]]):
    """
    获取单向好友列表 API 响应参数
    """
    pass