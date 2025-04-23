# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658779e0
@llms.txt: https://napcat.apifox.cn/226658779e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:删除群文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_folder"
__id__ = "226658779e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field
from typing import Union

# region req
class DeleteGroupFolderReq(BaseModel):
    """
    请求参数
    """

    group_id: float | str = Field(..., description="")
    folder_id: str = Field(..., description="")
# region req/


# region res
class DeleteGroupFolderRes(BaseModel):
    """
    响应参数
    """

    retCode: float = Field(..., description="")
    retMsg: str = Field(..., description="")
    clientWording: str = Field(..., description="")
# region res/

# region api
class DeleteGroupFolderAPI(BaseModel):
    
    Request : type[DeleteGroupFolderReq] = DeleteGroupFolderReq
    Response  : type[DeleteGroupFolderRes] = DeleteGroupFolderRes


# region api/
# region code/

