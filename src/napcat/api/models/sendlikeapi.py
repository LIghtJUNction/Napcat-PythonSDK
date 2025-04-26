# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226656717e0
@llms.txt: https://napcat.apifox.cn/226656717e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:点赞

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_like"
__id__ = "226656717e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field


# region req
class SendLikeReq(BaseModel):
    """
    请求参数
    """

    user_id: str | int = Field(..., description="用户ID")
    times: int = Field(..., description="点赞次数") # Assuming number means integer for times
# endregion req



# region res
class SendLikeRes(BaseModel):
    """
    响应参数
    """

    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(None, description="数据") # According to spec, data is null
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="回显数据")
# endregion res

# region api
class SendLikeAPI(BaseModel):
    """send_like接口数据模型"""
    endpoint: str = "send_like"
    method: str = "POST"
    Req: type[BaseModel] = SendLikeReq
    Res: type[BaseModel] = SendLikeRes
# endregion api




# endregion code
