# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226657054e0
@llms.txt: https://napcat.apifox.cn/226657054e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取 QQ 相关接口凭证

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_credentials"
__id__ = "226657054e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetCredentialsReq(BaseModel):
    """
    获取 QQ 相关接口凭证请求模型
    """

    domain: str = Field(..., description="需要获取凭证的域名")

# endregion req



# region res
class GetCredentialsRes(BaseModel):
    """
    获取 QQ 相关接口凭证响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        cookies: str = Field(..., description="QQ 接口 cookies")
        token: float = Field(..., description="QQ 接口 token") # Using float for number as per OpenAPI spec

    status: str = Field("ok", description="响应状态", pattern="^ok$")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="回显字段")

# endregion res

# region api
class GetCredentialsAPI(BaseModel):
    """get_credentials接口数据模型"""
    endpoint: str = "get_credentials"
    method: str = "POST"
    Req: type[BaseModel] = GetCredentialsReq
    Res: type[BaseModel] = GetCredentialsRes
# endregion api




# endregion code
