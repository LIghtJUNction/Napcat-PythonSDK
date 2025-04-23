# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656970e0
@llms.txt: https://napcat.apifox.cn/226656970e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取账号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_stranger_info"
__id__ = "226656970e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetStrangerInfoReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
# region req/


# region res
class GetStrangerInfoRes(BaseModel):
    """
    响应参数
    """

    user_id: float = Field(..., description="")
    uid: str = Field(..., description="")
    uin: str = Field(..., description="")
    nickname: str = Field(..., description="昵称")
    age: float = Field(..., description="年龄")
    qid: str = Field(..., description="")
    qqLevel: float = Field(..., description="账号等级")
    sex: str = Field(..., description="性别")
    long_nick: str = Field(..., description="个性签名")
    reg_time: float = Field(..., description="注册时间")
    is_vip: bool = Field(..., description="是否会员")
    is_years_vip: bool = Field(..., description="是否年费会员")
    vip_level: float = Field(..., description="会员等级")
    remark: str = Field(..., description="备注")
    status: float = Field(..., description="")
    login_days: float = Field(..., description="连续登录天数")
# region res/

# region api
class GetStrangerInfoAPI(BaseModel):
    
    Request : type[GetStrangerInfoReq] = GetStrangerInfoReq
    Response  : type[GetStrangerInfoRes] = GetStrangerInfoRes


# region api/
# region code/

