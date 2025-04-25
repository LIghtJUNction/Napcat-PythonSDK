# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656815e0
@llms.txt: https://napcat.apifox.cn/226656815e0.md
@last_update: 2025-04-26 01:17:44

@description: 设置群管理

summary: 设置群管理

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_admin"
__id__ = "226656815e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Used for status='ok'

logger = logging.getLogger(__name__)

# region req
class SetGroupAdminReq(BaseModel):
    """
    设置群管理 请求模型
    """
    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="要设置管理员的 QQ 号")
    enable: bool = Field(..., description="是否设置管理员，true 为设置，false 为取消")

# endregion req



# region res
class SetGroupAdminRes(BaseModel):
    """
    设置群管理 响应模型
    """
    status: Literal['ok'] = Field(..., description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据") # According to OpenAPI spec override, data should be null
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="Echo信息")

# endregion res

# region api
class SetGroupAdminAPI(BaseModel):
    """set_group_admin接口数据模型"""
    endpoint: str = "set_group_admin"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupAdminReq
    Res: type[BaseModel] = SetGroupAdminRes
# endregion api




# endregion code
