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
from typing import Literal

# region req
class GetDoubtFriendsAddRequestReq(BaseModel):
    """获取被过滤好友请求"""
    count: float = Field(default=50, description="指定获取被过滤好友请求的数量。默认值为50。")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetDoubtFriendsAddRequestRes(BaseModel):
    """获取被过滤好友请求"""
    class Data(BaseModel):
        """响应数据类型"""
        flag: str = Field(description="flag字段")
        uin: str = Field(description="uin字段")
        nick: str = Field(description="nick字段")
        source: str = Field(description="source字段")
        reason: str = Field(description="reason字段")
        msg: str = Field(description="msg字段")
        group_code: str = Field(description="group_code字段")
        time: str = Field(description="time字段")
        type: str = Field(description="type字段")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(0.0, description="retcode字段")
    data: Data = Field(default_factory=Data, description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

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
