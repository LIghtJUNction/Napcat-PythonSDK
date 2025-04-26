# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659234e0
@llms.txt: https://napcat.apifox.cn/226659234e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取被过滤的加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_ignore_add_request"
__id__ = "226659234e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupIgnoreAddRequestReq(BaseModel):
    """
    获取被过滤的加群请求 - 请求模型
    
    该接口不需要请求参数。
    """

    pass
# endregion req



# region res
class GroupIgnoreAddRequestItem(BaseModel):
    """
    被过滤的加群请求项
    """
    request_id: int = Field(..., description="加群请求ID")
    invitor_uin: int = Field(..., description="邀请者QQ号")
    invitor_nick: str | None = Field(..., description="邀请者昵称", nullable=True)
    group_id: int | None = Field(..., description="群号", nullable=True)
    message: str | None = Field(..., description="加群消息", nullable=True)
    group_name: str | None = Field(..., description="群名称", nullable=True)
    checked: bool = Field(..., description="是否已处理（true为已处理，false为未处理）")
    actor: int = Field(..., description="处理者QQ号")
    requester_nick: str | None = Field(..., description="请求者昵称", nullable=True)


class GetGroupIgnoreAddRequestRes(BaseModel):
    """
    获取被过滤的加群请求 - 响应模型
    """
    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: list[GroupIgnoreAddRequestItem] = Field(..., description="被过滤的加群请求列表")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="用户附加数据", nullable=True)
# endregion res

# region api
class GetGroupIgnoreAddRequestAPI(BaseModel):
    """get_group_ignore_add_request接口数据模型"""
    endpoint: str = "get_group_ignore_add_request"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupIgnoreAddRequestReq
    Res: type[BaseModel] = GetGroupIgnoreAddRequestRes
# endregion api




# endregion code