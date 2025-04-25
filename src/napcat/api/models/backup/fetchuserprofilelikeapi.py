# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659254e0
@llms.txt: https://napcat.apifox.cn/226659254e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:fetch_user_profile_like

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_user_profile_like"
__id__ = "226659254e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class FetchUserProfileLikeReq(BaseModel):
    """
    请求体模型
    """

    user_id: str | int = Field(
        ..., description="用户标识"
    )
# endregion req



# region res
class FetchUserProfileLikeRes(BaseModel):
    """
    响应体模型
    """
    class FetchUserProfileLikeResData(BaseModel):
        """
        响应数据字段
        """
        # The OpenAPI schema shows 'data' as an object with empty properties.
        pass

    status: str = Field(
        ..., description="状态, 总是 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: FetchUserProfileLikeResData = Field(
        ..., description="响应数据"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="描述"
    )
    echo: str | None = Field(
        ..., description="Echo字段"
    )
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
