"""
获取群根目录文件列表 API
用于获取群文件系统根目录下的文件和文件夹列表
接口地址: https://napcat.apifox.cn/227449787e0.md

参数：
- group_id: 群号

返回：
- 根目录下的文件和文件夹列表

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupRootFilesReq(BaseModel):
    """
    获取群根目录文件列表 API 请求参数
    """
    group_id: int  # 群号

class GroupFile(BaseModel):
    """
    群文件信息
    """
    file_id: str       # 文件ID
    file_name: str     # 文件名
    busid: int         # 文件类型
    file_size: int     # 文件大小（字节）
    upload_time: int   # 上传时间戳
    dead_time: int     # 过期时间戳
    modify_time: int   # 最后修改时间戳
    download_times: int # 下载次数
    uploader: int      # 上传者QQ号
    uploader_name: str # 上传者名称

class GroupFolder(BaseModel):
    """
    群文件夹信息
    """
    folder_id: str     # 文件夹ID
    folder_name: str   # 文件夹名称
    create_time: int   # 创建时间戳
    creator: int       # 创建者QQ号
    creator_name: str  # 创建者名称
    total_file_count: int  # 文件夹中文件总数

class GroupRootFiles(BaseModel):
    """
    群根目录文件列表
    """
    files: list[GroupFile]      # 文件列表
    folders: list[GroupFolder]  # 文件夹列表

class GetGroupRootFilesRes(BaseHttpResponse[GroupRootFiles]):
    """
    获取群根目录文件列表 API 响应参数
    """
    pass