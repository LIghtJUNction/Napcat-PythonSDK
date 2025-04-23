# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658755e0
@llms.txt: https://napcat.apifox.cn/226658755e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:删除群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_file"
__id__ = "226658755e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class DeleteGroupFileReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file_id: str = Field(..., description="")
# region req/


# region res
class DeleteGroupFileRes(BaseModel):
    """
    响应参数
    """

    result: float = Field(..., description="")
    errMsg: str = Field(..., description="")
    transGroupFileResult: dict = Field(..., description="")
# region res/

# region api
class DeleteGroupFileAPI(BaseModel):
    
    Request : type[DeleteGroupFileReq] = DeleteGroupFileReq
    Response  : type[DeleteGroupFileRes] = DeleteGroupFileRes


# region api/
# region code/

