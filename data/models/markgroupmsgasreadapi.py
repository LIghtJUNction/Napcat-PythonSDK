# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659167e0
@llms.txt: https://napcat.apifox.cn/226659167e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:设置群聊已读

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "mark_group_msg_as_read"
__id__ = "226659167e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class MarkGroupMsgAsReadReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class MarkGroupMsgAsReadRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class MarkGroupMsgAsReadAPI(BaseModel):
    """mark_group_msg_as_read接口数据模型"""
    endpoint: str = "mark_group_msg_as_read"
    method: str = "POST"
    Req: type[BaseModel] = MarkGroupMsgAsReadReq
    Res: type[BaseModel] = MarkGroupMsgAsReadRes
# endregion api




# endregion code

