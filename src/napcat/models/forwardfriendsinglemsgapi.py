# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226659051e0
@endpoint: forward_friend_single_msg
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659051e0
@llms.txt: https://napcat.apifox.cn/226659051e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:消息转发到私聊

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "forward_friend_single_msg"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class ForwardFriendSingleMsgReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class ForwardFriendSingleMsgRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class ForwardFriendSingleMsgAPI(BaseModel):
    
    Request : type[ForwardFriendSingleMsgReq] = ForwardFriendSingleMsgReq
    Response  : type[ForwardFriendSingleMsgRes] = ForwardFriendSingleMsgRes


# region api/




# region code/

