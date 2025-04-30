# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['群聊相关']
@homepage: https://napcat.apifox.cn/226656979e0
@llms.txt: https://napcat.apifox.cn/226656979e0.md
@last_update: 2025-04-27 00:53:40

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
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupInfoReq(BaseModel):
    """
    获取群信息请求参数
    """

    group_id: int | str = Field(..., description="群号")

# endregion req



# region res
class GetGroupInfoResData(BaseModel):
    """
    群信息数据
    """

    group_all_shut: int = Field(..., description="群是否开启全员禁言") # Assuming number is int
    group_remark: str = Field(..., description="群备注")
    group_id: str = Field(..., description="群号")
    group_name: str = Field(..., description="群名")
    member_count: int = Field(..., description="成员数量") # Assuming number is int
    max_member_count: int = Field(..., description="最大成员数量") # Assuming number is int


class GetGroupInfoRes(BaseModel):
    """
    获取群信息响应参数
    """
    # 定义响应参数

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码") # Assuming number is int
    data: GetGroupInfoResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="消息提示")
    echo: str | None = Field(None, description="echo") # Nullable field, set default to None

# endregion res

# region api
class GetGroupInfoAPI(BaseModel):
    """get_group_info接口数据模型"""
    endpoint: str = "get_group_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupInfoReq
    Res: type[BaseModel] = GetGroupInfoRes
# endregion api




# endregion code