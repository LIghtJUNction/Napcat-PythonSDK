# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658965e0
@llms.txt: https://napcat.apifox.cn/226658965e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取推荐好友/群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "ArkSharePeer"
__id__ = "226658965e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class ArksharepeerReq(BaseModel):
    """
    获取推荐好友/群聊卡片请求模型
    "

    group_id: int | str | None = Field(None, description="和user_id二选一") # Note: One of group_id, user_id, or phoneNumber is likely required by the API logic, though not explicitly marked as required in the schema.
    user_id: int | str | None = Field(None, description="和group_id二选一") # Note: One of group_id, user_id, or phoneNumber is likely required by the API logic, though not explicitly marked as required in the schema.
    phoneNumber: str | None = Field(None, description="对方手机号") # Note: One of group_id, user_id, or phoneNumber is likely required by the API logic, though not explicitly marked as required in the schema.

# endregion req



# region res
class ArksharepeerRes(BaseModel):
    """
    获取推荐好友/群聊卡片响应模型
    "

    class Data(BaseModel):
        """
        响应数据详情
        "
        errCode: int = Field(..., description="")
        errMsg: str = Field(..., description="")
        arkJson: str = Field(..., description="卡片json")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据详情")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class ArksharepeerAPI(BaseModel):
    """ArkSharePeer接口数据模型"""
    endpoint: Literal["ArkSharePeer"] = "ArkSharePeer"
    method: Literal["POST"] = "POST"
    Req: type[BaseModel] = ArksharepeerReq
    Res: type[BaseModel] = ArksharepeerRes
# endregion api




# endregion code
