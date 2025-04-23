# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136366e0
@llms.txt: https://napcat.apifox.cn/283136366e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:转存为永久文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "trans_group_file"
__id__ = "283136366e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class TransGroupFileReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file_id: str = Field(..., description="")
# region req/


# region res
class TransGroupFileRes(BaseModel):
    """
    响应参数
    """

    ok: bool = Field(..., description="")
# region res/

# region api
class TransGroupFileAPI(BaseModel):
    
    Request : type[TransGroupFileReq] = TransGroupFileReq
    Response  : type[TransGroupFileRes] = TransGroupFileRes


# region api/
# region code/

