# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226659292e0
@llms.txt: https://napcat.apifox.cn/226659292e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取用户状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_user_status"
__id__ = "226659292e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field


# region req
class NcGetUserStatusReq(BaseModel):
    """
    获取用户状态请求模型
    """

    user_id: int | str = Field(
        ..., description="用户 ID"
    )


# endregion req


# region res
class NcGetUserStatusResData(BaseModel):
    """
    获取用户状态响应数据模型
    """
    status: float = Field(..., description="用户状态")
    ext_status: float = Field(..., description="用户扩展状态")


class NcGetUserStatusRes(BaseModel):
    """
    获取用户状态响应模型
    """

    status: str = Field(
        "ok", Literal["ok"], description="响应状态"
    )
    retcode: int = Field(..., description="返回码")
    data: NcGetUserStatusResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="回显")


# endregion res


# region api
class NcGetUserStatusAPI(BaseModel):
    """nc_get_user_status接口数据模型"""

    endpoint: str = "nc_get_user_status"
    method: str = "POST"
    Req: type[BaseModel] = NcGetUserStatusReq
    Res: type[BaseModel] = NcGetUserStatusRes


# endregion api


# endregion code