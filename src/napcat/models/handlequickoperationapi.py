# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658889e0
@llms.txt: https://napcat.apifox.cn/226658889e0.md
@last_update: 2025-04-23 20:23:17

@description: 相当于http的快速操作

summary:.对事件执行快速操作

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".handle_quick_operation"
__id__ = "226658889e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class .handleQuickOperationReq(BaseModel):
    """
    请求参数
    """

    context: dict = Field(..., description="事件数据对象")
    operation: dict = Field(..., description="快速操作对象")
# region req/


# region res
class .handleQuickOperationRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class .handleQuickOperationAPI(BaseModel):
    
    Request : type[.handleQuickOperationReq] = .handleQuickOperationReq
    Response  : type[.handleQuickOperationRes] = .handleQuickOperationRes


# region api/
# region code/

