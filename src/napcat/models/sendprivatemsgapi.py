# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 244510838e0
@endpoint: send_private_msg
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/244510838e0
@llms.txt: https://napcat.apifox.cn/244510838e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 发送群消息

summary:发送私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_private_msg"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class SendPrivateMsgReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class SendPrivateMsgRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SendPrivateMsgAPI(BaseModel):
    
    Request : type[SendPrivateMsgReq] = SendPrivateMsgReq
    Response  : type[SendPrivateMsgRes] = SendPrivateMsgRes


# region api/




# region code/

