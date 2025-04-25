# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656952e0
@llms.txt: https://napcat.apifox.cn/226656952e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取登录号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_login_info"
__id__ = "226656952e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class GetLoginInfoReq(BaseModel):
    """
    请求模型：获取登录号信息
    "

    pass
# endregion req



# region res
class GetLoginInfoRes(BaseModel):
    """
    响应模型：获取登录号信息
    "

    class GetLoginInfoData(BaseModel):
        """
        登录号信息数据
        "
        user_id: int = Field(..., description="登录号的QQ号")
        nickname: str = Field(..., description="登录号的QQ昵称")

    status: str = Field("ok", description="状态，应为 'ok'", const=True)
    retcode: int = Field(..., description="返回码")
    data: GetLoginInfoData = Field(..., description="登录号信息")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="描述信息")
    echo: str | None = Field(..., description="echo")

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
