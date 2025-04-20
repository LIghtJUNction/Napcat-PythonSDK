"""
获取陌生人信息 API
用于获取非好友用户的基本信息
接口地址: https://napcat.apifox.cn/227060201e0.md

参数：
- user_id: 要查询的QQ号
- no_cache: 是否不使用缓存（使用缓存可能更新不及时，但响应更快）

返回：
- 陌生人用户的基本信息，包含QQ号、昵称等

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class GetStrangerInfoReq(TypedDict):
    """
    获取陌生人信息 API 请求参数
    """
    user_id: int  # 要查询的QQ号
    no_cache: bool  # 是否不使用缓存

class StrangerInfo(TypedDict):
    """
    陌生人信息
    """
    user_id: int       # QQ号
    nickname: str      # 昵称
    sex: str           # 性别
    age: int           # 年龄
    qid: str           # QID
    level: int         # 等级
    login_days: int    # 登录天数

class GetStrangerInfoRes(BaseHttpResponse[StrangerInfo]):
    """
    获取陌生人信息 API 响应参数
    """
    pass