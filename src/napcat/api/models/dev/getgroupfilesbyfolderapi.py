# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658865e0
@llms.txt: https://napcat.apifox.cn/226658865e0.md
@last_update: 2025-05-28 01:34:09

@description: 

summary:获取群子目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_group_files_by_folder"
__id__ = "226658865e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
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
class GetGroupFilesByFolderReq(BaseModel):
    """获取群子目录文件列表"""
    group_id: int | str = Field(description="群标识ID")
    folder_id: str | None = Field(None, description="和 folder 二选一")
    folder: str | None = Field(None, description="和 folder_id 二选一")
    file_count: float = Field(50.0, description="一次性获取的文件数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupFilesByFolderRes(BaseModel):
    """获取群子目录文件列表"""
    class Data(BaseModel):
        """响应数据类型"""
        files: list[群文件信息] = Field(description="文件列表")
        folders: list[群文件夹信息] = Field(description="文件夹列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="status字段")
    retcode: float = Field(0.0, description="retcode字段")
    data: Data = Field(default_factory=Data, description="data字段")
    message: str = Field("", description="message字段")
    wording: str = Field("", description="wording字段")
    echo: str | None = Field(None, description="echo字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetGroupFilesByFolderAPI(BaseModel):
    """get_group_files_by_folder接口数据模型"""
    endpoint: str = "get_group_files_by_folder"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupFilesByFolderReq
    Res: type[BaseModel] = GetGroupFilesByFolderRes

# region api/
# endregion code
