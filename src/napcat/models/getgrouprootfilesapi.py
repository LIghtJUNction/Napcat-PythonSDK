# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658823e0
@llms.txt: https://napcat.apifox.cn/226658823e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群根目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_root_files"
__id__ = "226658823e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupRootFilesReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file_count: float = Field(50, description="")
# region req/


# region res
class GetGroupRootFilesRes(BaseModel):
    """
    响应参数
    """

    files: list[dict] = Field(..., description="文件列表")
    folders: list[dict] = Field(..., description="文件夹列表")
# region res/

# region api
class GetGroupRootFilesAPI(BaseModel):
    
    Request : type[GetGroupRootFilesReq] = GetGroupRootFilesReq
    Response  : type[GetGroupRootFilesRes] = GetGroupRootFilesRes


# region api/
# region code/

