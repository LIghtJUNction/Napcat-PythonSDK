# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659178e0
@llms.txt: https://napcat.apifox.cn/226659178e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:创建收藏

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "create_collection"
__id__ = "226659178e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class CreateCollectionReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class CreateCollectionRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class CreateCollectionAPI(BaseModel):
    """create_collection接口数据模型"""
    endpoint: str = "create_collection"
    method: str = "POST"
    Req: type[BaseModel] = CreateCollectionReq
    Res: type[BaseModel] = CreateCollectionRes
# endregion api




# endregion code

