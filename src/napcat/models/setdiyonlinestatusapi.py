# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 266151905e0
@endpoint: set_diy_online_status
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151905e0
@llms.txt: https://napcat.apifox.cn/266151905e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:设置自定义在线状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_diy_online_status"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class SetDiyOnlineStatusReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class SetDiyOnlineStatusRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetDiyOnlineStatusAPI(BaseModel):
    
    Request : type[SetDiyOnlineStatusReq] = SetDiyOnlineStatusReq
    Response  : type[SetDiyOnlineStatusRes] = SetDiyOnlineStatusRes


# region api/




# region code/

