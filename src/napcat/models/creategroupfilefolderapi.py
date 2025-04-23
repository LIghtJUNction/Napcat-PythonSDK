# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658773e0
@llms.txt: https://napcat.apifox.cn/226658773e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:创建群文件文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "create_group_file_folder"
__id__ = "226658773e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class CreateGroupFileFolderReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    folder_name: str = Field(..., description="")
# region req/


# region res
class CreateGroupFileFolderRes(BaseModel):
    """
    响应参数
    """

    result: dict = Field(..., description="")
    groupItem: dict = Field(..., description="")
# region res/

# region api
class CreateGroupFileFolderAPI(BaseModel):
    
    Request : type[CreateGroupFileFolderReq] = CreateGroupFileFolderReq
    Response  : type[CreateGroupFileFolderRes] = CreateGroupFileFolderRes


# region api/
# region code/

