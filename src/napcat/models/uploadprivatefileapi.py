# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658883e0
@llms.txt: https://napcat.apifox.cn/226658883e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:上传私聊文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "upload_private_file"
__id__ = "226658883e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class UploadPrivateFileReq(BaseModel):
    """
    请求参数
    """

    user_id: float | str = Field(..., description="")
    file: str = Field(..., description="")
    name: str = Field(..., description="")
# region req/


# region res
class UploadPrivateFileRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class UploadPrivateFileAPI(BaseModel):
    
    Request : type[UploadPrivateFileReq] = UploadPrivateFileReq
    Response  : type[UploadPrivateFileRes] = UploadPrivateFileRes


# region api/
# region code/

