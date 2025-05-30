# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656976e0
@llms.txt: https://napcat.apifox.cn/226656976e0.md
@last_update: 2025-05-28 01:34:09

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
from pydantic import BaseModel, Field
from typing import Literal
import logging

logger = logging.getLogger(__name__)

# region component_models
class result(BaseModel):
    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(..., description="retcode字段")
    data: dict = Field(..., description="data字段")
    message: str = Field(..., description="message字段")
    wording: str = Field(..., description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }

class 好友信息(BaseModel):
    birthday_year: float = Field(..., description="生日年")
    birthday_month: float = Field(..., description="生日月")
    birthday_day: float = Field(..., description="生日日")
    user_id: float = Field(..., description="账号")
    age: float = Field(..., description="年龄")
    phone_num: str = Field(..., description="电话号码")
    email: str = Field(..., description="邮箱")
    category_id: float = Field(..., description="分组ID")
    nickname: str = Field(..., description="昵称")
    remark: str = Field(..., description="备注")
    sex: str = Field(..., description="性别")
    level: float = Field(..., description="等级")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetFriendListReq(BaseModel):
    """获取好友列表"""
    no_cache: bool = Field(False, description="不缓存")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetFriendListRes(BaseModel):
    """获取好友列表"""
    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(..., description="retcode字段")
    data: list[好友信息] = Field(..., description="data字段")
    message: str = Field(..., description="message字段")
    wording: str = Field(..., description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetFriendListAPI(BaseModel):
    """get_friend_list接口数据模型"""
    endpoint: str = "get_friend_list"
    method: str = "POST"
    Req: type[BaseModel] = GetFriendListReq
    Res: type[BaseModel] = GetFriendListRes

# region api/
# endregion code
