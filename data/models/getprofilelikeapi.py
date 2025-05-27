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
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class user_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }

class 点赞信息(BaseModel):
    uid: str = Field(description="uid字段")
    src: float = Field(description="src字段")
    latestTime: float = Field(description="latestTime字段")
    count: float = Field(description="count字段")
    giftCount: float = Field(description="giftCount字段")
    customId: float = Field(description="customId字段")
    lastCharged: float = Field(description="lastCharged字段")
    bAvailableCnt: float = Field(description="bAvailableCnt字段")
    bTodayVotedCnt: float = Field(description="bTodayVotedCnt字段")
    nick: str = Field(description="nick字段")
    gender: float = Field(description="gender字段")
    age: float = Field(description="age字段")
    isFriend: bool = Field(description="isFriend字段")
    isvip: bool = Field(description="isvip字段")
    isSvip: bool = Field(description="isSvip字段")
    uin: float = Field(description="uin字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetProfileLikeReq(BaseModel):
    """获取点赞列表"""
    user_id: user_id | None = Field(None, description="指定用户，不填为获取所有")
    start: float | None = Field(None)
    count: float | None = Field(None)

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetProfileLikeRes(BaseModel):
    """获取点赞列表"""
    class Data(BaseModel):
        """响应数据类型"""
        uid: str = Field(default=None, description="uid字段")
        time: float = Field(default=None, description="time字段")
        favoriteInfo: Favoriteinfo = Field(default=None, description="互赞信息")
        voteInfo: Voteinfo = Field(default=None, description="点赞信息")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

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

