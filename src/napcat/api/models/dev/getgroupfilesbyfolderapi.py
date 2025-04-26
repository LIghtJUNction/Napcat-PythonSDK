# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658865e0
@llms.txt: https://napcat.apifox.cn/226658865e0.md
@last_update: 2025-04-27 00:53:40

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
import logging
from pydantic import BaseModel, Field
from typing import Literal # Use Literal for const/enum values

logger = logging.getLogger(__name__)

# region req
class GetGroupFilesByFolderReq(BaseModel):
    """
    获取群子目录文件列表 请求模型
    """
    group_id: int | str = Field(
        ...,
        description="群号",
    )
    folder_id: str | None = Field(
        None,
        description="和 folder 二选一",
    )
    folder: str | None = Field(
        None,
        description="和 folder_id 二选一",
    )
    file_count: int = Field(
        50,
        description="一次性获取的文件数量",
    )
# endregion req



# region res

class GroupFileInfo(BaseModel):
    """
    群文件信息
    """
    group_id: int = Field(..., description="群号")
    file_id: str = Field(..., description="文件ID")
    file_name: str = Field(..., description="文件名")
    busid: int = Field(..., description="业务ID")
    size: int = Field(..., description="文件大小 (旧字段)")
    file_size: int = Field(..., description="文件大小")
    upload_time: int = Field(..., description="上传时间")
    dead_time: int = Field(..., description="过期时间")
    modify_time: int = Field(..., description="修改时间")
    download_times: int = Field(..., description="下载次数")
    uploader: int = Field(..., description="上传者账号")
    uploader_name: str = Field(..., description="上传者昵称")

class GroupFolderInfo(BaseModel):
    """
    群文件夹信息
    """
    group_id: int = Field(..., description="群号")
    folder_id: str = Field(..., description="文件夹ID")
    folder: str = Field(..., description="文件夹路径 (旧字段)")
    folder_name: str = Field(..., description="文件夹名称")
    create_time: int = Field(..., description="创建时间")
    creator: int = Field(..., description="创建人账号")
    creator_name: str = Field(..., description="创建人昵称")
    total_file_count: int = Field(..., description="文件数量")

class GetGroupFilesByFolderResData(BaseModel):
    """
    获取群子目录文件列表 响应数据
    """
    files: list[GroupFileInfo] = Field(..., description="文件列表")
    folders: list[GroupFolderInfo] | None = Field(None, description="文件夹列表") # Based on schema, folders is not required in data object


class GetGroupFilesByFolderRes(BaseModel):
    """
    获取群子目录文件列表 响应模型
    """
    status: Literal["ok"] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: GetGroupFilesByFolderResData = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="补充信息")
    echo: str | None = Field(None, description="Echo")

# endregion res

# region api
class GetGroupFilesByFolderAPI(BaseModel):
    """get_group_files_by_folder接口数据模型"""
    endpoint: str = "get_group_files_by_folder"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupFilesByFolderReq
    Res: type[BaseModel] = GetGroupFilesByFolderRes
# endregion api




# endregion code
