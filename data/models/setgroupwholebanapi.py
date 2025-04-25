# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226656802e0
@llms.txt: https://napcat.apifox.cn/226656802e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:全体禁言

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_group_whole_ban"
__id__ = "226656802e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class SetGroupWholeBanReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class SetGroupWholeBanRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class SetGroupWholeBanAPI(BaseModel):
    """set_group_whole_ban接口数据模型"""
    endpoint: str = "set_group_whole_ban"
    method: str = "POST"
    Req: type[BaseModel] = SetGroupWholeBanReq
    Res: type[BaseModel] = SetGroupWholeBanRes
# endregion api




# endregion code

