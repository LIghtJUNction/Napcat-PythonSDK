"""
获取群文件下载链接 API
用于获取指定群文件的下载链接
接口地址: https://napcat.apifox.cn/227449917e0.md

参数：
- group_id: 群号
- file_id: 文件ID
- busid: 文件类型

返回：
- 群文件下载链接信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class GetGroupFileUrlReq(BaseModel):
    """
    获取群文件下载链接 API 请求参数
    """
    group_id: int  # 群号
    file_id: str   # 文件ID
    busid: int     # 文件类型

class FileUrlInfo(BaseModel):
    """
    文件下载链接信息
    """
    url: str         # 下载URL
    file_name: str   # 文件名
    file_size: int   # 文件大小（字节）
    expire_time: int # 链接过期时间戳

class GetGroupFileUrlRes(BaseHttpResponse[FileUrlInfo]):
    """
    获取群文件下载链接 API 响应参数
    """
    pass