# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658965e0
@llms.txt: https://napcat.apifox.cn/226658965e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取推荐好友/群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "ArkSharePeer"
__id__ = "226658965e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class ArksharepeerReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str | None = Field(None, description="和user_id二选一")
    user_id: float | str | None = Field(None, description="和group_id二选一")
    phoneNumber: str | None = Field(None, description="对方手机号")
# region req/


# region res
class ArksharepeerRes(BaseModel):
    """
    响应参数
    """

    errCode: float = Field(..., description="")
    errMsg: str = Field(..., description="")
    arkJson: str = Field(..., description="卡片json")
# region res/

# region api
class ArksharepeerAPI(BaseModel):
    
    Request : type[ArksharepeerReq] = ArksharepeerReq
    Response  : type[ArksharepeerRes] = ArksharepeerRes


# region api/
# region code/

