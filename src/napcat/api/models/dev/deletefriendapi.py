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
from typing import Literal # For "ok" status


# region req
class DeleteFriendReq(BaseModel):
    """删除好友请求体"""
    user_id: int | str | None = Field(None, description="用户ID，可以是数字或字符串")
    friend_id: int | str | None = Field(None, description="好友ID，可以是数字或字符串")
    temp_block: bool = Field(description="拉黑")
    temp_both_del: bool = Field(description="双向删除")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class DeleteFriendRes(BaseModel):
    """删除好友响应体"""
    class Data(BaseModel):
        """响应数据类型"""
        result: float = Field(description="操作结果")
        errMsg: str = Field(description="错误信息")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="请求状态")
    retcode: float = Field(0.0, description="返回码")
    data: Data = Field(default_factory=Data, description="响应数据")
    message: str = Field("", description="消息")
    wording: str = Field("", description="提示词")
    echo: str | None = Field(None, description="回显数据")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class DeleteFriendAPI(BaseModel):
    """delete_friend接口数据模型"""
    endpoint: str = "delete_friend"
    method: str = "POST"
    Req: type[BaseModel] = DeleteFriendReq
    Res: type[BaseModel] = DeleteFriendRes

# endregion api/
# endregion code
