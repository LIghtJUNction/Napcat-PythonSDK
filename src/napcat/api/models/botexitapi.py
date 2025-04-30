# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['系统操作']
@homepage: https://napcat.apifox.cn/283136399e0
@llms.txt: https://napcat.apifox.cn/283136399e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:账号退出

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "bot_exit"
__id__ = "283136399e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__)

# region req
class BotExitReq(BaseModel):
    """
    请求体为空对象
    """
    pass
# endregion req



# region res
class BotExitRes(BaseModel):
    """
    响应体为空对象
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