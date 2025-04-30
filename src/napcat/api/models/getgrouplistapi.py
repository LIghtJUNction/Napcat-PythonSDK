# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656992e0
@llms.txt: https://napcat.apifox.cn/226656992e0.md
@last_update: 2025-04-27 00:53:40

@description: 获取群列表

summary:获取群列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_list"
__id__ = "226656992e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# logger = logging.getLogger(__name__)

# region req
class GetGroupListReq(BaseModel):
    """
    获取群列表请求模型
    """
    no_cache: bool = Field(default=False, description="不缓存")
# endregion req


# region res
class GroupInfo(BaseModel):
    """
    群信息模型
    """
    group_all_shut: int = Field(..., description="是否全员禁言")
    group_remark: str = Field(..., description="群备注")
    group_id: str = Field(..., description="群号")
    group_name: str = Field(..., description="群名")
    member_count: int = Field(..., description="成员数量")
    max_member_count: int = Field(..., description="最大成员数量")

class GetGroupListRes(BaseModel):
    """
    获取群列表响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[GroupInfo] = Field(..., description="群信息列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(default=None, description="回显数据")
# endregion res

# region api
class GetGroupListAPI(BaseModel):
    """get_group_list接口数据模型"""
    endpoint: str = "get_group_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupListReq
    Res: type[BaseModel] = GetGroupListRes
# endregion api




# endregion code
