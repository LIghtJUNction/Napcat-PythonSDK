# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656652e0
@llms.txt: https://napcat.apifox.cn/226656652e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:send_msg

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_msg"
__id__ = "226656652e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class SendMsgReq(BaseModel):
    """
    请求参数
    """

    message_type: str | str = Field(..., description="")
    group_id: float | str = Field(..., description="")
    user_id: float | str = Field(..., description="")
    message: list[文本消息 | 艾特消息 | 表情消息 | 图片消息 | 回复消息 | JSON消息 | 语音消息 | 视频消息 | markdown消息] = Field(..., description="")
# region req/


# region res
class SendMsgRes(BaseModel):
    """
    响应参数
    """

    message_id: float = Field(..., description="消息ID")
# region res/

# region api
class SendMsgAPI(BaseModel):
    
    Request : type[SendMsgReq] = SendMsgReq
    Response  : type[SendMsgRes] = SendMsgRes


# region api/
# region code/

