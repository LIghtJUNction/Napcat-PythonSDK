# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['密钥相关']
@homepage: https://napcat.apifox.cn/226657054e0
@llms.txt: https://napcat.apifox.cn/226657054e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取 QQ 相关接口凭证

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_credentials"
__id__ = "226657054e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Import Literal for fixed values

logger = logging.getLogger(__name__)

# region req
class GetCredentialsReq(BaseModel):
    """
    获取 QQ 相关接口凭证 请求模型
    """
    domain: str = Field(..., description="域名")
# endregion req



# region res
class GetCredentialsRes(BaseModel):
    """
    获取 QQ 相关接口凭证 响应模型
    """

    class Data(BaseModel):
        """
        响应数据详情
        """
        cookies: str = Field(..., description="Cookies")
        token: float = Field(..., description="Token")

    status: Literal["ok"] = Field(..., description="状态")
    retcode: float = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(..., description="回显") # nullable: true

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
