# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659254e0
@llms.txt: https://napcat.apifox.cn/226659254e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:fetch_user_profile_like

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "fetch_user_profile_like"
__id__ = "226659254e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal # Import Literal for status
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class FetchUserProfileLikeReq(BaseModel):
    """
    请求 fetch_user_profile_like 参数
    """
    user_id: int | str = Field(..., description="用户ID，可以是QQ号(number)或OpenID(string)")
# endregion req



# region res
class FetchUserProfileLikeRes(BaseModel):
    """
    响应 fetch_user_profile_like 参数
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: dict = Field(..., description="数据载荷")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文字说明")
    echo: str | None = Field(..., description="回显数据")

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
