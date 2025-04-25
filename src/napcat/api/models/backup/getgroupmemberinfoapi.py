# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226657019e0
@llms.txt: https://napcat.apifox.cn/226657019e0.md
@last_update: 2025-04-26 01:17:44

@description: 获取群成员信息

summary:获取群成员信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_member_info"
__id__ = "226657019e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupMemberInfoReq(BaseModel):
    """
    请求体模型: 获取群成员信息
    """

    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="用户ID")
    no_cache: bool = Field(..., description="是否不使用缓存")

# endregion req



# region res
class GetGroupMemberInfoRes(BaseModel):
    """
    响应体模型: 获取群成员信息
    """

    status: str = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: dict = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应文字")
    echo: str | None = Field(None, description="echo") # Changed to None default as per nullable: true

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
