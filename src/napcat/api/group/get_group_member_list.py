"""
获取群成员列表 API
用于获取群内所有成员的信息
接口地址: https://napcat.apifox.cn/227425563e0.md

参数：
- group_id: 群号
- no_cache: 是否不使用缓存

返回：
- 群成员列表

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupMemberListReq(BaseModel):
    """
    获取群成员列表 API 请求参数
    """
    group_id: int   # 群号
    no_cache: bool  # 是否不使用缓存

class GroupMember(BaseModel):
    """
    群成员信息
    """
    group_id: int         # 群号
    user_id: int          # QQ号
    nickname: str         # 昵称
    card: str             # 群名片
    sex: str              # 性别
    age: int              # 年龄
    area: str             # 地区
    join_time: int        # 入群时间
    last_sent_time: int   # 最后发言时间
    level: str            # 等级
    role: str             # 角色，owner或admin或member
    unfriendly: bool      # 是否不良记录成员
    title: str            # 专属头衔
    title_expire_time: int # 专属头衔过期时间
    card_changeable: bool # 是否允许修改群名片

class GetGroupMemberListRes(BaseHttpResponse[list[GroupMember]]):
    """
    获取群成员列表 API 响应参数
    """
    pass