# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/226657041e0
@llms.txt: https://napcat.apifox.cn/226657041e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取cookies

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_cookies"
__id__ = "226657041e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetCookiesReq(BaseModel):
    """
    get_cookies请求数据模型
    """
    domain: str = Field(..., description="需要获取cookies的域名")
# endregion req



# region res
class GetCookiesRes(BaseModel):
    """
    get_cookies响应数据模型
    """
    class Data(BaseModel):
        """
        响应数据详情
        """
        cookies: str = Field(..., description="获取到的cookies")
        bkn: str = Field(..., description="获取到的bkn")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据详情")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="措辞")
    echo: str | None = Field(None, description="Echo数据，可能为空")
# endregion res

# region api
class GetCookiesAPI(BaseModel):
    """get_cookies接口数据模型"""
    endpoint: str = "get_cookies"
    method: str = "POST"
    Req: type[BaseModel] = GetCookiesReq
    Res: type[BaseModel] = GetCookiesRes
# endregion api




# endregion code
