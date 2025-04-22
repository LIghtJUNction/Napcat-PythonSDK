# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658977e0
@endpoint: set_online_status
@tags:
@homepage: https://napcat.apifox.cn/226658977e0
@llms.txt: https://napcat.apifox.cn/226658977e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description:

### 在线 # 描述  特殊元数据 AI可修改
@usage: 使用 `client.set_online_status()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_online_status"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SetOnlineStatusReq(BaseHttpRequest):
    """
    set_online_status 请求参数
    """

    pass
# region req/

# region data
class SetOnlineStatusData(BaseModel):
    """
    set_online_status 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SetOnlineStatusRes(BaseHttpResponse[SetOnlineStatusData]):
    """
    set_online_status 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetOnlineStatusAPI(BaseHttpAPI[SetOnlineStatusReq, SetOnlineStatusRes]):
    """
    设置在线状态
    """
    api: str = "/set_online_status"
    method: Literal["POST", "GET"] = "POST"

    Request = SetOnlineStatusReq
    Response = SetOnlineStatusRes

    request: SetOnlineStatusReq
    response: SetOnlineStatusRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetOnlineStatusAPI)

# region code/

