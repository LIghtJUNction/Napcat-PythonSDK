# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658889e0
@llms.txt: https://napcat.apifox.cn/226658889e0.md
@last_update: 2025-05-28 01:34:09

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
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class HandleQuickOperationReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class HandleQuickOperationRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class HandleQuickOperationAPI(BaseModel):
    """.handle_quick_operation接口数据模型"""
    endpoint: str = ".handle_quick_operation"
    method: str = "POST"
    Req: type[BaseModel] = HandleQuickOperationReq
    Res: type[BaseModel] = HandleQuickOperationRes
# endregion api




# endregion code

