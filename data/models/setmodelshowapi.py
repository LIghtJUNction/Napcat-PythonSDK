# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227233993e0
@llms.txt: https://napcat.apifox.cn/227233993e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:_设置在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_set_model_show"
__id__ = "227233993e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetModelShowReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SetModelShowRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class SetModelShowAPI(BaseModel):
    """_set_model_show接口数据模型"""
    endpoint: str = "_set_model_show"
    method: str = "POST"
    Req: type[BaseModel] = SetModelShowReq
    Res: type[BaseModel] = SetModelShowRes
# endregion api




# endregion code

