# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226657058e0
@llms.txt: https://napcat.apifox.cn/226657058e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取语音消息详情

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_record"
__id__ = "226657058e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetRecordReq(BaseModel):
    """
    请求参数
    """

    file: str = Field(..., description="")
    out_format: str = Field(..., description="")
# region req/


# region res
class GetRecordRes(BaseModel):
    """
    响应参数
    """

    file: str = Field(..., description="本地路径")
    url: str = Field(..., description="网络路径")
    file_size: str = Field(..., description="文件大小")
    file_name: str = Field(..., description="文件名")
    base64: str = Field(..., description="")
# region res/

# region api
class GetRecordAPI(BaseModel):
    
    Request : type[GetRecordReq] = GetRecordReq
    Response  : type[GetRecordRes] = GetRecordRes


# region api/
# region code/

