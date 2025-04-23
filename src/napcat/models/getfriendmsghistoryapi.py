# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 226659174e0
@endpoint: get_friend_msg_history
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659174e0
@llms.txt: https://napcat.apifox.cn/226659174e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:获取好友历史消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friend_msg_history"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class GetFriendMsgHistoryReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class GetFriendMsgHistoryRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetFriendMsgHistoryAPI(BaseModel):
    
    Request : type[GetFriendMsgHistoryReq] = GetFriendMsgHistoryReq
    Response  : type[GetFriendMsgHistoryRes] = GetFriendMsgHistoryRes


# region api/




# region code/

