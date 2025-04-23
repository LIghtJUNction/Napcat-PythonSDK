# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658865e0
@llms.txt: https://napcat.apifox.cn/226658865e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群子目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_files_by_folder"
__id__ = "226658865e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupFilesByFolderReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    folder_id: str | None = Field(None, description="和 folder 二选一")
    folder: str | None = Field(None, description="和 folder_id 二选一")
    file_count: float | None = Field(50, description="一次性获取的文件数量")
# region req/


# region res
class GetGroupFilesByFolderRes(BaseModel):
    """
    响应参数
    """

    files: list[dict] = Field(..., description="文件列表")
    folders: list[dict] | None = Field(None, description="文件夹列表")
# region res/

# region api
class GetGroupFilesByFolderAPI(BaseModel):
    
    Request : type[GetGroupFilesByFolderReq] = GetGroupFilesByFolderReq
    Response  : type[GetGroupFilesByFolderRes] = GetGroupFilesByFolderRes


# region api/
# region code/

