# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/228534361e0
@llms.txt: https://napcat.apifox.cn/228534361e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:检查链接安全性

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "check_url_safely"
__id__ = "228534361e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class CheckUrlSafelyReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class CheckUrlSafelyRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class CheckUrlSafelyAPI(BaseModel):
    """check_url_safely接口数据模型"""
    endpoint: str = "check_url_safely"
    method: str = "POST"
    Req: type[BaseModel] = CheckUrlSafelyReq
    Res: type[BaseModel] = CheckUrlSafelyRes
# endregion api




# endregion code

