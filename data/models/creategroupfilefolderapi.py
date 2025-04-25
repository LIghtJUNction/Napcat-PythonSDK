# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658773e0
@llms.txt: https://napcat.apifox.cn/226658773e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:创建群文件文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "create_group_file_folder"
__id__ = "226658773e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Any
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class CreateGroupFileFolderReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# endregion req



# region res
class CreateGroupFileFolderRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# endregion res

# region api
class CreateGroupFileFolderAPI(BaseModel):
    """create_group_file_folder接口数据模型"""
    endpoint: str = "create_group_file_folder"
    method: str = "POST"
    Req: type[BaseModel] = CreateGroupFileFolderReq
    Res: type[BaseModel] = CreateGroupFileFolderRes
# endregion api




# endregion code

