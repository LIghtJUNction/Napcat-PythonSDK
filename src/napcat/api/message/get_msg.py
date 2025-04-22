# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226656707e0
@endpoint: get_msg
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226656707e0
@llms.txt: https://napcat.apifox.cn/226656707e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:49

@description: get_msg API
@usage: 使用 `client.get_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_msg"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetMsgReq(BaseHttpRequest):
    """
    get_msg 请求参数
    """

    pass
# region req/

# region data
class GetMsgData(BaseModel):
    """
    get_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetMsgRes(BaseHttpResponse[GetMsgData]):
    """
    get_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetMsgAPI(BaseHttpAPI[GetMsgReq, GetMsgRes]):
    """
    获取消息详情
    """
    api: str = "/get_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = GetMsgReq
    Response = GetMsgRes

    request: GetMsgReq
    response: GetMsgRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetMsgAPI)

# region code/

