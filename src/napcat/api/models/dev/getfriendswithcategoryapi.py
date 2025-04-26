# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226658978e0
@llms.txt: https://napcat.apifox.cn/226658978e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取好友分组列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_friends_with_category"
__id__ = "226658978e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetFriendsWithCategoryReq(BaseModel):
    """
    请求参数
    """
    # API seems to have no request body properties
    pass
# endregion req



# region res

class FriendInfo(BaseModel):
    """
    好友信息
    """
    birthday_year: int = Field(..., description="生日年")
    birthday_month: int = Field(..., description="生日月")
    birthday_day: int = Field(..., description="生日日")
    user_id: int = Field(..., description="账号")
    age: int = Field(..., description="年龄")
    phone_num: str = Field(..., description="电话号码")
    email: str = Field(..., description="邮箱")
    category_id: int = Field(..., description="分组ID")
    nickname: str = Field(..., description="昵称")
    remark: str = Field(..., description="备注")
    sex: str = Field(..., description="性别") # Consider Literal if possible values are known
    level: int = Field(..., description="等级")

class FriendCategory(BaseModel):
    """
    好友分组信息
    """
    categoryId: int = Field(..., description="分组ID")
    categorySortId: int = Field(..., description="分组排序ID")
    categoryName: str = Field(..., description="分组名")
    categoryMbCount: int = Field(..., description="好友数量")
    onlineCount: int = Field(..., description="在线好友数量")
    buddyList: list[FriendInfo] = Field(..., description="好友列表")


class GetFriendsWithCategoryRes(BaseModel):
    """
    响应参数
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: list[FriendCategory] = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="Echo参数")

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
