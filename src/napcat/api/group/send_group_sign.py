# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 230897177e0
@endpoint: send_group_sign
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/230897177e0
@llms.txt: https://napcat.apifox.cn/230897177e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: send_group_sign API
@usage: 使用 `client.send_group_sign()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_sign"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SendGroupSignReq(BaseHttpRequest):
    """
    send_group_sign 请求参数
    """

    pass
# region req/

# region data
class SendGroupSignData(BaseModel):
    """
    send_group_sign 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SendGroupSignRes(BaseHttpResponse[SendGroupSignData]):
    """
    send_group_sign 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendGroupSignAPI(BaseHttpAPI[SendGroupSignReq, SendGroupSignRes]):
    """
    群打卡
    """
    api: str = "/send_group_sign"
    method: Literal["POST", "GET"] = "POST"

    Request = SendGroupSignReq
    Response = SendGroupSignRes

    request: SendGroupSignReq
    response: SendGroupSignRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SendGroupSignAPI)

# region code/

