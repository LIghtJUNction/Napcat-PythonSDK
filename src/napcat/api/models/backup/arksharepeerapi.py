# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['账号相关']
@homepage: https://napcat.apifox.cn/226658965e0
@llms.txt: https://napcat.apifox.cn/226658965e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取推荐好友/群聊卡片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
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
    请求数据模型 for ArkSharePeer
    Note: group_id 和 user_id 二选一必填
    """

    group_id: int | str | None = Field(default=None, description="和user_id二选一")
    user_id: int | str | None = Field(default=None, description="和group_id二选一")
    phoneNumber: str | None = Field(default=None, description="对方手机号")

# endregion req


# region res
class ArksharepeerData(BaseModel):
    """
    响应数据模型 for ArkSharePeer data字段
    """
    errCode: int = Field(..., description="")
    errMsg: str = Field(..., description="")
    arkJson: str = Field(..., description="卡片json")

class ArksharepeerRes(BaseModel):
    """
    响应数据模型 for ArkSharePeer
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: ArksharepeerData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文字说明")
    echo: str | None = Field(default=None, description="回显数据")

# endregion res

# region api
class ArksharepeerAPI(BaseModel):
    """ArkSharePeer接口数据模型"""
    endpoint: str = "ArkSharePeer"
    method: str = "POST"
    Req: type[BaseModel] = ArksharepeerReq
    Res: type[BaseModel] = ArksharepeerRes
# endregion api


# endregion code
