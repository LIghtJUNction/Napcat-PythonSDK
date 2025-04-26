# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/289565516e0
@llms.txt: https://napcat.apifox.cn/289565516e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:get_doubt_friends_add_request

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_doubt_friends_add_request"
__id__ = "289565516e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetDoubtFriendsAddRequestReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetDoubtFriendsAddRequestRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetDoubtFriendsAddRequestAPI(BaseModel):
    """get_doubt_friends_add_request接口数据模型"""
    endpoint: str = "get_doubt_friends_add_request"
    method: str = "GET"
    Req: type[BaseModel] = GetDoubtFriendsAddRequestReq
    Res: type[BaseModel] = GetDoubtFriendsAddRequestRes
# endregion api




# endregion code

