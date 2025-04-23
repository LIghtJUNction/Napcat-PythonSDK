# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658678e0
@llms.txt: https://napcat.apifox.cn/226658678e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:删除群精华消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_essence_msg"
__id__ = "226658678e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class DeleteEssenceMsgReq(BaseModel):
    """
    请求参数
    """

    message_id: float | str = Field(..., description="")
# region req/


# region res
class DeleteEssenceMsgRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class DeleteEssenceMsgAPI(BaseModel):
    
    Request : type[DeleteEssenceMsgReq] = DeleteEssenceMsgReq
    Response  : type[DeleteEssenceMsgRes] = DeleteEssenceMsgRes


# region api/
# region code/

