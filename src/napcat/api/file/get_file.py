"""
获取文件信息 API
用于获取指定文件的信息
接口地址: https://napcat.apifox.cn/227492775e0.md

参数：
- file_id: 文件ID
- file_type: 文件类型，群文件: group，私聊文件: private，共享文件: share

返回：
- 文件的详细信息

# NapCat 开发中
"""

from typing import Literal
from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetFileReq(BaseModel):
    """
    获取文件信息 API 请求参数
    """
    file_id: str  # 文件ID
    file_type: Literal["group", "private", "share"]  # 文件类型

class FileInfo(BaseModel):
    """
    文件信息
    """
    file_id: str       # 文件ID
    file_name: str     # 文件名称
    file_size: int     # 文件大小（字节）
    upload_time: int   # 上传时间戳
    uploader: int      # 上传者QQ号
    file_type: str     # 文件类型
    expire_time: int   # 过期时间戳
    download_times: int # 下载次数

class GetFileRes(BaseHttpResponse[FileInfo]):
    """
    获取文件信息 API 响应参数
    """
    pass