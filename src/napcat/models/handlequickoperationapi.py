# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226658889e0
@endpoint: .handle_quick_operation
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658889e0
@llms.txt: https://napcat.apifox.cn/226658889e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 相当于http的快速操作

summary:.对事件执行快速操作

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".handle_quick_operation"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class .handleQuickOperationReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class .handleQuickOperationRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class .handleQuickOperationAPI(BaseModel):
    
    Request : type[.handleQuickOperationReq] = .handleQuickOperationReq
    Response  : type[.handleQuickOperationRes] = .handleQuickOperationRes


# region api/




# region code/

