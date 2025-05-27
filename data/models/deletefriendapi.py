# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/227237873e0
@llms.txt: https://napcat.apifox.cn/227237873e0.md
@last_update: 2025-05-28 01:34:11

@description: 

summary:删除好友

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "delete_friend"
__id__ = "227237873e0"
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
# region component_models/

# region req
class DeleteFriendReq(BaseModel):
    """删除好友"""
    user_id: user_id | None = Field(None)
    friend_id: user_id | None = Field(None)
    temp_block: bool = Field(description="拉黑")
    temp_both_del: bool = Field(description="双向删除")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class DeleteFriendRes(BaseModel):
    """删除好友"""
    class Data(BaseModel):
        """响应数据类型"""
        result: float = Field(default=None, description="result字段")
        errMsg: str = Field(default=None, description="errMsg字段")

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
class DeleteFriendAPI(BaseModel):
    """delete_friend接口数据模型"""
    endpoint: str = "delete_friend"
    method: str = "POST"
    Req: type[BaseModel] = DeleteFriendReq
    Res: type[BaseModel] = DeleteFriendRes

# region api/
# endregion code

