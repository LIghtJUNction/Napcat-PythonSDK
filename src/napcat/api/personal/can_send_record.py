# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226657080e0
@endpoint: can_send_record
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226657080e0
@llms.txt: https://napcat.apifox.cn/226657080e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: can_send_record API
@usage: 使用 `client.can_send_record()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "can_send_record"
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
class CanSendRecordReq(BaseHttpRequest):
    """
    can_send_record 请求参数
    """

    pass
# region req/

# region data
class CanSendRecordData(BaseModel):
    """
    can_send_record 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class CanSendRecordRes(BaseHttpResponse[CanSendRecordData]):
    """
    can_send_record 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class CanSendRecordAPI(BaseHttpAPI[CanSendRecordReq, CanSendRecordRes]):
    """
    检查是否可以发送语音
    """
    api: str = "/can_send_record"
    method: Literal["POST", "GET"] = "POST"

    Request = CanSendRecordReq
    Response = CanSendRecordRes

    request: CanSendRecordReq
    response: CanSendRecordRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(CanSendRecordAPI)

# region code/

