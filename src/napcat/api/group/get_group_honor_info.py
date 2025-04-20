"""
获取群荣誉信息 API
用于获取群内荣誉信息，如龙王、群聊之火等
接口地址: https://napcat.apifox.cn/227425479e0.md

参数：
- group_id: 群号
- type: 要获取的荣誉类型，可选值：talkative(龙王)、performer(群聊之火)、
        legend(群聊炽焰)、strong_newbie(冒尖小春笋)、
        emotion(快乐之源)，留空表示全部获取

返回：
- 群荣誉信息

# NapCat 开发中
"""

from typing import Literal
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupHonorInfoReq(BaseModel):
    """
    获取群荣誉信息 API 请求参数
    """
    group_id: int  # 群号
    type: Literal["talkative", "performer", "legend", "strong_newbie", "emotion"]  # 荣誉类型

class HonorOwnerInfo(BaseModel):
    """
    荣誉拥有者信息
    """
    user_id: int    # QQ号
    nickname: str   # 昵称
    avatar: str     # 头像URL
    description: str # 描述

class CurrentTalkative(BaseModel):
    """
    当前龙王信息
    """
    user_id: int       # QQ号
    nickname: str      # 昵称
    avatar: str        # 头像URL
    day_count: int     # 持续天数
    expire_time: int   # 过期时间戳

class GroupHonorInfo(BaseModel):
    """
    群荣誉信息
    """
    group_id: int                      # 群号
    current_talkative: CurrentTalkative  # 当前龙王信息
    talkative_list: list[HonorOwnerInfo] # 历史龙王列表
    performer_list: list[HonorOwnerInfo] # 群聊之火列表
    legend_list: list[HonorOwnerInfo]    # 群聊炽焰列表
    strong_newbie_list: list[HonorOwnerInfo] # 冒尖小春笋列表
    emotion_list: list[HonorOwnerInfo]    # 快乐之源列表

class GetGroupHonorInfoRes(BaseHttpResponse[GroupHonorInfo]):
    """
    获取群荣誉信息 API 响应参数
    """
    pass