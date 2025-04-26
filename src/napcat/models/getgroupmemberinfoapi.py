# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657019e0
@llms.txt: https://napcat.apifox.cn/226657019e0.md
@last_update: 2025-04-27 00:53:40

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
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class user_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }

class 群成员信息(BaseModel):
    group_id: float = Field(description="group_id字段")
    user_id: float = Field(description="user_id字段")
    nickname: str = Field(description="nickname字段")
    card: str = Field(description="群昵称")
    sex: str = Field(description="性别")
    age: float = Field(description="年龄")
    area: str = Field(description="area字段")
    level: float = Field(description="群等级")
    qq_level: float = Field(description="账号等级")
    join_time: float = Field(description="加群时间")
    last_sent_time: float = Field(description="最后发言时间")
    title_expire_time: float = Field(description="title_expire_time字段")
    unfriendly: bool = Field(description="unfriendly字段")
    card_changeable: bool = Field(description="card_changeable字段")
    is_robot: bool = Field(description="是否机器人")
    shut_up_timestamp: float = Field(description="禁言时长")
    role: str = Field(description="权限")
    title: str = Field(description="头衔")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupMemberInfoReq(BaseModel):
    """获取群成员信息"""
    group_id: group_id
    user_id: user_id
    no_cache: bool

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupMemberInfoRes(BaseModel):
    """获取群成员信息"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupMemberInfoAPI(BaseModel):
    """get_group_member_info接口数据模型"""
    endpoint: str = "get_group_member_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupMemberInfoReq
    Res: type[BaseModel] = GetGroupMemberInfoRes

# region api/
# endregion code

