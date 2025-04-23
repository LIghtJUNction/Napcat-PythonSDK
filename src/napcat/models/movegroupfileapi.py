# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136359e0
@llms.txt: https://napcat.apifox.cn/283136359e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:移动群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "move_group_file"
__id__ = "283136359e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class MoveGroupFileReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file_id: str = Field(..., description="")
    current_parent_directory: str = Field(..., description="当前父目录")
    target_parent_directory: str = Field(..., description="目标父目录")
# region req/


# region res
class MoveGroupFileRes(BaseModel):
    """
    响应参数
    """

    ok: bool = Field(..., description="")
# region res/

# region api
class MoveGroupFileAPI(BaseModel):
    
    Request : type[MoveGroupFileReq] = MoveGroupFileReq
    Response  : type[MoveGroupFileRes] = MoveGroupFileRes


# region api/
# region code/

