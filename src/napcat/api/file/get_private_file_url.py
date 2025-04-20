"""
获取私聊文件下载链接 API
用于获取私聊消息中的文件下载链接
接口地址: https://napcat.apifox.cn/227450162e0.md

参数：
- user_id: 用户QQ号
- file_id: 文件ID
- busid: 文件类型

返回：
- 私聊文件下载链接信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class GetPrivateFileUrlReq(TypedDict):
    """
    获取私聊文件下载链接 API 请求参数
    """
    user_id: int  # 用户QQ号
    file_id: str  # 文件ID
    busid: int    # 文件类型

class PrivateFileUrl(TypedDict):
    """
    私聊文件下载链接信息
    """
    url: str         # 下载URL
    file_name: str   # 文件名
    file_size: int   # 文件大小（字节）
    expire_time: int # 链接过期时间戳

class GetPrivateFileUrlRes(BaseHttpResponse[PrivateFileUrl]):
    """
    获取私聊文件下载链接 API 响应参数
    """
    pass