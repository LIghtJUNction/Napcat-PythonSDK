# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658753e0
@llms.txt: https://napcat.apifox.cn/226658753e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:上传群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "upload_group_file"
__id__ = "226658753e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class UploadGroupFileReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file: str = Field(..., description="")
    name: str = Field(..., description="")
    folder_id: str = Field(..., description="文件夹ID")
# region req/


# region res
class UploadGroupFileRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class UploadGroupFileAPI(BaseModel):
    
    Request : type[UploadGroupFileReq] = UploadGroupFileReq
    Response  : type[UploadGroupFileRes] = UploadGroupFileRes


# region api/
# region code/

