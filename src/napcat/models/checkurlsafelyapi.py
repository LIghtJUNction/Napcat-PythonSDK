# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 228534361e0
@endpoint: check_url_safely
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/228534361e0
@llms.txt: https://napcat.apifox.cn/228534361e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:检查链接安全性

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "check_url_safely"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class CheckUrlSafelyReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class CheckUrlSafelyRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class CheckUrlSafelyAPI(BaseModel):
    
    Request : type[CheckUrlSafelyReq] = CheckUrlSafelyReq
    Response  : type[CheckUrlSafelyRes] = CheckUrlSafelyRes


# region api/




# region code/

