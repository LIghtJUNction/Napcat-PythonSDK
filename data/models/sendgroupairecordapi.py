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
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SendGroupAiRecordReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SendGroupAiRecordRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
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

