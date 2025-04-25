# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658740e0
@llms.txt: https://napcat.apifox.cn/226658740e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:_发送群公告

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_send_group_notice"
__id__ = "226658740e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SendGroupNoticeReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SendGroupNoticeRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class SendGroupNoticeAPI(BaseModel):
    """_send_group_notice接口数据模型"""
    endpoint: str = "_send_group_notice"
    method: str = "POST"
    Req: type[BaseModel] = SendGroupNoticeReq
    Res: type[BaseModel] = SendGroupNoticeRes
# endregion api




# endregion code

