# -*- coding: utf-8 -*-
# region METADATA
"""
@author: LIghtJUNction

@api_id: 266151849e0
@endpoint: get_private_file_url
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/266151849e0
@llms.txt: https://napcat.apifox.cn/266151849e0.md
@version: 4.7.17
@last_update: 2025-04-23 20:09:55

@description: 

summary:获取私聊文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_private_file_url"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any , Literal

from pydantic import BaseModel, Field

# region req
class GetPrivateFileUrlReq(BaseModel): # type: ignore
    """
    {{DESC_EndPointReq}}
    """

    pass
# region req/



# region res
class GetPrivateFileUrlRes(BaseModel): # type: ignore
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetPrivateFileUrlAPI(BaseModel):
    
    Request : type[GetPrivateFileUrlReq] = GetPrivateFileUrlReq
    Response  : type[GetPrivateFileUrlRes] = GetPrivateFileUrlRes


# region api/




# region code/

