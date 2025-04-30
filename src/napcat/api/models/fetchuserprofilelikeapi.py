# -*- coding: utf-8 -*-
from __future__ import annotations

# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659254e0
@llms.txt: https://napcat.apifox.cn/226659254e0.md
@last_update: 2025-04-30 00:00:00

@description: 
功能：获取用户资料点赞状态
获取指定用户的个人资料页点赞相关信息
"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "fetch_user_profile_like"
__id__ = "226659254e0"
__method__ = "POST"
# endregion METADATA

# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
logger.debug("加载 FetchUserProfileLikeAPI 模型")

# region req
class FetchUserProfileLikeReq(BaseModel):
    """获取用户资料点赞状态请求模型"""
    user_id: int | str = Field(..., description="用户ID，可以是QQ号(number)或OpenID(string)")
# endregion req

# region res
class FetchUserProfileLikeRes(BaseModel):
    """获取用户资料点赞状态响应模型"""
    class Data(BaseModel):
        """用户资料点赞数据"""
        like_count: int = Field(0, description="点赞数量")
        is_liked: bool = Field(False, description="当前账号是否已点赞")
        last_update_time: int = Field(0, description="最后更新时间戳")
        allow_like: bool = Field(True, description="是否允许点赞")
    
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(0, description="返回码")
    data: Data = Field(..., description="点赞数据")
    message: str = Field("", description="消息")
    wording: str = Field("", description="文字说明")
    echo: str | None = Field(None, description="回显数据")
# endregion res

# region api
class FetchUserProfileLikeAPI(BaseModel):
    """fetch_user_profile_like接口数据模型"""
    endpoint: str = "fetch_user_profile_like"
    method: str = "POST"
    Req: type[BaseModel] = FetchUserProfileLikeReq
    Res: type[BaseModel] = FetchUserProfileLikeRes
# endregion api
# endregion code