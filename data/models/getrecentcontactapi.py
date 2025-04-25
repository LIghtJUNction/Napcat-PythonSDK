# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659190e0
@llms.txt: https://napcat.apifox.cn/226659190e0.md
@last_update: 2025-04-26 01:17:44

@description: 获取的最新消息是每个会话最新的消息

summary:最近消息列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_recent_contact"
__id__ = "226659190e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetRecentContactReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetRecentContactRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetRecentContactAPI(BaseModel):
    """get_recent_contact接口数据模型"""
    endpoint: str = "get_recent_contact"
    method: str = "POST"
    Req: type[BaseModel] = GetRecentContactReq
    Res: type[BaseModel] = GetRecentContactRes
# endregion api




# endregion code

