# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226657374e0
@llms.txt: https://napcat.apifox.cn/226657374e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:设置账号信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "set_qq_profile"
__id__ = "226657374e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal


# region req
class SetQqProfileReq(BaseModel):
    """
    设置账号信息请求模型
    """

    nickname: str = Field(..., description="昵称")
    personal_note: str | None = Field(None, description="个性签名")
    sex: str | None = Field(None, description="性别")
# endregion req



# region res
class SetQqProfileRes(BaseModel):
    """
    设置账号信息响应模型
    """

    class SetQqProfileResData(BaseModel):
        """
        设置账号信息响应数据详情
        """
        result: int | float = Field(..., description="结果码") # OpenAPI says number, can be int or float
        errMsg: str = Field(..., description="错误信息")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: SetQqProfileResData = Field(..., description="响应数据详情")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class SetQqProfileAPI(BaseModel):
    """set_qq_profile接口数据模型"""
    endpoint: str = "set_qq_profile"
    method: str = "POST"
    Req: type[BaseModel] = SetQqProfileReq
    Res: type[BaseModel] = SetQqProfileRes
# endregion api




# endregion code