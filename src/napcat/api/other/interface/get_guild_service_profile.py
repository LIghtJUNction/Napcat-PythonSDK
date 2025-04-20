"""
获取频道资料卡片 API
用于获取频道服务器的资料卡片信息
接口地址: https://napcat.apifox.cn/227495445e0.md

参数：
- guild_id: 频道服务器ID

返回：
- 频道资料卡片信息

# NapCat 开发中
"""

from napcat.api.base.types import BaseHttpResponse
from pydantic import BaseModel

class GetGuildServiceProfileReq(BaseModel):
    """
    获取频道资料卡片 API 请求参数
    """
    guild_id: str  # 频道服务器ID

class GuildServiceProfile(BaseModel):
    """
    频道资料卡片信息
    """
    guild_id: str          # 频道服务器ID
    guild_name: str        # 频道服务器名称
    guild_profile: str     # 频道简介
    create_time: int       # 创建时间
    avatar_url: str        # 头像URL
    owner_id: str          # 创建者ID
    owner_name: str        # 创建者名称
    member_count: int      # 成员数
    max_member_count: int  # 最大成员数

class GetGuildServiceProfileRes(BaseHttpResponse[GuildServiceProfile]):
    """
    获取频道资料卡片 API 响应参数
    """
    pass