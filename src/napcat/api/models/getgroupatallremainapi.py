# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/227245941e0
@llms.txt: https://napcat.apifox.cn/227245941e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取群 @全体成员 剩余次数

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_at_all_remain"
__id__ = "227245941e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupAtAllRemainReq(BaseModel):
    """
    获取群 @全体成员 剩余次数请求参数
    """
    group_id: int | str = Field(
        ..., description="群号"
    )
# endregion req



# region res
class GetGroupAtAllRemainRes(BaseModel):
    """
    获取群 @全体成员 剩余次数响应参数
    """
    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="提示信息"
    )
    echo: str | None = Field(
        None, description="echo"
    )

    class Data(BaseModel):
        """
        响应数据
        """
        can_at_all: bool = Field(
            ..., description="是否可以 @全体成员"
        )
        remain_at_all_count_for_group: float = Field(
            ..., description="群内所有管理员的 @全体成员 剩余次数"
        )
        remain_at_all_count_for_uin: float = Field(
            ..., description="当前用户 @全体成员 剩余次数"
        )

    data: Data = Field(
        ..., description="响应数据"
    )
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
