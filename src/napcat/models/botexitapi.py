# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 283136399e0
@endpoint: bot_exit
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136399e0
@llms.txt: https://napcat.apifox.cn/283136399e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:账号退出

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "bot_exit"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class BotExitReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class BotExitRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class BotExitAPI(BaseModel):
    
    Request : type[BotExitReq] = BotExitReq
    Response  : type[BotExitRes] = BotExitRes


# region api/




# region code/

