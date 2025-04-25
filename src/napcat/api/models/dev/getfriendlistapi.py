# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226656976e0
@llms.txt: https://napcat.apifox.cn/226656976e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取好友列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friend_list"
__id__ = "226656976e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging

from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetFriendListReq(BaseModel):
    """
    请求参数
    """

    no_cache: bool = Field(
        default=False, description="不缓存"
    )

# endregion req


# region res
class FriendInfo(BaseModel):
    """
    好友信息
    """

    qid: str = Field(..., description="QQID")
    longNick: str = Field(..., description="个性签名")
    birthday_year: int = Field(..., description="生日_年")
    birthday_month: int = Field(..., description="生日_月")
    birthday_day: int = Field(..., description="生日_日")
    age: int = Field(..., description="年龄")
    sex: str = Field(..., description="性别")
    eMail: str = Field(..., description="邮箱")
    phoneNum: str = Field(..., description="手机号")
    categoryId: int = Field(..., description="分类")
    richTime: int = Field(..., description="注册时间")
    richBuffer: dict = Field(
        ..., description=""
    )  # OpenAPI spec shows this as an empty object {}
    uid: str = Field(...)
    uin: str = Field(...)
    nick: str = Field(...)
    remark: str = Field(..., description="备注")
    user_id: int = Field(...)
    nickname: str = Field(...)
    level: int = Field(..., description="等级")


class GetFriendListRes(BaseModel):
    """
    响应参数
    """

    status: Literal[
        "ok"
    ] = Field(
        ..., description="状态"
    )  # OpenAPI spec defines this as a constant 'ok'
    retcode: int = Field(..., description="返回码")
    data: list[FriendInfo] = Field(..., description="好友列表数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(default=None, description="Echo数据")


# endregion res


# region api
class GetFriendListAPI(BaseModel):
    """get_friend_list接口数据模型"""

    endpoint: str = "get_friend_list"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendListReq
    Res: type[BaseModel] = GetFriendListRes


# endregion api

# endregion code
