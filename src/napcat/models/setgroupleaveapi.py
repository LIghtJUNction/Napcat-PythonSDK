# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656926e0
@llms.txt: https://napcat.apifox.cn/226656926e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:退群

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_leave"
__id__ = "226656926e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetGroupLeaveReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class SetGroupLeaveRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetGroupLeaveAPI(BaseModel):
    
    Request : type[SetGroupLeaveReq] = SetGroupLeaveReq
    Response  : type[SetGroupLeaveRes] = SetGroupLeaveRes


# region api/
# region code/

