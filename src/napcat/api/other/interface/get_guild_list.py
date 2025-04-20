"""
获取频道服务器列表 API
用于获取机器人加入的频道服务器列表
接口地址: https://napcat.apifox.cn/227495429e0.md

参数：
无需参数

返回：
- 频道服务器列表

# NapCat 开发中
"""

from napcat.api.base.models import BaseHttpResponse
from pydantic import BaseModel

class GetGuildListReq(BaseModel):
    """
    获取频道服务器列表 API 请求参数
    """
    pass  # 无需参数

class GuildInfo(BaseModel):
    """
    频道服务器信息
    """
    guild_id: str       # 频道服务器ID
    guild_name: str     # 频道服务器名称
    guild_display_id: str  # 频道服务器显示ID
    member_count: int   # 成员数
    max_member_count: int  # 最大成员数
    description: str    # 描述
    create_time: int    # 创建时间
    is_owner: bool      # 是否为创建者

class GetGuildListRes(BaseHttpResponse[list[GuildInfo]]):
    """
    获取频道服务器列表 API 响应参数
    """
    pass