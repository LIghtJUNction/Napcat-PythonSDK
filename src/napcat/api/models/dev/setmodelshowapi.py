# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227233993e0
@llms.txt: https://napcat.apifox.cn/227233993e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:_设置在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "_set_model_show"
__id__ = "227233993e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class SetModelShowReq(BaseModel):
    """
    _设置在线机型的请求模型
    根据OpenAPI文档，请求体为空。
    """
    pass
# endregion req



# region res
class SetModelShowRes(BaseModel):
    """
    _设置在线机型的响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="响应数据体")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="额外消息或提示")
    echo: str | None = Field(..., description="echo") # Spec says required but nullable
# endregion res

# region api
class SetModelShowAPI(BaseModel):
    """_set_model_show接口数据模型"""
    endpoint: str = "_set_model_show"
    method: str = "POST"
    Req: type[BaseModel] = SetModelShowReq
    Res: type[BaseModel] = SetModelShowRes
# endregion api




# endregion code
