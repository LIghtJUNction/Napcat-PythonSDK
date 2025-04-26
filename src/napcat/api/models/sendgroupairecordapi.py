# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/229486774e0
@llms.txt: https://napcat.apifox.cn/229486774e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:发送群AI语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "send_group_ai_record"
__id__ = "229486774e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SendGroupAiRecordReq(BaseModel):
    """
    {{DESC_EndPointReq}}
    """

    group_id: str | int = Field(..., description="群号")
    character: str = Field(..., description="character_id")
    text: str = Field(..., description="文本")

# endregion req



# region res
class SendGroupAiRecordRes(BaseModel):
    """
    {{DESC_EndPointRes}}
    """

    class Data(BaseModel):
        """
        响应数据
        """
        message_id: str = Field(..., description="消息id")

    status: Literal["ok"] = Field("ok", description="状态，总是ok")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="echo")

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
