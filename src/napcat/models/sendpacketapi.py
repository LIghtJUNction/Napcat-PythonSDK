# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/250286903e0
@llms.txt: https://napcat.apifox.cn/250286903e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:发送自定义组包

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_packet"
__id__ = "250286903e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SendPacketReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class SendPacketRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SendPacketAPI(BaseModel):
    
    Request : type[SendPacketReq] = SendPacketReq
    Response  : type[SendPacketRes] = SendPacketRes


# region api/
# region code/

