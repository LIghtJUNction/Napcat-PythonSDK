# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658823e0
@llms.txt: https://napcat.apifox.cn/226658823e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群根目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_root_files"
__id__ = "226658823e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupRootFilesReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetGroupRootFilesRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetGroupRootFilesAPI(BaseModel):
    """get_group_root_files接口数据模型"""
    endpoint: str = "get_group_root_files"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupRootFilesReq
    Res: type[BaseModel] = GetGroupRootFilesRes
# endregion api




# endregion code

