"""
上传私聊文件 API
用于向指定用户发送文件
接口地址: https://napcat.apifox.cn/227450195e0.md

参数：
- user_id: 对方QQ号
- file: 本地文件路径
- name: 上传后的文件名

返回：
- 上传结果信息

# NapCat 开发中
"""

from typing import TypedDict
from napcat.api.base.models import BaseHttpResponse
# region TypedDicts
class UploadPrivateFileReq(TypedDict):
    """
    上传私聊文件 API 请求参数
    """
    user_id: int  # 对方QQ号
    file: str     # 本地文件路径
    name: str     # 上传后的文件名

class PrivateUploadResult(TypedDict):
    """
    私聊文件上传结果
    """
    file_id: str     # 文件ID
    file_name: str   # 文件名
    file_size: int   # 文件大小（字节）
    busid: int       # 文件类型

class UploadPrivateFileRes(BaseHttpResponse[PrivateUploadResult]):
    """
    上传私聊文件 API 响应参数
    """
    pass