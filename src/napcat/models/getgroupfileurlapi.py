# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658867e0
@llms.txt: https://napcat.apifox.cn/226658867e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:获取群文件链接

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_file_url"
__id__ = "226658867e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class GetGroupFileUrlReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file_id: str = Field(..., description="")
# region req/


# region res
class GetGroupFileUrlRes(BaseModel):
    """
    响应参数
    """

    url: str = Field(..., description="")
# region res/

# region api
class GetGroupFileUrlAPI(BaseModel):
    
    Request : type[GetGroupFileUrlReq] = GetGroupFileUrlReq
    Response  : type[GetGroupFileUrlRes] = GetGroupFileUrlRes


# region api/
# region code/

