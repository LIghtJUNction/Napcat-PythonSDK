# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226657389e0
@endpoint: mark_msg_as_read
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657389e0
@llms.txt: https://napcat.apifox.cn/226657389e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: mark_msg_as_read API
@usage: 使用 `client.mark_msg_as_read()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_msg_as_read"
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
class MarkMsgAsReadReq(BaseHttpRequest):
    """
    mark_msg_as_read 请求参数
    """

    pass
# region req/

# region data
class MarkMsgAsReadData(BaseModel):
    """
    mark_msg_as_read 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class MarkMsgAsReadRes(BaseHttpResponse[None]):
    """
    mark_msg_as_read 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class MarkMsgAsReadAPI(BaseHttpAPI[MarkMsgAsReadReq, MarkMsgAsReadRes]):
    """
    设置消息已读
    """
    api: str = "/mark_msg_as_read"
    method: Literal["POST", "GET"] = "POST"

    Request = MarkMsgAsReadReq
    Response = MarkMsgAsReadRes

    request: MarkMsgAsReadReq
    response: MarkMsgAsReadRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(MarkMsgAsReadAPI)

# region code/

