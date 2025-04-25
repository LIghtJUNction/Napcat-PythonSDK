# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/226657044e0
@llms.txt: https://napcat.apifox.cn/226657044e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取 CSRF Token

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_csrf_token"
__id__ = "226657044e0"
__method__ = "POST"

# endregion METADATA


# region code

from pydantic import BaseModel, Field

# region req
class GetCsrfTokenReq(BaseModel):
    """
    获取 CSRF Token 请求模型
    """

    # 根据 OpenAPI 规范，请求体为空
    pass
# endregion req



# region res
class GetCsrfTokenRes(BaseModel):
    """
    获取 CSRF Token 响应模型
    """
    status: str = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: "GetCsrfTokenRes.Data" = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="补充信息")
    echo: str | None = Field(None, description="回显信息")

    class Data(BaseModel):
        """
        CSRF Token 数据
        """
        token: int = Field(..., description="CSRF token") # Assuming int based on common usage despite 'number' in spec

# endregion res

# region api
class GetCsrfTokenAPI(BaseModel):
    """get_csrf_token接口数据模型"""
    endpoint: str = "get_csrf_token"
    method: str = "POST"
    Req: type[BaseModel] = GetCsrfTokenReq
    Res: type[BaseModel] = GetCsrfTokenRes
# endregion api




# endregion code
