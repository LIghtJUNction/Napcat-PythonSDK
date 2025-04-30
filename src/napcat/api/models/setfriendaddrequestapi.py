# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656932e0
@llms.txt: https://napcat.apifox.cn/226656932e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:处理好友请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_friend_add_request"
__id__ = "226656932e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetFriendAddRequestReq(BaseModel):
    """
    处理好友请求 - 请求参数
    """

    flag: str = Field(..., description="请求id")
    approve: bool = Field(..., description="是否同意")
    remark: str = Field(..., description="好友备注")
# endregion req



# region res
class SetFriendAddRequestRes(BaseModel):
    """
    处理好友请求 - 响应参数
    """
    # 定义响应参数
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据") # Based on schema defining data as type null and required
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="补充信息")
    echo: str | None = Field(..., description="echo信息") # According to schema, echo is nullable and required

# endregion res

# region api
class SetFriendAddRequestAPI(BaseModel):
    """set_friend_add_request接口数据模型"""
    endpoint: str = "set_friend_add_request"
    method: str = "POST"
    Req: type[BaseModel] = SetFriendAddRequestReq
    Res: type[BaseModel] = SetFriendAddRequestRes
# endregion api




# endregion code
