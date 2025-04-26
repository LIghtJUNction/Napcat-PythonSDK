# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658889e0
@llms.txt: https://napcat.apifox.cn/226658889e0.md
@last_update: 2025-04-27 00:53:40

@description: 相当于http的快速操作

summary:.对事件执行快速操作

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = ".handle_quick_operation"
__id__ = "226658889e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class HandleQuickOperationReq(BaseModel): # type: ignore
    """
    对事件执行快速操作的请求模型
    """

    context: dict = Field(..., description="事件数据对象")
    operation: dict = Field(..., description="快速操作对象")

# endregion req



# region res
class HandleQuickOperationRes(BaseModel): # type: ignore
    """
    对事件执行快速操作的响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: None = Field(..., description="数据字段，此处为null") # OpenAPI spec overrides data to null
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="回显，可能为null")

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
