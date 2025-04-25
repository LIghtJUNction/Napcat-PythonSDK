# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657080e0
@llms.txt: https://napcat.apifox.cn/226657080e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:检查是否可以发送语音

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "can_send_record"
__id__ = "226657080e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class CanSendRecordReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class CanSendRecordRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
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

