# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657071e0
@llms.txt: https://napcat.apifox.cn/226657071e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:检查是否可以发送图片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "can_send_image"
__id__ = "226657071e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class CanSendImageReq(BaseModel):
    """
    请求参数
    """

    pass
# region req/


# region res
class CanSendImageRes(BaseModel):
    """
    响应参数
    """

    yes: bool = Field(..., description="")
# region res/

# region api
class CanSendImageAPI(BaseModel):
    
    Request : type[CanSendImageReq] = CanSendImageReq
    Response  : type[CanSendImageRes] = CanSendImageRes


# region api/
# region code/

