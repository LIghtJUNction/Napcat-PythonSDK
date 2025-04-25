# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227233993e0
@llms.txt: https://napcat.apifox.cn/227233993e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:_设置在线机型

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_set_model_show"
__id__ = "227233993e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class SetModelShowReq(BaseModel):
    """
    设置在线机型的请求参数
    """
    model: str = Field(..., description="在线机型")
    model_show: str = Field(..., description="显示的机型")
# endregion req



# region res
class SetModelShowRes(BaseModel):
    """
    设置在线机型的响应参数
    """
    status: str = Field(..., description="状态，通常为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: None = Field(..., description="数据，在此接口中为 null") # OpenAPI spec indicates data is null
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="词语")
    echo: str | None = Field(None, description="回显信息") # OpenAPI spec indicates nullable string
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
