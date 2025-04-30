# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656815e0
@llms.txt: https://napcat.apifox.cn/226656815e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置群管理

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_admin"
__id__ = "226656815e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class SetGroupAdminReq(BaseModel):
    """
    请求参数
    """

    group_id: int | str = Field(..., description="群号")
    user_id: int | str = Field(..., description="要设置管理员的QQ号")
    enable: bool = Field(..., description="是否设置为管理员")
# endregion req



# region res
class SetGroupAdminRes(BaseModel):
    """
    响应参数
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据，null表示成功")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo回显")
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