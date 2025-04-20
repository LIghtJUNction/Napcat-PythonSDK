"""
上传群文件 API
用于向群文件系统上传新文件
接口地址: https://napcat.apifox.cn/227449969e0.md

参数：
- group_id: 群号
- file: 本地文件路径
- name: 上传后的文件名
- folder: 上传目标文件夹ID，空字符串表示上传到根目录

返回：
- 上传结果信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class UploadGroupFileReq(BaseModel):
    """
    上传群文件 API 请求参数
    """
    group_id: int  # 群号
    file: str      # 本地文件路径
    name: str      # 上传后的文件名
    folder: str    # 上传目标文件夹ID，空字符串表示上传到根目录

class UploadResult(BaseModel):
    """
    上传结果信息
    """
    file_id: str     # 文件ID
    file_name: str   # 文件名
    file_size: int   # 文件大小（字节）
    busid: int       # 文件类型

class UploadGroupFileRes(BaseHttpResponse[UploadResult]):
    """
    上传群文件 API 响应参数
    """
    pass