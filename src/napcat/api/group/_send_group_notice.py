# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658740e0
@endpoint: _send_group_notice
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658740e0
@llms.txt: https://napcat.apifox.cn/226658740e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: _send_group_notice API
@usage: 使用 `client._send_group_notice()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_send_group_notice"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SendGroupNoticeReq(BaseHttpRequest):
    """
    _send_group_notice 请求参数
    """

    pass
# region req/

# region data
class SendGroupNoticeData(BaseModel):
    """
    _send_group_notice 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendGroupNoticeRes(BaseHttpResponse[None]):
    """
    _send_group_notice 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendGroupNoticeAPI(BaseHttpAPI[SendGroupNoticeReq, SendGroupNoticeRes]):
    """
    _发送群公告
    """
    api: str = "/_send_group_notice"
    method: Literal["POST", "GET"] = "POST"

    Request = SendGroupNoticeReq
    Response = SendGroupNoticeRes

    request: SendGroupNoticeReq
    response: SendGroupNoticeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendGroupNoticeAPI)

# region code/

