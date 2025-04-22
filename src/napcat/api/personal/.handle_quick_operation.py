# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226658889e0
@endpoint: .handle_quick_operation
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226658889e0
@llms.txt: https://napcat.apifox.cn/226658889e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: 相当于http的快速操作
@usage: 使用 `client..handle_quick_operation()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".handle_quick_operation"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    -
    -
    -
    -
    -
    -
    -
    # 本行注释旨在测试构建清理逻辑


# region req
class HandleQuickOperationReq(BaseHttpRequest):
    """
    .handle_quick_operation 请求参数
    """

    pass
# region req/

# region data
class HandleQuickOperationData(BaseModel):
    """
    .handle_quick_operation 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class HandleQuickOperationRes(BaseHttpResponse[None]):
    """
    .handle_quick_operation 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class HandleQuickOperationAPI(BaseHttpAPI[HandleQuickOperationReq, HandleQuickOperationRes]):
    """
    .对事件执行快速操作
    """
    api: str = "/.handle_quick_operation"
    method: Literal["POST", "GET"] = "POST"

    Request = HandleQuickOperationReq
    Response = HandleQuickOperationRes

    request: HandleQuickOperationReq
    response: HandleQuickOperationRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(HandleQuickOperationAPI)

# region code/

