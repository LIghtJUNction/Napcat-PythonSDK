# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659197e0
@llms.txt: https://napcat.apifox.cn/226659197e0.md
@last_update: 2025-05-28 01:34:10

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
from pydantic import BaseModel, Field
import logging
from typing import Literal, Any # 导入 Literal 和 Any

logger = logging.getLogger(__name__)

# region component_models

class Result(BaseModel):
    """通用响应结果模型"""
    status: Literal["ok"] = Field("ok", description="请求状态")
    retcode: float = Field(0, description="返回码")
    # data type will be overridden by specific response models
    data: dict[str, Any] = Field(default_factory=dict, description="响应数据") # 通用数据字段，实际类型会在子类中覆盖
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示词")
    echo: str | None = Field(None, description="回声数据")

    model_config = {
        "extra": "allow",
    }

class VoteUserInfo(BaseModel):
    """点赞用户详细信息"""
    uid: str = Field(..., description="用户ID")
    src: float = Field(..., description="来源")
    latestTime: float = Field(..., description="最新时间")
    count: float = Field(..., description="次数")
    giftCount: float = Field(..., description="礼物次数")
    customId: float = Field(..., description="自定义ID")
    lastCharged: float = Field(..., description="最后充值时间")
    bAvailableCnt: float = Field(..., description="可用次数")
    bTodayVotedCnt: float = Field(..., description="今日投票次数")
    nick: str = Field(..., description="昵称")
    gender: float = Field(..., description="性别")
    age: float = Field(..., description="年龄")
    isFriend: bool = Field(..., description="是否好友")
    isvip: bool = Field(..., description="是否VIP")
    isSvip: bool = Field(..., description="是否SVIP")
    uin: float = Field(..., description="UIN")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetProfileLikeReq(BaseModel):
    """获取点赞列表请求模型"""
    user_id: str | int | None = Field(None, description="指定用户，不填为获取所有")
    start: float = Field(0, description="起始位置")
    count: float = Field(10, description="数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetProfileLikeRes(Result): # 继承自 Result
    """获取点赞列表响应模型"""
    class Data(BaseModel):
        """响应数据类型"""
        class FavoriteInfo(BaseModel):
            """互赞信息"""
            total_count: float = Field(..., description="总次数")
            last_time: float = Field(..., description="最后点赞时间（不是时间戳）")
            today_count: float = Field(..., description="上次次数")
            userInfos: list[VoteUserInfo] = Field(..., description="互赞用户列表")

            model_config = {
                "extra": "allow",
            }

        class VoteInfo(BaseModel):
            """点赞信息"""
            total_count: float = Field(..., description="总次数")
            new_count: float = Field(..., description="点赞次数")
            new_nearby_count: float = Field(..., description="附近新点赞次数")
            last_visit_time: float = Field(..., description="最后访问时间")
            userInfos: list[VoteUserInfo] = Field(..., description="点赞用户列表")

            model_config = {
                "extra": "allow",
            }

        uid: str = Field(..., description="用户ID")
        time: float = Field(..., description="时间")
        favoriteInfo: FavoriteInfo = Field(..., description="互赞信息")
        voteInfo: VoteInfo = Field(..., description="点赞信息")

        model_config = {
            "extra": "allow",
        }

    data: Data = Field(default_factory=Data, description="响应数据") # 覆盖父类的 data 字段

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetProfileLikeAPI(BaseModel):
    """get_profile_like接口数据模型"""
    endpoint: str = "get_profile_like"
    method: str = "POST"
    Req: type[BaseModel] = GetProfileLikeReq
    Res: type[BaseModel] = GetProfileLikeRes

# region api/
# endregion code
