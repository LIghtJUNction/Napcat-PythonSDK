# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657071e0
@llms.txt: https://napcat.apifox.cn/226657071e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:检查是否可以发送图片

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "can_send_image"
__id__ = "226657071e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class CanSendImageReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class CanSendImageRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class CanSendImageAPI(BaseModel):
    """can_send_image接口数据模型"""
    endpoint: str = "can_send_image"
    method: str = "POST"
    Req: type[BaseModel] = CanSendImageReq
    Res: type[BaseModel] = CanSendImageRes
# endregion api




# endregion code

