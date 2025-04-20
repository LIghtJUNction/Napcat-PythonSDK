"""
下载文件到缓存目录 API
用于下载群文件或私聊文件到本地缓存目录
接口地址: https://napcat.apifox.cn/226658887e0.md

参数：
- url: 文件下载链接
- thread_count: 下载线程数(可选)，默认为单线程下载
- headers: 自定义HTTP请求头(可选)

返回：
- 下载结果信息，包含下载后的本地文件路径

# NapCat 开发中
"""

# 具体实现内容将根据API规范添加

"""
下载文件 API
用于下载指定的文件
接口地址: https://napcat.apifox.cn/227492775e0.md

参数：
- file_id: 文件ID
- file_type: 文件类型，群文件: group，私聊文件: private，共享文件: share
- download_path: 下载保存的路径

返回：
- 下载结果和保存路径信息

# NapCat 开发中
"""

from typing import TypedDict, Literal
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class DownloadFileReq(TypedDict):
    """
    下载文件 API 请求参数
    """
    file_id: str  # 文件ID
    file_type: Literal["group", "private", "share"]  # 文件类型
    download_path: str  # 下载保存的路径

class DownloadResult(TypedDict):
    """
    下载结果信息
    """
    file_path: str  # 文件保存路径
    file_name: str  # 文件名称
    file_size: int  # 文件大小（字节）
    success: bool   # 下载是否成功

class DownloadFileRes(BaseHttpResponse[DownloadResult]):
    """
    下载文件 API 响应参数
    """
    pass