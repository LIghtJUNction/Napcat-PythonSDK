# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658674e0
@endpoint: set_essence_msg
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226658674e0
@llms.txt: https://napcat.apifox.cn/226658674e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: set_essence_msg API
@usage: 使用 `client.set_essence_msg()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_essence_msg"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class SetEssenceMsgReq(BaseHttpRequest):
    """
    set_essence_msg 请求参数
    """

    pass
# region req/

# region data
class SetEssenceMsgData(BaseModel):
    """
    set_essence_msg 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SetEssenceMsgRes(BaseHttpResponse[SetEssenceMsgData]):
    """
    set_essence_msg 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetEssenceMsgAPI(BaseHttpAPI[SetEssenceMsgReq, SetEssenceMsgRes]):
    """
    设置群精华消息
    """
    api: str = "/set_essence_msg"
    method: Literal["POST", "GET"] = "POST"

    Request = SetEssenceMsgReq
    Response = SetEssenceMsgRes

    request: SetEssenceMsgReq
    response: SetEssenceMsgRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetEssenceMsgAPI)

# region code/

