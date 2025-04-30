# -*- coding: utf-8 -*-# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656952e0
@llms.txt: https://napcat.apifox.cn/226656952e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取登录号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_login_info"
__id__ = "226656952e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class GetLoginInfoReq(BaseModel):
    """
    获取登录号信息请求模型
    """
    pass
# endregion req



# region res
class GetLoginInfoRes(BaseModel):
    """
    获取登录号信息响应模型
    """

    class Data(BaseModel):
        """
        响应数据
        """
        user_id: int = Field(..., description="机器人账号")
        nickname: str = Field(..., description="机器人昵称")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="Echo数据")
# endregion res

# region api
class GetLoginInfoAPI(BaseModel):
    """get_login_info接口数据模型"""
    endpoint: str = "get_login_info"
    method: str = "POST"
    Req: type[BaseModel] = GetLoginInfoReq
    Res: type[BaseModel] = GetLoginInfoRes
# endregion api




# endregion code
