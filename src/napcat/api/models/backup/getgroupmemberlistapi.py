# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226657034e0
@llms.txt: https://napcat.apifox.cn/226657034e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群成员列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_member_list"
__id__ = "226657034e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupMemberListReq(BaseModel):
    """
    获取群成员列表请求体
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    no_cache: bool = Field(
        default=False, description="是否不使用缓存，如果为true则全量获取"
    )
# endregion req



# region res
class GetGroupMemberListRes(BaseModel):
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")

    status: str = Field(..., description="状态, 例如: ok, async, failed")
    retcode: int = Field(..., description="状态码, 例如: 0")
    data: list[dict] = Field(
        ..., description="响应数据"
    )
    message: str = Field(
        ..., description="错误信息, 仅在 status 为 failed 时有效"
    )
    wording: str = Field(
        ..., description="错误信息的自然语言描述, 仅在 status 为 failed 时有效"
    )
    echo: str | None = Field(
        default=None, description="可以提供 echo 给 api 调用方, 方便 api 调用方识别是哪次请求的响应"
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
