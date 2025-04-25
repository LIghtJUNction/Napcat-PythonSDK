# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657389e0
@llms.txt: https://napcat.apifox.cn/226657389e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置消息已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_msg_as_read"
__id__ = "226657389e0"
__method__ = "POST"

# endregion METADATA


# region code

from pydantic import BaseModel, Field, model_validator

# region req
class MarkMsgAsReadReq(BaseModel):
    """
    设置消息已读请求模型
    """

    group_id: str | int | None = Field(None, description="与user_id二选一")
    user_id: str | int | None = Field(None, description="与group_id二选一")

    @model_validator(mode='after')
    def check_either_or(self) -> 'MarkMsgAsReadReq':
        if self.group_id is None and self.user_id is None:
            raise ValueError("group_id and user_id cannot both be None")
        if self.group_id is not None and self.user_id is not None:
             # API spec implies either-or, not both. Adjust logic if both is allowed.
             pass # Allowing both for now based on common API practices unless specified otherwise.
        return self

# endregion req



# region res
class MarkMsgAsReadRes(BaseModel):
    """
    设置消息已读响应模型
    """

    status: str = Field(..., description="状态", pattern="^ok$")
    retcode: int | float = Field(..., description="返回码")
    data: None = Field(..., description="数据") # Explicitly null as per OpenAPI override
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class MarkMsgAsReadAPI(BaseModel):
    """mark_msg_as_read接口数据模型"""
    endpoint: str = "mark_msg_as_read"
    method: str = "POST"
    Req: type[BaseModel] = MarkMsgAsReadReq
    Res: type[BaseModel] = MarkMsgAsReadRes
# endregion api




# endregion code
