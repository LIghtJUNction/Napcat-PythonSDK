# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151849e0
@llms.txt: https://napcat.apifox.cn/266151849e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:获取私聊文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_private_file_url"
__id__ = "266151849e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class GetPrivateFileUrlReq(BaseModel):
    """
    请求参数
    """

    file_id: str = Field(..., description="")
# region req/


# region res
class GetPrivateFileUrlRes(BaseModel):
    """
    响应参数
    """

    url: str = Field(..., description="")
# region res/

# region api
class GetPrivateFileUrlAPI(BaseModel):
    
    Request : type[GetPrivateFileUrlReq] = GetPrivateFileUrlReq
    Response  : type[GetPrivateFileUrlRes] = GetPrivateFileUrlRes


# region api/
# region code/

