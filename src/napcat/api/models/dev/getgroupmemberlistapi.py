# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657034e0
@llms.txt: https://napcat.apifox.cn/226657034e0.md
@last_update: 2025-05-28 01:34:09

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
from pydantic import BaseModel, Field
from typing import Literal # Used for Literal["ok"]

# region component_models
# OpenAPI component schema: #/components/schemas/%E7%BE%A4%E6%88%90%E5%91%98%E4%BF%A1%E6%81%AF
class GroupMemberInfo(BaseModel):
    """群成员信息"""
    group_id: float = Field(description="群号")
    user_id: float = Field(description="用户ID")
    nickname: str = Field(description="昵称")
    card: str = Field(description="群昵称")
    sex: str = Field(description="性别")
    age: float = Field(description="年龄")
    area: str = Field(description="地区")
    level: float = Field(description="群等级")
    qq_level: float = Field(description="账号等级")
    join_time: float = Field(description="加群时间 (Unix时间戳)")
    last_sent_time: float = Field(description="最后发言时间 (Unix时间戳)")
    title_expire_time: float = Field(description="头衔过期时间 (Unix时间戳)")
    unfriendly: bool = Field(description="是否不友好（如被举报等）")
    card_changeable: bool = Field(description="群昵称是否可修改")
    is_robot: bool = Field(description="是否机器人")
    shut_up_timestamp: float = Field(description="禁言时长 (Unix时间戳)，0 表示未被禁言")
    role: str = Field(description="权限，可选值：owner (群主), admin (管理员), member (普通成员)")
    title: str = Field(description="专属头衔")

# region component_models/

# region req
class GetGroupMemberListReq(BaseModel):
    """获取群成员列表请求"""
    # OpenAPI: group_id: oneOf: [number, string] -> corresponds to `group_id` parameter directly
    group_id: str | float = Field(description="群号，可以是群ID（数字）或群名称（字符串）")
    # OpenAPI: no_cache: type: boolean, default: false -> optional parameter with default
    no_cache: bool = Field(default=False, description="是否不使用缓存，若为 True 则不使用缓存，强制拉取新数据")

# region req/


# region res
class GetGroupMemberListRes(BaseModel):
    """获取群成员列表响应"""
    # OpenAPI: status: const: ok
    status: Literal["ok"] = Field(description="状态码，固定为 'ok'")
    # OpenAPI: retcode: type: number
    retcode: float = Field(description="操作返回码")
    # OpenAPI: data: type: array, items: #/components/schemas/群成员信息
    data: list[GroupMemberInfo] = Field(description="群成员信息列表")
    # OpenAPI: message: type: string
    message: str = Field(description="提示信息")
    # OpenAPI: wording: str = Field(description="更详细的提示信息（人类可读）")
    wording: str = Field(description="更详细的提示信息（人类可读）")
    # OpenAPI: echo: type: string, nullable: true
    echo: str | None = Field(description="echo字段")

# region res/

# region api
class GetGroupMemberListAPI(BaseModel):
    """get_group_member_list接口数据模型"""
    endpoint: str = "get_group_member_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupMemberListReq
    Res: type[BaseModel] = GetGroupMemberListRes

# region api/
# endregion code
