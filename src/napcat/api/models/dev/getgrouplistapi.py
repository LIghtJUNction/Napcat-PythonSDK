# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656992e0
@llms.txt: https://napcat.apifox.cn/226656992e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_list"
__id__ = "226656992e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
class GroupInfo(BaseModel):
    """群信息模型"""
    group_all_shut: float = Field(description="群是否全员禁言")
    group_remark: str = Field(description="群备注")
    group_id: str = Field(description="群号")
    group_name: str = Field(description="群名")
    member_count: float = Field(description="成员数量")
    max_member_count: float = Field(description="最大成员数量")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupListReq(BaseModel):
    """获取群列表请求模型"""
    no_cache: bool = Field(default=False, description="是否不使用缓存")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupListRes(BaseModel):
    """获取群列表响应模型"""
    status: Literal["ok"] = Field(default="ok", description="状态码")
    retcode: float = Field(default=0.0, description="返回码")
    data: list[GroupInfo] = Field(default_factory=list, description="群信息列表")
    message: str = Field(default="", description="信息")
    wording: str = Field(default="", description="提示语")
    echo: str | None = Field(default=None, description="回显")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupListAPI(BaseModel):
    """get_group_list接口数据模型"""
    endpoint: str = "get_group_list"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupListReq
    Res: type[BaseModel] = GetGroupListRes

# region api/
# endregion code
