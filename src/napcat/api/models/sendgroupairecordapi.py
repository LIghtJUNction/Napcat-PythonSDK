# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 
@homepage: https://napcat.apifox.cn/229486774e0
@llms.txt: https://napcat.apifox.cn/229486774e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:发送群AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_group_ai_record"
__id__ = "229486774e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal


# region req
class SendGroupAiRecordReq(BaseModel):
    """
    发送群AI语音请求模型
    """

    group_id: int | str = Field(
        ..., description="群号",
    )
    character: str = Field(
        ..., description="character_id"
    )
    text: str = Field(
        ..., description="文本"
    )
# endregion req



# region res
class SendGroupAiRecordRes(BaseModel):
    """
    发送群AI语音响应模型
    """

    status: Literal["ok"] = Field(
        "ok", description="状态码，固定为 'ok'"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: "SendGroupAiRecordRes.Data" = Field(
        ..., description="响应数据"
    )
    message: str = Field(
        ..., description="信息"
    )
    wording: str = Field(
        ..., description="提示"
    )
    echo: str | None = Field(
        ..., description="Echo信息"
    )

    class Data(BaseModel):
        """
        响应数据Data模型
        """
        message_id: str = Field(
            ..., description="消息ID"
        )
# endregion res

# region api
class SendGroupAiRecordAPI(BaseModel):
    """send_group_ai_record接口数据模型"""
    endpoint: str = "send_group_ai_record"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupAiRecordReq
    Res: type[BaseModel] = SendGroupAiRecordRes
# endregion api




# endregion code