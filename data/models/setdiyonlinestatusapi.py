# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151905e0
@llms.txt: https://napcat.apifox.cn/266151905e0.md
@last_update: 2025-04-26 01:17:45

@description: 

summary:设置自定义在线状态

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_diy_online_status"
__id__ = "266151905e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetDiyOnlineStatusReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SetDiyOnlineStatusRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class SetDiyOnlineStatusAPI(BaseModel):
    """set_diy_online_status接口数据模型"""
    endpoint: str = "set_diy_online_status"
    method: str = "POST"
    Req: type[BaseModel] = SetDiyOnlineStatusReq
    Res: type[BaseModel] = SetDiyOnlineStatusRes
# endregion api




# endregion code

