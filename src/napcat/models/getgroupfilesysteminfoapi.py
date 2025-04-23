# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658789e0
@llms.txt: https://napcat.apifox.cn/226658789e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群文件系统信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_file_system_info"
__id__ = "226658789e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupFileSystemInfoReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
# region req/


# region res
class GetGroupFileSystemInfoRes(BaseModel):
    """
    响应参数
    """

    file_count: float = Field(..., description="文件总数")
    limit_count: float = Field(..., description="文件上限")
    used_space: float = Field(..., description="已使用空间")
    total_space: float = Field(..., description="空间上限")
# region res/

# region api
class GetGroupFileSystemInfoAPI(BaseModel):
    
    Request : type[GetGroupFileSystemInfoReq] = GetGroupFileSystemInfoReq
    Response  : type[GetGroupFileSystemInfoRes] = GetGroupFileSystemInfoRes


# region api/
# region code/

