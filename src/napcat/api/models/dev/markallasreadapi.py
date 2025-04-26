# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659194e0
@llms.txt: https://napcat.apifox.cn/226659194e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:_设置所有消息已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_mark_all_as_read"
__id__ = "226659194e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal # Import Literal for fixed string value
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class MarkAllAsReadReq(BaseModel):
    """
    设置所有消息已读请求模型
    """
    # API spec indicates an empty request body, so no fields needed.
    pass
# endregion req



# region res
class MarkAllAsReadRes(BaseModel):
    """
    设置所有消息已读响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    # According to the spec, 'data' must be null.
    data: None = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class MarkAllAsReadAPI(BaseModel):
    """_mark_all_as_read接口数据模型"""
    endpoint: str = "_mark_all_as_read"
    method: str = "POST"
    Req: type[BaseModel] = MarkAllAsReadReq
    Res: type[BaseModel] = MarkAllAsReadRes
# endregion api




# endregion code