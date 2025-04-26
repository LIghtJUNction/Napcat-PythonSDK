# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658823e0
@llms.txt: https://napcat.apifox.cn/226658823e0.md
@last_update: 2025-04-27 00:53:40

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
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region models

class GroupId(BaseModel):
    """
    群号，可以是数字或字符串
    """
    __root__: int | str

class GroupFileInfo(BaseModel):
    """
    群文件信息
    """
    group_id: int = Field(..., description="群号")
    file_id: str = Field(..., description="文件ID")
    file_name: str = Field(..., description="文件名称")
    busid: int = Field(..., description="业务ID")
    size: int = Field(..., description="文件大小 (bytes)")
    file_size: int = Field(..., description="文件大小 (bytes), 同 size")
    upload_time: int = Field(..., description="上传时间 (时间戳)")
    dead_time: int = Field(..., description="过期时间 (时间戳)")
    modify_time: int = Field(..., description="修改时间 (时间戳)")
    download_times: int = Field(..., description="下载次数")
    uploader: int = Field(..., description="上传者QQ号")
    uploader_name: str = Field(..., description="上传者昵称")

class GroupFolderInfo(BaseModel):
    """
    群文件夹信息
    """
    group_id: int = Field(..., description="群号")
    folder_id: str = Field(..., description="文件夹ID")
    folder: str = Field(..., description="文件夹名") # OpenAPI spec shows 'folder', but description says '文件夹名称', seems inconsistent but using 'folder' as per property name
    folder_name: str = Field(..., description="文件夹名称")
    create_time: int = Field(..., description="创建时间 (时间戳)")
    creator: int = Field(..., description="创建人账号 (QQ号)")
    creator_name: str = Field(..., description="创建人昵称")
    total_file_count: int = Field(..., description="文件夹内的文件数量")

# endregion models


# region req
class GetGroupRootFilesReq(BaseModel):
    """
    获取群根目录文件列表请求
    """
    group_id: GroupId = Field(..., description="群号")
    file_count: int = Field(50, description="文件数量限制")
# endregion req



# region res

class GetGroupRootFilesResData(BaseModel):
    """
    获取群根目录文件列表响应数据
    """
    files: list[GroupFileInfo] = Field(..., description="文件列表")
    folders: list[GroupFolderInfo] = Field(..., description="文件夹列表")


class GetGroupRootFilesRes(BaseModel):
    """
    获取群根目录文件列表响应
    """\n    status: Literal["ok"] = Field(..., description="响应状态")
    retcode: int = Field(..., description="响应码")
    data: GetGroupRootFilesResData = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应提示")
    echo: str | None = Field(None, description="回显")

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
