# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/250286915e0
@llms.txt: https://napcat.apifox.cn/250286915e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:获取clientkey

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_clientkey"
__id__ = "250286915e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field


# region req
class GetClientkeyReq(BaseModel):
    """
    获取clientkey 请求模型
    "

    # Request has no parameters according to OpenAPI spec
    pass

# endregion req



# region res
class GetClientkeyRes(BaseModel):
    """
    获取clientkey 响应模型
    """

    class Data(BaseModel):
        """
        响应数据 Data 字段模型
        """
        clientkey: str = Field(..., description="客户端密钥")

    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应用语")
    echo: str | None = Field(..., description="回显数据")

# endregion res

# region api
class GetClientkeyAPI(BaseModel):
    """get_clientkey接口数据模型"""
    endpoint: str = "get_clientkey"
    method: str = "POST"
    Req: type[BaseModel] = GetClientkeyReq
    Res: type[BaseModel] = GetClientkeyRes
# endregion api




# endregion code
