# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227237873e0
@llms.txt: https://napcat.apifox.cn/227237873e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:删除好友

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_friend"
__id__ = "227237873e0"
__method__ = "POST"

# endregion METADATA


# region code

from pydantic import BaseModel, Field

# region req
class DeleteFriendReq(BaseModel):
    """
    删除好友请求参数
    """

    user_id: int | str | None = Field(None, description="用户ID")
    friend_id: int | str | None = Field(None, description="好友ID")
    temp_block: bool = Field(..., description="拉黑")
    temp_both_del: bool = Field(..., description="双向删除")

# endregion req



# region res
class DeleteFriendResData(BaseModel):
    """
    删除好友响应数据
    """
    result: int | float = Field(..., description="结果码")
    errMsg: str = Field(..., description="错误信息")


class DeleteFriendRes(BaseModel):
    """
    删除好友响应参数
    """
    status: str = Field(..., description="状态") # OpenAPI const: ok
    retcode: int | float = Field(..., description="返回码")
    data: DeleteFriendResData = Field(..., description="数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class DeleteFriendAPI(BaseModel):
    """delete_friend接口数据模型"""
    endpoint: str = "delete_friend"
    method: str = "POST"
    Req: type[BaseModel] = DeleteFriendReq
    Res: type[BaseModel] = DeleteFriendRes
# endregion api




# endregion code
