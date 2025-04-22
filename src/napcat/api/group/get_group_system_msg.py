# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658660e0
@endpoint: get_group_system_msg
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658660e0
@llms.txt: https://napcat.apifox.cn/226658660e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: get_group_system_msg API
@usage: 使用 `client.get_group_system_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_system_msg"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetGroupSystemMsgReq(BaseHttpRequest):
    """
    get_group_system_msg 请求参数
    """

    pass
# region req/

# region data
class GetGroupSystemMsgData(BaseModel):
    """
    get_group_system_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupSystemMsgRes(BaseHttpResponse[GetGroupSystemMsgData]):
    """
    get_group_system_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupSystemMsgAPI(BaseHttpAPI[GetGroupSystemMsgReq, GetGroupSystemMsgRes]):
    """
    获取群系统消息
    """
    api: str = "/get_group_system_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupSystemMsgReq
    Response = GetGroupSystemMsgRes

    request: GetGroupSystemMsgReq
    response: GetGroupSystemMsgRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupSystemMsgAPI)

# region code/

