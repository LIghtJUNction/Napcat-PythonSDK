# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658779e0
@llms.txt: https://napcat.apifox.cn/226658779e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:删除群文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "delete_group_folder"
__id__ = "226658779e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class group_id(BaseModel):
    id: str = Field(description="标识ID")
    name: str | None = Field(None, description="名称")

    model_config = {
        "extra": "allow",
    }

class result(BaseModel):
    status: str = Field(description="status字段")
    retcode: float = Field(description="retcode字段")
    data: dict[str, Any] = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class DeleteGroupFolderReq(BaseModel):
    """删除群文件夹"""
    group_id: group_id
    folder_id: str

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class DeleteGroupFolderRes(BaseModel):
    """删除群文件夹"""
    class Data(BaseModel):
        """响应数据类型"""
        retCode: float = Field(default=None, description="retCode字段")
        retMsg: str = Field(default=None, description="retMsg字段")
        clientWording: str = Field(default=None, description="clientWording字段")

        model_config = {
            "extra": "allow",
        }

    status: str = Field(default="ok", description="status字段")
    retcode: float = Field(default=0, description="retcode字段")
    data: Data = Field(default_factory=lambda: Data(), description="data字段")
    message: str = Field(default="", description="message字段")
    wording: str = Field(default="", description="wording字段")
    echo: str | None = Field(default=None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class DeleteGroupFolderAPI(BaseModel):
    """delete_group_folder接口数据模型"""
    endpoint: str = "delete_group_folder"
    method: str = "POST"
    Req: type[BaseModel] = DeleteGroupFolderReq
    Res: type[BaseModel] = DeleteGroupFolderRes

# region api/
# endregion code

