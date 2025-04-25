# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226656926e0
@llms.txt: https://napcat.apifox.cn/226656926e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:退群

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_leave"
__id__ = "226656926e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupLeaveReq(BaseModel):
    """
    退群请求模型
    """
    group_id: int | str = Field(..., description="群号")
# endregion req



# region res
class SetGroupLeaveRes(BaseModel):
    """
    退群响应模型
    """
    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="响应数据") # Based on OpenAPI override
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="补充说明")
    echo: str | None = Field(None, description="echo") # nullable field, default to None
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
