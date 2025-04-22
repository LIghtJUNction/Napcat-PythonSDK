# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 244510838e0
@endpoint: send_private_msg
@tags: 消息相关/发送私聊消息
@homepage: https://napcat.apifox.cn/244510838e0
@llms.txt: https://napcat.apifox.cn/244510838e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: 发送群消息
@usage: 使用 `client.send_private_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_msg"
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
class SendPrivateMsgReq(BaseHttpRequest):
    """
    send_private_msg 请求参数
    """

    pass
# region req/

# region data
class SendPrivateMsgData(BaseModel):
    """
    send_private_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendPrivateMsgRes(BaseHttpResponse[SendPrivateMsgData]):
    """
    send_private_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendPrivateMsgAPI(BaseHttpAPI[SendPrivateMsgReq, SendPrivateMsgRes]):
    """
    发送私聊文件
    """
    api: str = "/send_private_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = SendPrivateMsgReq
    Response = SendPrivateMsgRes

    request: SendPrivateMsgReq
    response: SendPrivateMsgRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendPrivateMsgAPI)

# region code/

