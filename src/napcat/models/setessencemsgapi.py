# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658674e0
@llms.txt: https://napcat.apifox.cn/226658674e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_essence_msg"
__id__ = "226658674e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SetEssenceMsgReq(BaseModel):
    """
    请求参数
    """

    message_id: float | str = Field(..., description="")
# region req/


# region res
class SetEssenceMsgRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class SetEssenceMsgAPI(BaseModel):
    
    Request : type[SetEssenceMsgReq] = SetEssenceMsgReq
    Response  : type[SetEssenceMsgRes] = SetEssenceMsgRes


# region api/
# region code/

