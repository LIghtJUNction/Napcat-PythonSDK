# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659234e0
@llms.txt: https://napcat.apifox.cn/226659234e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取被过滤的加群请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_ignore_add_request"
__id__ = "226659234e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupIgnoreAddRequestReq(BaseModel):
    """
    获取被过滤的加群请求请求模型
    "

    pass
# endregion req



# region res
class GroupIgnoreAddRequestData(BaseModel):
    """
    被过滤的加群请求数据项模型
    """
    request_id: int = Field(..., description="请求ID")
    invitor_uin: int = Field(..., description="邀请者UIN")
    invitor_nick: str | None = Field(None, description="邀请者昵称")
    group_id: int | None = Field(None, description="群号")
    message: str | None = Field(None, description="附言")
    group_name: str | None = Field(None, description="群名称")
    checked: bool = Field(..., description="是否已处理")
    actor: int = Field(..., description="处理者UIN，没有则为0")
    requester_nick: str | None = Field(None, description="请求者昵称")

class GetGroupIgnoreAddRequestRes(BaseModel):
    """
    获取被过滤的加群请求响应模型
    """
    status: str = Field("ok", description="状态") # Assuming 'ok' is the constant value based on spec
    retcode: int = Field(..., description="返回码")
    data: list[GroupIgnoreAddRequestData] = Field(..., description="被过滤的加群请求列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="echo")
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