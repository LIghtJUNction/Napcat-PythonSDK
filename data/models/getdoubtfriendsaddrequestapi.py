# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/289565516e0
@llms.txt: https://napcat.apifox.cn/289565516e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:获取被过滤好友请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_doubt_friends_add_request"
__id__ = "289565516e0"
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
# region component_models/

# region req
class GetDoubtFriendsAddRequestReq(BaseModel):
    """获取被过滤好友请求"""
    count: float

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetDoubtFriendsAddRequestRes(BaseModel):
    """获取被过滤好友请求"""
    class Data(BaseModel):
        """响应数据类型"""
        flag: str = Field(default=None, description="flag字段")
        uin: str = Field(default=None, description="uin字段")
        nick: str = Field(default=None, description="nick字段")
        source: str = Field(default=None, description="source字段")
        reason: str = Field(default=None, description="reason字段")
        msg: str = Field(default=None, description="msg字段")
        group_code: str = Field(default=None, description="group_code字段")
        time: str = Field(default=None, description="time字段")
        type: str = Field(default=None, description="type字段")

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
class GetDoubtFriendsAddRequestAPI(BaseModel):
    """get_doubt_friends_add_request接口数据模型"""
    endpoint: str = "get_doubt_friends_add_request"
    method: str = "POST"
    Req: type[BaseModel] = GetDoubtFriendsAddRequestReq
    Res: type[BaseModel] = GetDoubtFriendsAddRequestRes

# region api/
# endregion code

