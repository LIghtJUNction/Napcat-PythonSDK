# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657036e0
@llms.txt: https://napcat.apifox.cn/226657036e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群荣誉

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_honor_info"
__id__ = "226657036e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupHonorInfoReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupHonorInfoRes(BaseModel):
    """
    响应参数
    """

    group_id: str = Field(..., description="")
    current_talkative: Any = Field(..., description="当前龙王")
    talkative_list: list[龙王信息] = Field(..., description="历史龙王列表")
    performer_list: list[dict] = Field(..., description="群聊之火")
    legend_list: list[str] = Field(..., description="群聊炽焰")
    emotion_list: list[str] = Field(..., description="快乐之源")
    strong_newbie_list: list[str] = Field(..., description="冒尖小春笋")
# region res/

# region api
class GetGroupHonorInfoAPI(BaseModel):
    
    Request : type[GetGroupHonorInfoReq] = GetGroupHonorInfoReq
    Response  : type[GetGroupHonorInfoRes] = GetGroupHonorInfoRes


# region api/
# region code/

