# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658978e0
@llms.txt: https://napcat.apifox.cn/226658978e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取好友分组列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_friends_with_category"
__id__ = "226658978e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal # Import Literal for const
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetFriendsWithCategoryReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    "

    pass
# endregion req



# region res

class FriendInfo(BaseModel):
    """好友信息"""
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
    richBuffer: dict = Field(..., description="") # Empty object in spec
    uid: str = Field(..., description="")
    uin: str = Field(..., description="")
    nick: str = Field(..., description="")
    remark: str = Field(..., description="备注")
    user_id: int = Field(..., description="")
    nickname: str = Field(..., description="")
    level: int = Field(..., description="等级")

class FriendCategory(BaseModel):
    """好友分组信息"""
    categoryId: int = Field(..., description="分组ID")
    categorySortId: int = Field(..., description="分组排序ID")
    categoryName: str = Field(..., description="分组名")
    categoryMbCount: int = Field(..., description="好友数量")
    onlineCount: int = Field(..., description="在线好友数量")
    buddyList: list[FriendInfo] = Field(..., description="好友列表")

class GetFriendsWithCategoryRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[FriendCategory] = Field(..., description="好友分组列表数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显，可能为null")

# endregion res

# region api
class GetFriendsWithCategoryAPI(BaseModel):
    """get_friends_with_category接口数据模型"""
    endpoint: str = "get_friends_with_category"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendsWithCategoryReq
    Res: type[BaseModel] = GetFriendsWithCategoryRes
# endregion api




# endregion code