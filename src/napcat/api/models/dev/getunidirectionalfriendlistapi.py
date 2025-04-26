# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/266151878e0
@llms.txt: https://napcat.apifox.cn/266151878e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取单向好友列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_unidirectional_friend_list"
__id__ = "266151878e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetUnidirectionalFriendListReq(BaseModel): # type: ignore
    """
    获取单向好友列表请求模型
    """
    # 请求体为空，不需要定义字段
    pass
# endregion req



# region res
class FriendInfo(BaseModel):
    """
    单向好友信息模型
    """
    uin: int = Field(..., description="用户ID (QQ号)")
    uid: str = Field(..., description="用户唯一标识")
    nick_name: str = Field(..., description="昵称")
    age: int = Field(..., description="年龄")
    source: str = Field(..., description="来源")

class GetUnidirectionalFriendListRes(BaseModel): # type: ignore
    """
    获取单向好友列表响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: list[FriendInfo] = Field(..., description="单向好友列表数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误描述")
    echo: str | None = Field(None, description="echo") # nullable: true

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
