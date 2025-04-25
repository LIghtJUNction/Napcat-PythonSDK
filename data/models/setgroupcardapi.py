# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656913e0
@llms.txt: https://napcat.apifox.cn/226656913e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置群成员名片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_card"
__id__ = "226656913e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupCardReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SetGroupCardRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class SetGroupCardAPI(BaseModel):
    """set_group_card接口数据模型"""
    endpoint: str = "set_group_card"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupCardReq
    Res: type[BaseModel] = SetGroupCardRes
# endregion api




# endregion code

