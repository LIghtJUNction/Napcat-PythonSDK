# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226657036e0
@llms.txt: https://napcat.apifox.cn/226657036e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群荣誉

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_honor_info"
__id__ = "226657036e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# Define a base Result model mirroring the common response structure
# Assuming this base model is not imported from elsewhere
class Result(BaseModel):
    """通用响应结构"""
    status: str = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: any = Field(..., description="数据详情 (具体类型在继承类中定义)")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="Echo")


# Define nested models for specific data structures
class TalkativeInfo(BaseModel):
    """龙王信息"""
    user_id: int = Field(..., description="用户ID")
    avatar: str = Field(..., description="头像")
    nickname: str = Field(..., description="昵称")
    day_count: int = Field(..., description="连续天数")
    description: str = Field(..., description="说明")


class PerformerInfo(BaseModel):
    """群聊之火成员信息"""
    user_id: int = Field(..., description="用户ID")
    avatar: str = Field(..., description="头像")
    nickname: str = Field(..., description="昵称")
    description: str = Field(..., description="说明")


# region req
class GetGroupHonorInfoReq(BaseModel):
    """
    获取群荣誉请求
    """
    group_id: int | str = Field(..., description="群号")
# endregion req



# region res
class GetGroupHonorInfoData(BaseModel):
    """获取群荣誉响应数据详情"""
    group_id: int | str = Field(..., description="群号") # Using int | str based on req and common practice
    current_talkative: TalkativeInfo = Field(..., description="当前龙王")
    talkative_list: list[TalkativeInfo] = Field(..., description="历史龙王列表")
    performer_list: list[PerformerInfo] = Field(..., description="群聊之火列表")
    legend_list: list[str] = Field(..., description="群聊炽焰列表 (通常是用户ID字符串)")
    emotion_list: list[str] = Field(..., description="快乐之源列表 (通常是用户ID字符串)")
    strong_newbie_list: list[str] = Field(..., description="冒尖小春笋列表 (通常是用户ID字符串)")


class GetGroupHonorInfoRes(Result):
    """
    获取群荣誉响应
    """
    # Override the data field with the specific data model
    data: GetGroupHonorInfoData = Field(..., description="响应数据详情")
# endregion res

# region api
class GetGroupHonorInfoAPI(BaseModel):
    """get_group_honor_info接口数据模型"""
    endpoint: str = "get_group_honor_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupHonorInfoReq
    Res: type[BaseModel] = GetGroupHonorInfoRes
# endregion api




# endregion code
