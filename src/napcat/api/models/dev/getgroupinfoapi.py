# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656979e0
@llms.txt: https://napcat.apifox.cn/226656979e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_info"
__id__ = "226656979e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
class GroupInfo(BaseModel):
    group_all_shut: float = Field(..., description="群禁言状态")
    group_remark: str = Field(..., description="群备注")
    group_id: str = Field(..., description="群号")
    group_name: str = Field(..., description="群名")
    member_count: float = Field(..., description="成员数量")
    max_member_count: float = Field(..., description="最大成员数量")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupInfoReq(BaseModel):
    """获取群信息请求模型"""
    group_id: int | str = Field(..., description="群号或标识ID")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupInfoRes(BaseModel):
    """获取群信息响应模型"""
    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: float = Field(..., description="返回码")
    data: GroupInfo = Field(..., description="群信息数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupInfoAPI(BaseModel):
    """get_group_info接口数据模型"""
    endpoint: str = "get_group_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupInfoReq
    Res: type[BaseModel] = GetGroupInfoRes

# region api/
# endregion code
