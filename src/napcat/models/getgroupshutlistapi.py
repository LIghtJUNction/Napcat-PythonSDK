# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659300e0
@llms.txt: https://napcat.apifox.cn/226659300e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群禁言列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_shut_list"
__id__ = "226659300e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupShutListReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupShutListRes(BaseModel):
    """
    响应参数
    """

    uid: str = Field(..., description="")
    qid: str = Field(..., description="")
    uin: str = Field(..., description="")
    nick: str = Field(..., description="")
    remark: str = Field(..., description="")
    cardType: float = Field(..., description="")
    cardName: str = Field(..., description="")
    role: float = Field(..., description="")
    avatarPath: str = Field(..., description="")
    shutUpTime: float = Field(..., description="解禁时间")
    isDelete: bool = Field(..., description="")
    isSpecialConcerned: bool = Field(..., description="")
    isSpecialShield: bool = Field(..., description="")
    isRobot: bool = Field(..., description="")
    groupHonor: dict = Field(..., description="")
    memberRealLevel: float = Field(..., description="群聊等级")
    memberLevel: float = Field(..., description="")
    globalGroupLevel: float = Field(..., description="")
    globalGroupPoint: float = Field(..., description="")
    memberTitleId: float = Field(..., description="")
    memberSpecialTitle: str = Field(..., description="")
    specialTitleExpireTime: str = Field(..., description="")
    userShowFlag: float = Field(..., description="")
    userShowFlagNew: float = Field(..., description="")
    richFlag: float = Field(..., description="")
    mssVipType: float = Field(..., description="")
    bigClubLevel: float = Field(..., description="")
    bigClubFlag: float = Field(..., description="")
    autoRemark: str = Field(..., description="")
    creditLevel: float = Field(..., description="")
    joinTime: float = Field(..., description="入群时间")
    lastSpeakTime: float = Field(..., description="最后发言时间")
    memberFlag: float = Field(..., description="")
    memberFlagExt: float = Field(..., description="")
    memberMobileFlag: float = Field(..., description="")
    memberFlagExt2: float = Field(..., description="")
    isSpecialShielded: bool = Field(..., description="")
    cardNameId: float = Field(..., description="")
# region res/

# region api
class GetGroupShutListAPI(BaseModel):
    
    Request : type[GetGroupShutListReq] = GetGroupShutListReq
    Response  : type[GetGroupShutListRes] = GetGroupShutListRes


# region api/
# region code/

