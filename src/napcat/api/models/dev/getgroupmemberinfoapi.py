# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226657019e0
@llms.txt: https://napcat.apifox.cn/226657019e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群成员信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_member_info"
__id__ = "226657019e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
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
    title_expire_time: float = Field(description="头衔过期时间 (Unix时间戳, 0为永久)")
    unfriendly: bool = Field(description="是否不友好")
    card_changeable: bool = Field(description="群昵称是否可更改")
    is_robot: bool = Field(description="是否机器人")
    shut_up_timestamp: float = Field(description="禁言时长 (Unix时间戳, 0为未禁言)")
    role: str = Field(description="权限 (owner/admin/member)")
    title: str = Field(description="专属头衔")

    model_config = {
        "extra": "allow",
    }
# endregion component_models/

# region req
class GetGroupMemberInfoReq(BaseModel):
    """获取群成员信息请求模型"""
    group_id: float | str = Field(description="群号或群ID")
    user_id: float | str = Field(description="用户ID")
    no_cache: bool = Field(description="是否不使用缓存，强制获取最新数据")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class GetGroupMemberInfoRes(BaseModel):
    """获取群成员信息响应模型"""
    status: Literal["ok"] = Field(description="响应状态，固定为 'ok'")
    retcode: float = Field(default=0.0, description="状态码")
    data: GroupMemberInfo = Field(description="群成员详细信息")
    message: str = Field(default="", description="提示信息")
    wording: str = Field(default="", description="额外提示信息")
    echo: str | None = Field(default=None, description="回显字段")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class GetGroupMemberInfoAPI(BaseModel):
    """get_group_member_info接口数据模型"""
    endpoint: Literal["get_group_member_info"] = "get_group_member_info"
    method: Literal["POST"] = "POST"
    Req: type[BaseModel] = GetGroupMemberInfoReq
    Res: type[BaseModel] = GetGroupMemberInfoRes

# endregion api/
# endregion code