# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226657401e0
@endpoint: get_group_msg_history
@tags: 消息相关
@homepage: https://napcat.apifox.cn/226657401e0
@llms.txt: https://napcat.apifox.cn/226657401e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: get_group_msg_history API
@usage: 使用 `client.get_group_msg_history()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_msg_history"
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
class GetGroupMsgHistoryReq(BaseHttpRequest):
    """
    get_group_msg_history 请求参数
    """

    pass
# region req/

# region data
class GetGroupMsgHistoryData(BaseModel):
    """
    get_group_msg_history 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupMsgHistoryRes(BaseHttpResponse[GetGroupMsgHistoryData]):
    """
    get_group_msg_history 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupMsgHistoryAPI(BaseHttpAPI[GetGroupMsgHistoryReq, GetGroupMsgHistoryRes]):
    """
    获取群历史消息
    """
    api: str = "/get_group_msg_history"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupMsgHistoryReq
    Response = GetGroupMsgHistoryRes

    request: GetGroupMsgHistoryReq
    response: GetGroupMsgHistoryRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupMsgHistoryAPI)

# region code/

