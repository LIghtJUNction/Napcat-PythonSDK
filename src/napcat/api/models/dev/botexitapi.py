# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 系统操作
@homepage: https://napcat.apifox.cn/283136399e0
@llms.txt: https://napcat.apifox.cn/283136399e0.md
@last_update: 2025-04-26 01:17:46

@description: 账号退出

summary: 账号退出

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "bot_exit"
__id__ = "283136399e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class BotExitReq(BaseModel):
    """
    账号退出请求体
    """
    pass
# endregion req



# region res
class BotExitRes(BaseModel):
    """
    账号退出响应体
    """
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
