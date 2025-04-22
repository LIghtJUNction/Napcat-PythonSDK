# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 250286903e0
@endpoint: send_packet
@tags: 系统操作
@homepage: https://napcat.apifox.cn/250286903e0
@llms.txt: https://napcat.apifox.cn/250286903e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: send_packet API
@usage: 使用 `client.send_packet()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_packet"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SendPacketReq(BaseHttpRequest):
    """
    send_packet 请求参数
    """

    pass
# region req/

# region data
class SendPacketData(BaseModel):
    """
    send_packet 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendPacketRes(BaseHttpResponse[SendPacketData]):
    """
    send_packet 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendPacketAPI(BaseHttpAPI[SendPacketReq, SendPacketRes]):
    """
    发送自定义组包
    """
    api: str = "/send_packet"
    method: Literal["POST", "GET"] = "POST"

    Request = SendPacketReq
    Response = SendPacketRes

    request: SendPacketReq
    response: SendPacketRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendPacketAPI)

# region code/

