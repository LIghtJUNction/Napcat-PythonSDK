# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/289565525e0
@llms.txt: https://napcat.apifox.cn/289565525e0.md
@last_update: 2025-05-28 01:34:11

@description:  在 4.7.43 版本中 
approve 的值无效
调用该接口既是同意好友请求！！！
调用该接口既是同意好友请求！！！
调用该接口既是同意好友请求！！！

summary:处理被过滤好友请求

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_doubt_friends_add_request"
__id__ = "289565525e0"
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
class SetDoubtFriendsAddRequestReq(BaseModel):
    """处理被过滤好友请求"""
    flag: str
    approve: bool = Field(description="4.7.43 版本中该值无效")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class SetDoubtFriendsAddRequestRes(BaseModel):
    """处理被过滤好友请求"""
    class Data(BaseModel):
        """响应数据类型"""

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
class SetDoubtFriendsAddRequestAPI(BaseModel):
    """set_doubt_friends_add_request接口数据模型"""
    endpoint: str = "set_doubt_friends_add_request"
    method: str = "POST"
    Req: type[BaseModel] = SetDoubtFriendsAddRequestReq
    Res: type[BaseModel] = SetDoubtFriendsAddRequestRes

# region api/
# endregion code

