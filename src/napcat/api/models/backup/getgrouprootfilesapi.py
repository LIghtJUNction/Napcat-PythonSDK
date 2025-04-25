# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658823e0
@llms.txt: https://napcat.apifox.cn/226658823e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取群根目录文件列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_root_files"
__id__ = "226658823e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal

# region req
class GetGroupRootFilesReq(BaseModel):
    """
    获取群根目录文件列表的请求模型
    """
    group_id: int | str = Field(
        ..., description="群号"
    )
    file_count: int = Field(
        50, description="文件数量"
    )
# endregion req



# region res
class File(BaseModel):
    """
    文件信息模型
    """
    group_id: int = Field(..., description="群号")
    file_id: str = Field(..., description="文件ID")
    file_name: str = Field(..., description="文件名称")
    busid: int = Field(..., description="busid")
    size: int = Field(..., description="文件大小")
    file_size: int = Field(..., description="文件大小") # Duplicate field name in spec, assuming same meaning as size
    upload_time: int = Field(..., description="上传时间")
    dead_time: int = Field(..., description="过期时间")
    modify_time: int = Field(..., description="修改时间")
    download_times: int = Field(..., description="下载次数")
    uploader: int = Field(..., description="上传者账号")
    uploader_name: str = Field(..., description="上传者昵称")

class Folder(BaseModel):
    """
    文件夹信息模型
    """
    group_id: int = Field(..., description="群号")
    folder_id: str = Field(..., description="文件夹ID")
    folder: str = Field(..., description="文件夹") # Note: field name is 'folder' in spec
    folder_name: str = Field(..., description="文件夹名称")
    create_time: int = Field(..., description="创建时间")
    creator: int = Field(..., description="创建人账号")
    creator_name: str = Field(..., description="创建人昵称")
    total_file_count: int = Field(..., description="文件数量")

class Data(BaseModel):
    """
    响应数据部分模型
    """
    files: list[File] = Field(..., description="文件列表")
    folders: list[Folder] = Field(..., description="文件夹列表")

class GetGroupRootFilesRes(BaseModel):
    """
    获取群根目录文件列表的响应模型
    """
    status: Literal['ok'] = Field(..., description="状态")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="文案")
    echo: str | None = Field(..., description="回显")

# endregion res

# region api
class GetGroupRootFilesAPI(BaseModel):
    """get_group_root_files接口数据模型"""
    endpoint: str = "get_group_root_files"
    method: str = "POST"
    Req: type[BaseModel] = GetGroupRootFilesReq
    Res: type[BaseModel] = GetGroupRootFilesRes
# endregion api




# endregion code