# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658660e0
@llms.txt: https://napcat.apifox.cn/226658660e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群系统消息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_system_msg"
__id__ = "226658660e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupSystemMsgReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetGroupSystemMsgRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetGroupSystemMsgAPI(BaseModel):
    """get_group_system_msg接口数据模型"""
    endpoint: str = "get_group_system_msg"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupSystemMsgReq
    Res: type[BaseModel] = GetGroupSystemMsgRes
# endregion api




# endregion code

