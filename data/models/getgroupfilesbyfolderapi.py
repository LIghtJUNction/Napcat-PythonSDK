# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658865e0
@llms.txt: https://napcat.apifox.cn/226658865e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取群子目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_files_by_folder"
__id__ = "226658865e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetGroupFilesByFolderReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class GetGroupFilesByFolderRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class GetGroupFilesByFolderAPI(BaseModel):
    """get_group_files_by_folder接口数据模型"""
    endpoint: str = "get_group_files_by_folder"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupFilesByFolderReq
    Res: type[BaseModel] = GetGroupFilesByFolderRes
# endregion api




# endregion code

