# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226656652e0
@endpoint: send_msg
@tags: 其他/保留
@homepage: https://napcat.apifox.cn/226656652e0
@llms.txt: https://napcat.apifox.cn/226656652e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: send_msg API
@usage: 使用 `client.send_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_msg"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SendMsgReq(BaseHttpRequest):
    """
    send_msg 请求参数
    """

    pass
# region req/

# region data
class SendMsgData(BaseModel):
    """
    send_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendMsgRes(BaseHttpResponse[SendMsgData]):
    """
    send_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendMsgAPI(BaseHttpAPI[SendMsgReq, SendMsgRes]):
    """
    send_msg
    """
    api: str = "/send_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = SendMsgReq
    Response = SendMsgRes

    request: SendMsgReq
    response: SendMsgRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendMsgAPI)

# region code/

