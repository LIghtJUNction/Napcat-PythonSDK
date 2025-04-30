# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659197e0
@llms.txt: https://napcat.apifox.cn/226659197e0.md
@last_update: 2025-04-27 00:53:40

@description:

summary:获取点赞列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_profile_like"
__id__ = "226659197e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetProfileLikeReq(BaseModel):
    """
    获取点赞列表请求模型
    """
    user_id: int | str | None = Field(None, description="指定用户，不填为获取所有")
    start: float = Field(0, description="起始位置") # OpenAPI spec says number, which maps to float in Python
    count: float = Field(10, description="数量")   # OpenAPI spec says number, which maps to float in Python
# endregion req



# region res
class UserInfoItem(BaseModel):
    """
    点赞信息详情模型
    """
    uid: str = Field(..., description="用户ID")
    src: float = Field(..., description="来源") # OpenAPI spec says number
    latestTime: float = Field(..., description="最新时间") # OpenAPI spec says number
    count: float = Field(..., description="次数") # OpenAPI spec says number
    giftCount: float = Field(..., description="礼物次数") # OpenAPI spec says number
    customId: float = Field(..., description="自定义ID") # OpenAPI spec says number
    lastCharged: float = Field(..., description="最后充值时间") # OpenAPI spec says number
    bAvailableCnt: float = Field(..., description="可用次数") # OpenAPI spec says number
    bTodayVotedCnt: float = Field(..., description="今日点赞次数") # OpenAPI spec says number
    nick: str = Field(..., description="昵称")
    gender: float = Field(..., description="性别") # OpenAPI spec says number
    age: float = Field(..., description="年龄") # OpenAPI spec says number
    isFriend: bool = Field(..., description="是否好友")
    isvip: bool = Field(..., description="是否VIP")
    isSvip: bool = Field(..., description="是否超级VIP")
    uin: float = Field(..., description="UIN") # OpenAPI spec says number

class FavoriteInfo(BaseModel):
    """
    互赞信息模型
    """
    total_count: float = Field(..., description="总次数") # OpenAPI spec says number
    last_time: float = Field(..., description="最后点赞时间（不是时间戳）") # OpenAPI spec says number
    today_count: float = Field(..., description="上次次数") # OpenAPI spec says number
    userInfos: list[UserInfoItem] = Field(..., description="用户列表")

class VoteInfo(BaseModel):
    """
    点赞信息模型
    """
    total_count: float = Field(..., description="总次数") # OpenAPI spec says number
    new_count: float = Field(..., description="点赞次数") # OpenAPI spec says number
    new_nearby_count: float = Field(..., description="附近新点赞次数") # OpenAPI spec says number
    last_visit_time: float = Field(..., description="最后访问时间") # OpenAPI spec says number
    userInfos: list[UserInfoItem] = Field(..., description="用户列表")

class Data(BaseModel):
    """
    响应数据模型
    """
    uid: str = Field(..., description="用户UID")
    time: float = Field(..., description="时间") # OpenAPI spec says number
    favoriteInfo: FavoriteInfo = Field(..., description="互赞信息")
    voteInfo: VoteInfo = Field(..., description="点赞信息")

class GetProfileLikeRes(BaseModel):
    """
    获取点赞列表响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="回显")
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
