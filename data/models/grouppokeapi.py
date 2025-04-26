# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659265e0
@llms.txt: https://napcat.apifox.cn/226659265e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:发送群聊戳一戳

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "group_poke"
__id__ = "226659265e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GroupPokeReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GroupPokeRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GroupPokeAPI(BaseModel):
    """group_poke接口数据模型"""
    endpoint: str = "group_poke"
    method: str = "POST"
    Req: type[BaseModel] = GroupPokeReq
    Res: type[BaseModel] = GroupPokeRes
# endregion api




# endregion code

