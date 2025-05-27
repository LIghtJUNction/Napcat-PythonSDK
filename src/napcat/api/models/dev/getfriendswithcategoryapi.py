# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658978e0
@llms.txt: https://napcat.apifox.cn/226658978e0.md
@last_update: 2025-05-28 01:34:09

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
from pydantic import BaseModel, Field
from typing import Literal # Required for Literal type

# Removed unused 'logging' import

# region component_models
class 好友信息(BaseModel):
    """好友信息"""
    birthday_year: float = Field(description="生日年")
    birthday_month: float = Field(description="生日月")
    birthday_day: float = Field(description="生日日")
    user_id: float = Field(description="账号")
    age: float = Field(description="年龄")
    phone_num: str = Field(description="电话号码")
    email: str = Field(description="邮箱")
    category_id: float = Field(description="分组ID")
    nickname: str = Field(description="昵称")
    remark: str = Field(description="备注")
    sex: str = Field(description="性别")
    level: float = Field(description="等级")

    model_config = {
        "extra": "allow",
    }
# endregion component_models


# region req
class GetFriendsWithCategoryReq(BaseModel):
    """获取好友分组列表的请求模型"""
    # No request parameters as per OpenAPI spec
    pass

    model_config = {
        "extra": "allow",
    }
# endregion req


# region res
class GetFriendsWithCategoryRes(BaseModel):
    """获取好友分组列表的响应模型"""

    class FriendCategory(BaseModel):
        """好友分组信息"""
        category_id: float = Field(alias="categoryId", description="分组ID")
        category_sort_id: float = Field(alias="categorySortId", description="分组排序ID")
        category_name: str = Field(alias="categoryName", description="分组名")
        category_mb_count: float = Field(alias="categoryMbCount", description="好友数量")
        online_count: float = Field(alias="onlineCount", description="在线好友数量")
        buddy_list: list[好友信息] = Field(alias="buddyList", description="好友列表")

        model_config = {
            "extra": "allow",
            "populate_by_name": True # Allow instantiation by field name or alias
        }

    status: Literal["ok"] = Field(default="ok", description="状态字段")
    retcode: float = Field(default=0.0, description="返回码字段")
    data: list[FriendCategory] = Field(default_factory=list, description="响应数据字段")
    message: str = Field(default="", description="消息字段")
    wording: str = Field(default="", description="提示语字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
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
