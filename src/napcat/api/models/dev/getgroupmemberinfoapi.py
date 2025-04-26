# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
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
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupMemberInfoReq(BaseModel):
    """
    获取群成员信息的请求模型
    """
    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="成员QQ号")
    no_cache: bool = Field(..., description="是否不使用缓存")
# endregion req



# region res
class GetGroupMemberInfoRes(BaseModel):
    """
    获取群成员信息的响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="echo")

    class GroupMemberInfoData(BaseModel):
        """
        群成员信息数据模型
        """
        group_id: int = Field(..., description="群号")
        user_id: int = Field(..., description="成员QQ号")
        nickname: str = Field(..., description="昵称")
        card: str = Field(..., description="群昵称")
        sex: str = Field(..., description="性别")
        age: int = Field(..., description="年龄")
        area: str = Field(..., description="地区")
        level: int = Field(..., description="群等级")
        qq_level: int = Field(..., description="账号等级")
        join_time: int = Field(..., description="加群时间")
        last_sent_time: int = Field(..., description="最后发言时间")
        title_expire_time: int = Field(..., description="头衔过期时间")
        unfriendly: bool = Field(..., description="是否不友好")
        card_changeable: bool = Field(..., description="群昵称是否可更改")
        is_robot: bool = Field(..., description="是否机器人")
        shut_up_timestamp: int = Field(..., description="禁言时长")
        role: str = Field(..., description="权限")
        title: str = Field(..., description="头衔")

    data: GroupMemberInfoData = Field(..., description="群成员信息数据")

# endregion res

# region api
class GetGroupMemberInfoAPI(BaseModel):
    """get_group_member_info接口数据模型"""
    endpoint: str = "get_group_member_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupMemberInfoReq
    Res: type[BaseModel] = GetGroupMemberInfoRes
# endregion api




# endregion code
