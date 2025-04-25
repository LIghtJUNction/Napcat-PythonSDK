# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659197e0
@llms.txt: https://napcat.apifox.cn/226659197e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取点赞列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_profile_like"
__id__ = "226659197e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetProfileLikeReq(BaseModel):
    """
    获取点赞列表请求模型
    "
    # API spec shows an empty request body
    pass
# endregion req



# region res
class UserInfo(BaseModel):
    """
    点赞用户信息模型
    """
    uid: str = Field(..., description="用户ID")
    src: int = Field(..., description="来源") # Assuming int based on common API patterns
    latestTime: int = Field(..., description="最新点赞时间戳")
    count: int = Field(..., description="点赞次数")
    giftCount: int = Field(..., description="礼物计数")
    customId: int = Field(..., description="自定义ID")
    lastCharged: int = Field(..., description="最后充电时间戳")
    bAvailableCnt: int = Field(..., description="可用计数")
    bTodayVotedCnt: int = Field(..., description="今日投票计数")
    nick: str = Field(..., description="昵称")
    gender: int = Field(..., description="性别")
    age: int = Field(..., description="年龄")
    isFriend: bool = Field(..., description="是否好友")
    isvip: bool = Field(..., description="是否VIP")
    isSvip: bool = Field(..., description="是否SVIP")
    uin: int = Field(..., description="UIN")

class GetProfileLikeData(BaseModel):
    """
    获取点赞列表数据模型
    """
    total_count: int = Field(..., description="总点赞数")
    new_count: int = Field(..., description="新点赞数")
    new_nearby_count: int = Field(..., description="新附近点赞数")
    last_visit_time: int = Field(..., description="最后访问时间戳")
    userInfos: list[UserInfo] = Field(..., description="点赞用户列表")

class GetProfileLikeRes(BaseModel):
    """
    获取点赞列表响应模型
    """
    status: str = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: GetProfileLikeData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述")
    echo: str | None = Field(None, description="回显信息")
# endregion res

# region api
class GetProfileLikeAPI(BaseModel):
    """get_profile_like接口数据模型"""
    endpoint: str = "get_profile_like"
    method: str = "POST"
    Req: type[BaseModel] = GetProfileLikeReq
    Res: type[BaseModel] = GetProfileLikeRes
# endregion api




# endregion code
