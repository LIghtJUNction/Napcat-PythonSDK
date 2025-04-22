# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226656717e0
@endpoint: send_like
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656717e0
@llms.txt: https://napcat.apifox.cn/226656717e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: send_like API
@usage: 使用 `client.send_like()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_like"
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
class SendLikeReq(BaseHttpRequest):
    """
    send_like 请求参数
    """

    pass
# region req/

# region data
class SendLikeData(BaseModel):
    """
    send_like 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendLikeRes(BaseHttpResponse[None]):
    """
    send_like 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendLikeAPI(BaseHttpAPI[SendLikeReq, SendLikeRes]):
    """
    点赞
    """
    api: str = "/send_like"
    method: Literal["POST", "GET"] = "POST"

    Request = SendLikeReq
    Response = SendLikeRes

    request: SendLikeReq
    response: SendLikeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendLikeAPI)

# region code/

