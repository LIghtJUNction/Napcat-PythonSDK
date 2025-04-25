# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658865e0
@llms.txt: https://napcat.apifox.cn/226658865e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群子目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_files_by_folder"
__id__ = "226658865e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field

# region req
class GetGroupFilesByFolderReq(BaseModel):
    """
    获取群子目录文件列表请求模型
    """

    group_id: int | str = Field(..., description="群号")
    folder_id: str | None = Field(None, description="文件夹ID, 和 folder 二选一")
    folder: str | None = Field(None, description="文件夹路径, 和 folder_id 二选一")
    file_count: int = Field(50, description="一次性获取的文件数量")

# endregion req


# region res

class File(BaseModel):
    """群文件信息模型"""
    group_id: int = Field(..., description="群号")
    file_id: str = Field(..., description="文件ID")
    file_name: str = Field(..., description="文件名")
    busid: int = Field(..., description="busid")
    size: int = Field(..., description="文件大小")
    upload_time: int = Field(..., description="上传时间 (Unix timestamp)")
    dead_time: int = Field(..., description="过期时间 (Unix timestamp)")
    modify_time: int = Field(..., description="修改时间 (Unix timestamp)")
    download_times: int = Field(..., description="下载次数")
    uploader: int = Field(..., description="上传者账号")
    uploader_name: str = Field(..., description="上传者昵称")

class Folder(BaseModel):
    """群文件夹信息模型"""
    group_id: int = Field(..., description="群号")
    folder_id: str = Field(..., description="文件夹ID")
    folder: str = Field(..., description="文件夹路径") # Note: The spec has 'folder' here, but it's likely a path, check spec if this is 'parent_id' or actual path string
    folder_name: str = Field(..., description="文件夹名称")
    create_time: str = Field(..., description="创建时间") # Note: Spec says string, might be better as datetime or int depending on format
    creator: str = Field(..., description="创建人账号")
    creator_name: str = Field(..., description="创建人昵称")
    total_file_count: str = Field(..., description="文件数量") # Note: Spec says string, likely better as int

class GetGroupFilesByFolderResData(BaseModel):
    """获取群子目录文件列表响应数据模型"""
    files: list[File] = Field(..., description="文件列表")
    folders: list[Folder] = Field(..., description="文件夹列表")

class GetGroupFilesByFolderRes(BaseModel):
    """
    获取群子目录文件列表响应模型
    """

    status: str = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: GetGroupFilesByFolderResData | None = Field(None, description="响应数据") # Based on apifox spec, 'data' is required, but could be null or empty
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(None, description="echo")

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
