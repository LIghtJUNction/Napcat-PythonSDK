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
from typing import Literal

# region component_models
# The original 'group_id' BaseModel was incorrect as per OpenAPI schema.
# The OpenAPI schema indicates group_id is directly a number or string, not an object.
# Thus, it has been removed.

# The 'result' BaseModel from OpenAPI is a generic response structure,
# but 'GetGroupRootFilesRes' directly defines its fields based on the specific API response.
# Thus, it has been removed to avoid redundancy and better reflect the actual response structure.

class 群文件夹信息(BaseModel):
    group_id: float = Field(..., description="group_id字段")
    folder_id: str = Field(..., description="folder_id字段")
    folder: str = Field(..., description="folder字段")
    folder_name: str = Field(..., description="文件夹名称")
    create_time: float = Field(..., description="创建时间")
    creator: float = Field(..., description="创建人账号")
    creator_name: str = Field(..., description="创建人昵称")
    total_file_count: float = Field(..., description="文件数量")

    model_config = {
        "extra": "allow",
    }

class 群文件信息(BaseModel):
    group_id: float = Field(..., description="group_id字段")
    file_id: str = Field(..., description="file_id字段")
    file_name: str = Field(..., description="file_name字段")
    busid: float = Field(..., description="busid字段")
    size: float = Field(..., description="size字段")
    file_size: float = Field(..., description="file_size字段")
    upload_time: float = Field(..., description="upload_time字段")
    dead_time: float = Field(..., description="dead_time字段")
    modify_time: float = Field(..., description="modify_time字段")
    download_times: float = Field(..., description="download_times字段")
    uploader: float = Field(..., description="uploader字段")
    uploader_name: str = Field(..., description="uploader_name字段")

    model_config = {
        "extra": "allow",
    }
# endregion component_models/

# region req
class GetGroupRootFilesReq(BaseModel):
    """获取群根目录文件列表"""
    # Based on OpenAPI 'group_id' schema: oneOf: [number, string]
    group_id: float | str = Field(..., description="群ID")

    # OpenAPI specifies default: 50
    file_count: float = Field(50.0, description="获取文件数量，默认50")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetGroupRootFilesRes(BaseModel):
    """获取群根目录文件列表"""
    class Data(BaseModel):
        """响应数据类型"""
        # OpenAPI indicates files and folders are required and can be empty arrays
        files: list[群文件信息] = Field([], description="文件列表")
        folders: list[群文件夹信息] = Field([], description="文件夹列表")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="status字段，固定为'ok'")
    retcode: float = Field(0.0, description="retcode字段，默认0")
    data: Data = Field(default_factory=Data, description="data字段")
    message: str = Field("", description="message字段，默认空字符串")
    wording: str = Field("", description="wording字段，默认空字符串")
    echo: str | None = Field(None, description="echo字段，可能为null")

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
