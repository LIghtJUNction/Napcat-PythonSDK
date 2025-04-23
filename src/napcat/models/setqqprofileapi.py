# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657374e0
@llms.txt: https://napcat.apifox.cn/226657374e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:设置账号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_qq_profile"
__id__ = "226657374e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class SetQqProfileReq(BaseModel):
    """
    请求参数
    """

    nickname: str = Field(..., description="昵称")
    personal_note: str = Field(..., description="个性签名")
    sex: str = Field(..., description="性别")
# region req/


# region res
class SetQqProfileRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
# region res/

# region api
class SetQqProfileAPI(BaseModel):
    
    Request : type[SetQqProfileReq] = SetQqProfileReq
    Response  : type[SetQqProfileRes] = SetQqProfileRes


# region api/
# region code/

