# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 250286903e0
@endpoint: send_packet
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/250286903e0
@llms.txt: https://napcat.apifox.cn/250286903e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:发送自定义组包

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_packet"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class SendPacketReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class SendPacketRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendPacketAPI(BaseModel):
    
    Request : type[SendPacketReq] = SendPacketReq
    Response  : type[SendPacketRes] = SendPacketRes


# region api/




# region code/

