# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658889e0
@llms.txt: https://napcat.apifox.cn/226658889e0.md
@last_update: 2025-04-26 01:17:44

@description: 相当于http的快速操作

summary:.对事件执行快速操作

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".handle_quick_operation"
__id__ = "226658889e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class HandleQuickOperationReq(BaseModel):
    """
    对事件执行快速操作的请求模型
    """

    context: dict = Field(..., description="事件数据对象")
    operation: dict = Field(..., description="快速操作对象")
# endregion req



# region res
class HandleQuickOperationRes(BaseModel):
    """
    对事件执行快速操作的响应模型
    """

    status: Literal["ok"] = Field("ok", description="响应状态")
    retcode: int | float = Field(..., description="响应码")
    data: None = Field(None, description="响应数据，应为null")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="补充说明")
    echo: str | None = Field(None, description="回传的echo")
# endregion res

# region api
class HandleQuickOperationAPI(BaseModel):
    ".handle_quick_operation接口数据模型"
    endpoint: str = ".handle_quick_operation"
    method: str = "POST"
    Req: type[BaseModel] = HandleQuickOperationReq
    Res: type[BaseModel] = HandleQuickOperationRes
# endregion api




# endregion code
