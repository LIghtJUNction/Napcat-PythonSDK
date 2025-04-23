# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/230897177e0
@llms.txt: https://napcat.apifox.cn/230897177e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:群打卡

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_sign"
__id__ = "230897177e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SendGroupSignReq(BaseModel):
    """
    请求参数
    """

    group_id: str = Field(..., description="")
# region req/


# region res
class SendGroupSignRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SendGroupSignAPI(BaseModel):
    
    Request : type[SendGroupSignReq] = SendGroupSignReq
    Response  : type[SendGroupSignRes] = SendGroupSignRes


# region api/
# region code/

