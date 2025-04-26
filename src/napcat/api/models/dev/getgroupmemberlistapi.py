# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: group
@homepage: https://napcat.apifox.cn/226657034e0
@llms.txt: https://napcat.apifox.cn/226657034e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取群成员列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_member_list"
__id__ = "226657034e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupMemberListReq(BaseModel):
    """
    获取群成员列表请求参数
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    no_cache: bool = Field(
        False, description="是否不使用缓存"
    )

# endregion req


# region res
class GroupMemberInfo(BaseModel):
    """
    群成员信息
    """
    group_id: int = Field(..., description="群号")
    user_id: int = Field(..., description="用户ID")
    nickname: str = Field(..., description="昵称")
    card: str = Field(..., description="群昵称")
    sex: str = Field(..., description="性别")
    age: int = Field(..., description="年龄")
    area: str = Field(..., description="地区")
    level: int = Field(..., description="群等级")
    qq_level: int = Field(..., description="账号等级")
    join_time: int = Field(..., description="加群时间")
    last_sent_time: int = Field(..., description="最后发言时间")
    title_expire_time: int = Field(..., description="头衔到期时间") # Note: Description missing in schema, added placeholder
    unfriendly: bool = Field(..., description="是否不友好") # Note: Description missing in schema, added placeholder
    card_changeable: bool = Field(..., description="群名片是否可修改") # Note: Description missing in schema, added placeholder
    is_robot: bool = Field(..., description="是否机器人")
    shut_up_timestamp: int = Field(..., description="禁言时长")
    role: str = Field(..., description="权限") # Note: Could be Literal['owner', 'admin', 'member'] if schema specified
    title: str = Field(..., description="头衔")


class GetGroupMemberListRes(BaseModel):
    """
    获取群成员列表响应参数
    """

    status: Literal["ok"] = Field(
        ..., description="状态"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: list[GroupMemberInfo] = Field(
        ..., description="群成员信息列表"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="提示"
    )
    echo: str | None = Field(
        ..., description="回显"
    )

# endregion res

# region api
class GetGroupMemberListAPI(BaseModel):
    """get_group_member_list接口数据模型"""
    endpoint: str = "get_group_member_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupMemberListReq
    Res: type[BaseModel] = GetGroupMemberListRes
# endregion api


# endregion code
