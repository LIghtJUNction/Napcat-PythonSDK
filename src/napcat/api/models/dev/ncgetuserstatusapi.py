# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659292e0
@llms.txt: https://napcat.apifox.cn/226659292e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取用户状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "nc_get_user_status"
__id__ = "226659292e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class NcGetUserStatusReq(BaseModel):
    """
    请求数据模型
    """

    user_id: int | str = Field(..., description="用户ID")

# endregion req



# region res
class NcGetUserStatusRes(BaseModel):
    """
    响应数据模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        status: int = Field(..., description="用户状态")
        ext_status: int = Field(..., description="用户扩展状态")

    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="状态码")
    data: Data = Field(..., description="响应数据详情")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显") # Changed from default to None for nullable field

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
