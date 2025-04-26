# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226656976e0
@llms.txt: https://napcat.apifox.cn/226656976e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取好友列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
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
    获取好友列表请求参数
    """
    no_cache: bool = Field(default=False, description="不缓存")
# endregion req


# region res
class FriendInfo(BaseModel):
    """
    好友信息
    """
    birthday_year: int = Field(..., description="生日年")
    birthday_month: int = Field(..., description="日月")
    birthday_day: int = Field(..., description="生日日")
    user_id: int = Field(..., description="账号")
    age: int = Field(..., description="年龄")
    phone_num: str = Field(..., description="电话号码")
    email: str = Field(..., description="邮箱")
    category_id: int = Field(..., description="分组ID")
    nickname: str = Field(..., description="昵称")
    remark: str = Field(..., description="备注")
    sex: str = Field(..., description="性别")
    level: int = Field(..., description="等级")

class GetFriendListRes(BaseModel):
    """
    获取好友列表响应参数
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: list[FriendInfo] = Field(..., description="好友列表数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="警告信息")
    echo: str | None = Field(..., description="echo")
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
