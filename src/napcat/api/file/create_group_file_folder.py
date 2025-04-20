"""
创建群文件文件夹 API
用于在群文件系统中创建新的文件夹
接口地址: https://napcat.apifox.cn/227450004e0.md

参数：
- group_id: 群号
- name: 文件夹名称
- parent_id: 父文件夹ID，空字符串表示在根目录创建

返回：
- 创建结果信息

# NapCat 开发中
"""

from pydantic import BaseModel
from napcat.api.base.models import BaseHttpResponse

class CreateGroupFileFolderReq(BaseModel):
    """
    创建群文件文件夹 API 请求参数
    """
    group_id: int  # 群号
    name: str      # 文件夹名称
    parent_id: str # 父文件夹ID，空字符串表示在根目录创建

class FolderInfo(BaseModel):
    """
    创建的文件夹信息
    """
    folder_id: str    # 文件夹ID
    folder_name: str  # 文件夹名称

class CreateGroupFileFolderRes(BaseHttpResponse[FolderInfo]):
    """
    创建群文件文件夹 API 响应参数
    """
    pass