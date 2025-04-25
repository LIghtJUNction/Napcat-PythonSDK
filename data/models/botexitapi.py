# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136399e0
@llms.txt: https://napcat.apifox.cn/283136399e0.md
@last_update: 2025-04-26 01:17:46

@description: 

summary:账号退出

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "bot_exit"
__id__ = "283136399e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class BotExitReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class BotExitRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class BotExitAPI(BaseModel):
    """bot_exit接口数据模型"""
    endpoint: str = "bot_exit"
    method: str = "POST"
    Req: type[BaseModel] = BotExitReq
    Res: type[BaseModel] = BotExitRes
# endregion api




# endregion code

