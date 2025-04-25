# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: ['密钥相关']
@homepage: https://napcat.apifox.cn/226657041e0
@llms.txt: https://napcat.apifox.cn/226657041e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取cookies

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_cookies"
__id__ = "226657041e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetCookiesReq(BaseModel):
    """
    请求模型
    """
    domain: str = Field(..., description="需要获取cookies的域名")
# endregion req



# region res
class GetCookiesRes(BaseModel):
    """
    响应模型
    """
    class Data(BaseModel):
        """
        响应数据详情
        """
        cookies: str = Field(..., description="cookies字符串")
        bkn: str = Field(..., description="bkn字符串")

    status: str = Field(..., description="状态码, 永远为 ok")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="补充说明")
    echo: str | None = Field(..., description="可能为空的 echo")

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
