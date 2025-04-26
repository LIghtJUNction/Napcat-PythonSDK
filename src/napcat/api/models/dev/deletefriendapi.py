# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/227237873e0
@llms.txt: https://napcat.apifox.cn/227237873e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:删除好友

"""
# __author__ = "LIghtJUNction"
# __version__ = "4.7.43"
__endpoint__ = "delete_friend"
__id__ = "227237873e0"
__method__ = "POST"

# endregion METADATA


# region code

from pydantic import BaseModel, Field
from typing import Literal # For Literal["ok"]

# region req
class DeleteFriendReq(BaseModel):
    """
    请求模型: 删除好友
    """
    user_id: int | str | None = Field(None, description="用户ID") # Based on oneOf number/string, and not explicitly required in schema
    friend_id: int | str | None = Field(None, description="好友ID") # Based on oneOf number/string, and not explicitly required in schema
    temp_block: bool = Field(..., description="拉黑") # Required based on schema
    temp_both_del: bool = Field(..., description="双向删除") # Required based on schema
# endregion req



# region res
class DeleteFriendRes(BaseModel):
    """
    响应模型: 删除好友
    """
    class Data(BaseModel):
        """
        响应数据模型
        """
        result: int = Field(..., description="结果")
        errMsg: str = Field(..., description="错误信息")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="数据体")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显信息")
# endregion res

# region api
class DeleteFriendAPI(BaseModel):
    """delete_friend接口数据模型"""
    endpoint: str = __endpoint__
    method: str = __method__
    Req: type[BaseModel] = DeleteFriendReq
    Res: type[BaseModel] = DeleteFriendRes
# endregion api




# endregion code