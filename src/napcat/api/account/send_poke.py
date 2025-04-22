# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 250286923e0
@endpoint: send_poke
@tags: 账号相关
@homepage: https://napcat.apifox.cn/250286923e0
@llms.txt: https://napcat.apifox.cn/250286923e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: send_poke API
@usage: 使用 `client.send_poke()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_poke"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SendPokeReq(BaseHttpRequest):
    """
    send_poke 请求参数
    """

    pass
# region req/

# region data
class SendPokeData(BaseModel):
    """
    send_poke 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendPokeRes(BaseHttpResponse[None]):
    """
    send_poke 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendPokeAPI(BaseHttpAPI[SendPokeReq, SendPokeRes]):
    """
    发送戳一戳
    """
    api: str = "/send_poke"
    method: Literal["POST", "GET"] = "POST"

    Request = SendPokeReq
    Response = SendPokeRes

    request: SendPokeReq
    response: SendPokeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendPokeAPI)

# region code/

