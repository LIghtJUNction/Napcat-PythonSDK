# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658664e0
@llms.txt: https://napcat.apifox.cn/226658664e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_essence_msg_list"
__id__ = "226658664e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetEssenceMsgListReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetEssenceMsgListRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class GetEssenceMsgListAPI(BaseModel):
    
    Request : type[GetEssenceMsgListReq] = GetEssenceMsgListReq
    Response  : type[GetEssenceMsgListRes] = GetEssenceMsgListRes


# region api/
# region code/

