# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/227245941e0
@llms.txt: https://napcat.apifox.cn/227245941e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取群 @全体成员 剩余次数

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_at_all_remain"
__id__ = "227245941e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class GetGroupAtAllRemainReq(BaseModel):
    """
    获取群 @全体成员 剩余次数的请求模型
    """

    group_id: int | str = Field(..., description="群号")

# endregion req



# region res
class GetGroupAtAllRemainResData(BaseModel):
    """
    获取群 @全体成员 剩余次数响应数据模型
    """
    can_at_all: bool = Field(..., description="是否可以 @全体成员")
    remain_at_all_count_for_group: int = Field(..., description="群内 @全体成员 剩余次数")
    remain_at_all_count_for_uin: int = Field(..., description="帐号 @全体成员 剩余次数")


class GetGroupAtAllRemainRes(BaseModel):
    """
    获取群 @全体成员 剩余次数的响应模型
    """
    status: str = Field(..., description="响应状态", pattern="^ok$")
    retcode: int = Field(..., description="返回码")
    data: GetGroupAtAllRemainResData = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误信息 (更详细)")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class GetGroupAtAllRemainAPI(BaseModel):
    """get_group_at_all_remain接口数据模型"""
    endpoint: str = "get_group_at_all_remain"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupAtAllRemainReq
    Res: type[BaseModel] = GetGroupAtAllRemainRes
# endregion api

# endregion code