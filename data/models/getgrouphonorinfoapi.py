# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657036e0
@llms.txt: https://napcat.apifox.cn/226657036e0.md
@last_update: 2025-04-27 00:53:40

@description: |  type                   |         类型                    |
|  ----------------- | ------------------------ |
| all                       |  所有（默认）             |
| talkative              | 群聊之火                     |
| performer           | 群聊炽焰                     |
| legend                | 龙王                             |
| strong_newbie   | 冒尖小春笋（R.I.P）     |
| emotion              | 快乐源泉                      |

summary:获取群荣誉

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_honor_info"
__id__ = "226657036e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupHonorInfoReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetGroupHonorInfoRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetGroupHonorInfoAPI(BaseModel):
    """get_group_honor_info接口数据模型"""
    endpoint: str = "get_group_honor_info"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupHonorInfoReq
    Res: type[BaseModel] = GetGroupHonorInfoRes
# endregion api




# endregion code

