"""
获取群文件系统信息 API
用于获取指定群的文件系统信息，包括容量、已使用空间等
接口地址: https://napcat.apifox.cn/227449759e0.md

参数：
- group_id: 群号

返回：
- 群文件系统信息，包括容量限制和使用情况

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupFileSystemInfoReq(BaseModel):
    """
    获取群文件系统信息 API 请求参数
    """
    group_id: int  # 群号

class FileSystemInfo(BaseModel):
    """
    文件系统信息
    """
    file_count: int       # 文件总数
    limit_count: int      # 文件数量上限
    used_space: int       # 已使用空间（字节）
    total_space: int      # 空间总大小（字节）

class GetGroupFileSystemInfoRes(BaseHttpResponse[FileSystemInfo]):
    """
    获取群文件系统信息 API 响应参数
    """
    pass