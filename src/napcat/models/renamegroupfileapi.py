# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/283136375e0
@llms.txt: https://napcat.apifox.cn/283136375e0.md
@last_update: 2025-04-23 20:23:18

@description: 

summary:重命名群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "rename_group_file"
__id__ = "283136375e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class RenameGroupFileReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    file_id: str = Field(..., description="")
    current_parent_directory: str = Field(..., description="")
    new_name: str = Field(..., description="")
# region req/


# region res
class RenameGroupFileRes(BaseModel):
    """
    响应参数
    """

    ok: bool = Field(..., description="")
# region res/

# region api
class RenameGroupFileAPI(BaseModel):
    
    Request : type[RenameGroupFileReq] = RenameGroupFileReq
    Response  : type[RenameGroupFileRes] = RenameGroupFileRes


# region api/
# region code/

