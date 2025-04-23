# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658985e0
@llms.txt: https://napcat.apifox.cn/226658985e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取文件信息

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_file"
__id__ = "226658985e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetFileReq(BaseModel):
    """
    请求参数
    """

    file_id: str = Field(..., description="")
# region req/


# region res
class GetFileRes(BaseModel):
    """
    响应参数
    """

    file: str = Field(..., description="路径或链接")
    url: str = Field(..., description="路径或链接")
    file_size: str = Field(..., description="文件大小")
    file_name: str = Field(..., description="文件名")
    base64: str = Field(..., description="")
# region res/

# region api
class GetFileAPI(BaseModel):
    
    Request : type[GetFileReq] = GetFileReq
    Response  : type[GetFileRes] = GetFileRes


# region api/
# region code/

