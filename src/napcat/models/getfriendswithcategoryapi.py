# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
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
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
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

class 好友信息(BaseModel):
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
# region component_models/

# region req
class GetFriendsWithCategoryReq(BaseModel):
    """获取好友分组列表"""
    pass  # 没有请求参数

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFriendsWithCategoryRes(BaseModel):
    """获取好友分组列表"""
    class Data(BaseModel):
        """响应数据类型"""
        yes: bool = Field(default=True, description="是否可用")
        reason: str | None = Field(default=None, description="原因")

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
class GetFriendsWithCategoryAPI(BaseModel):
    """get_friends_with_category接口数据模型"""
    endpoint: str = "get_friends_with_category"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendsWithCategoryReq
    Res: type[BaseModel] = GetFriendsWithCategoryRes

# region api/
# endregion code

