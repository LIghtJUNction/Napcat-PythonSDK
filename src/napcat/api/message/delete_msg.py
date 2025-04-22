# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226919954e0
@endpoint: delete_msg
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226919954e0
@llms.txt: https://napcat.apifox.cn/226919954e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: delete_msg API
@usage: 使用 `client.delete_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_msg"
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
class DeleteMsgReq(BaseHttpRequest):
    """
    delete_msg 请求参数
    """

    pass
# region req/

# region data
class DeleteMsgData(BaseModel):
    """
    delete_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class DeleteMsgRes(BaseHttpResponse[None]):
    """
    delete_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class DeleteMsgAPI(BaseHttpAPI[DeleteMsgReq, DeleteMsgRes]):
    """
    撤回消息
    """
    api: str = "/delete_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = DeleteMsgReq
    Response = DeleteMsgRes

    request: DeleteMsgReq
    response: DeleteMsgRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(DeleteMsgAPI)

# region code/

