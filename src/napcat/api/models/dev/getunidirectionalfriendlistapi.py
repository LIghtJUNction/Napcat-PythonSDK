# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/266151878e0
@llms.txt: https://napcat.apifox.cn/266151878e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:获取单向好友列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_unidirectional_friend_list"
__id__ = "266151878e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class GetUnidirectionalFriendListReq(BaseModel):
    """
    获取单向好友列表的请求模型
    """
    pass
# endregion req



# region res
class UnidirectionalFriend(BaseModel):
    """
    单向好友信息模型
    """
    uin: int = Field(..., description="好友的uin (QQ号)")
    uid: str = Field(..., description="好友的uid (内部唯一标识)")
    nick_name: str = Field(..., description="好友的昵称")
    age: int = Field(..., description="好友的年龄")
    source: str = Field(..., description="获取好友信息的来源")

class GetUnidirectionalFriendListRes(BaseModel):
    """
    获取单向好友列表的响应模型
    """
    status: str = Field(
        ..., description="响应状态，固定为 'ok'", const="ok"
    )
    retcode: int = Field(..., description="返回码")
    data: list[UnidirectionalFriend] = Field(..., description="单向好友列表")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="说明")
    echo: str | None = Field(None, description="echo回显")
# endregion res

# region api
class GetUnidirectionalFriendListAPI(BaseModel):
    """get_unidirectional_friend_list接口数据模型"""
    endpoint: str = "get_unidirectional_friend_list"
    method: str = "POST"
    Req: type[BaseModel] = GetUnidirectionalFriendListReq
    Res: type[BaseModel] = GetUnidirectionalFriendListRes
# endregion api




# endregion code
