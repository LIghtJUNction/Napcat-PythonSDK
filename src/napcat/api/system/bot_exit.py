# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 283136399e0
@endpoint: bot_exit
@tags: 系统操作
@homepage: https://napcat.apifox.cn/283136399e0
@llms.txt: https://napcat.apifox.cn/283136399e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: bot_exit API
@usage: 使用 `client.bot_exit()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "bot_exit"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class BotExitReq(BaseHttpRequest):
    """
    bot_exit 请求参数
    """

    pass
# region req/

# region data
class BotExitData(BaseModel):
    """
    bot_exit 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class BotExitRes(BaseHttpResponse[BotExitData]):
    """
    bot_exit 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class BotExitAPI(BaseHttpAPI[BotExitReq, BotExitRes]):
    """
    账号退出
    """
    api: str = "/bot_exit"
    method: Literal["POST", "GET"] = "POST"

    Request = BotExitReq
    Response = BotExitRes

    request: BotExitReq
    response: BotExitRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(BotExitAPI)

# region code/

