# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 229486774e0
@endpoint: send_group_ai_record
@tags: 消息相关
@homepage: https://napcat.apifox.cn/229486774e0
@llms.txt: https://napcat.apifox.cn/229486774e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: send_group_ai_record API
@usage: 使用 `client.send_group_ai_record()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_ai_record"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SendGroupAiRecordReq(BaseHttpRequest):
    """
    send_group_ai_record 请求参数
    """

    pass
# region req/

# region data
class SendGroupAiRecordData(BaseModel):
    """
    send_group_ai_record 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendGroupAiRecordRes(BaseHttpResponse[SendGroupAiRecordData]):
    """
    send_group_ai_record 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendGroupAiRecordAPI(BaseHttpAPI[SendGroupAiRecordReq, SendGroupAiRecordRes]):
    """
    发送群AI语音
    """
    api: str = "/send_group_ai_record"
    method: Literal["POST", "GET"] = "POST"

    Request = SendGroupAiRecordReq
    Response = SendGroupAiRecordRes

    request: SendGroupAiRecordReq
    response: SendGroupAiRecordRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendGroupAiRecordAPI)

# region code/

