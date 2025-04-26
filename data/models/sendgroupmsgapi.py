# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/244510830e0
@llms.txt: https://napcat.apifox.cn/244510830e0.md
@last_update: 2025-04-27 00:53:41

@description: 发送群消息

summary:发送群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "send_group_msg"
__id__ = "244510830e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SendGroupMsgReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SendGroupMsgRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class SendGroupMsgAPI(BaseModel):
    """send_group_msg接口数据模型"""
    endpoint: str = "send_group_msg"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupMsgReq
    Res: type[BaseModel] = SendGroupMsgRes
# endregion api




# endregion code

