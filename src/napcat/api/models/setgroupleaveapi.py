# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656926e0
@llms.txt: https://napcat.apifox.cn/226656926e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:退群

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_group_leave"
__id__ = "226656926e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class SetGroupLeaveReq(BaseModel):
    """
    退群请求参数
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    is_dismiss: bool | None = Field(
        None, description="是否解散群，如果登录号是群主，则填写true，否则填写false"
    )

# endregion req



# region res
class SetGroupLeaveRes(BaseModel):
    """
    退群响应参数
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据 (固定为 null)") # Data is explicitly null in the spec
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应文本")
    echo: str | None = Field(None, description="echo回显")

# endregion res

# region api
class SetGroupLeaveAPI(BaseModel):
    """set_group_leave接口数据模型"""
    endpoint: str = "set_group_leave"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupLeaveReq
    Res: type[BaseModel] = SetGroupLeaveRes
# endregion api




# endregion code