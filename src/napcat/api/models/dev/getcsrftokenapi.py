# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/226657044e0
@llms.txt: https://napcat.apifox.cn/226657044e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取 CSRF Token

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_csrf_token"
__id__ = "226657044e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetCsrfTokenReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """
    pass
# endregion req



# region res
class GetCsrfTokenRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """

    class Data(BaseModel):
        """
        响应数据
        """
        token: int = Field(..., description="CSRF Token") # Assuming number is integer based on common usage

    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="echo")
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
