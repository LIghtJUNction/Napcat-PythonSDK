# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227738594e0
@llms.txt: https://napcat.apifox.cn/227738594e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取小程序卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_mini_app_ark"
__id__ = "227738594e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetMiniAppArkReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetMiniAppArkRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetMiniAppArkAPI(BaseModel):
    """get_mini_app_ark接口数据模型"""
    endpoint: str = "get_mini_app_ark"
    method: str = "POST"
    Req: type[BaseModel] = GetMiniAppArkReq
    Res: type[BaseModel] = GetMiniAppArkRes
# endregion api




# endregion code

