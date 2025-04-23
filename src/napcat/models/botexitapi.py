# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136399e0
@llms.txt: https://napcat.apifox.cn/283136399e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:账号退出

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "bot_exit"
__id__ = "283136399e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class BotExitReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class BotExitRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class BotExitAPI(BaseModel):
    
    Request : type[BotExitReq] = BotExitReq
    Response  : type[BotExitRes] = BotExitRes


# region api/
# region code/

