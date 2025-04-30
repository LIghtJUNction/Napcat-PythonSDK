# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226657080e0
@llms.txt: https://napcat.apifox.cn/226657080e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:检查是否可以发送语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "can_send_record"
__id__ = "226657080e0"
__method__ = "POST"

# endregion METADATA


# region code

from pydantic import BaseModel, Field
from typing import Literal

# region req
class CanSendRecordReq(BaseModel):
    """
    检查是否可以发送语音 请求模型
    """
    # 请求体为空，无需定义字段
    pass
# endregion req



# region res
class CanSendRecordRes(BaseModel):
    """
    检查是否可以发送语音 响应模型
    """
    # 定义嵌套的data模型
    class Data(BaseModel):
        yes: bool = Field(..., description="是否可以发送语音")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'") # 确定的值使用Literal
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应词")
    echo: str | None = Field(None, description="Echo字段")

# endregion res

# region api
class CanSendRecordAPI(BaseModel):
    """can_send_record接口数据模型"""
    endpoint: str = "can_send_record"
    method: str = "POST"
    Req: type[BaseModel] = CanSendRecordReq
    Res: type[BaseModel] = CanSendRecordRes
# endregion api




# endregion code
