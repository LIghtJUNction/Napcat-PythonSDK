# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658823e0
@llms.txt: https://napcat.apifox.cn/226658823e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群根目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_root_files"
__id__ = "226658823e0"
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

class 群文件夹信息(BaseModel):
    group_id: float = Field(description="group_id字段")
    folder_id: str = Field(description="folder_id字段")
    folder: str = Field(description="folder字段")
    folder_name: str = Field(description="文件夹名称")
    create_time: float = Field(description="创建时间")
    creator: float = Field(description="创建人账号")
    creator_name: str = Field(description="创建人昵称")
    total_file_count: float = Field(description="文件数量")

    model_config = {
        "extra": "allow",
    }

class 群文件信息(BaseModel):
    group_id: float = Field(description="group_id字段")
    file_id: str = Field(description="file_id字段")
    file_name: str = Field(description="file_name字段")
    busid: float = Field(description="busid字段")
    size: float = Field(description="size字段")
    file_size: float = Field(description="file_size字段")
    upload_time: float = Field(description="upload_time字段")
    dead_time: float = Field(description="dead_time字段")
    modify_time: float = Field(description="modify_time字段")
    download_times: float = Field(description="download_times字段")
    uploader: float = Field(description="uploader字段")
    uploader_name: str = Field(description="uploader_name字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetGroupRootFilesReq(BaseModel):
    """获取群根目录文件列表"""
    group_id: group_id
    file_count: float | None = Field(None)

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupRootFilesRes(BaseModel):
    """获取群根目录文件列表"""
    class Data(BaseModel):
        """响应数据类型"""
        files: list[群文件信息] = Field(default=None, description="文件列表")
        folders: list[群文件夹信息] = Field(default=None, description="文件夹列表")

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
class GetGroupRootFilesAPI(BaseModel):
    """get_group_root_files接口数据模型"""
    endpoint: str = "get_group_root_files"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupRootFilesReq
    Res: type[BaseModel] = GetGroupRootFilesRes

# region api/
# endregion code

