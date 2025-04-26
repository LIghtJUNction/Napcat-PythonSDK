# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658753e0
@llms.txt: https://napcat.apifox.cn/226658753e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:上传群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "upload_group_file"
__id__ = "226658753e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# region req
class UploadGroupFileReq(BaseModel):
    """
    上传群文件请求模型
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    file: str = Field(
        ..., description="文件路径"
    )
    name: str = Field(
        ..., description="文件名"
    )
    folder: str | None = Field(
        default=None, description="文件夹ID（二选一）"
    )
    folder_id: str | None = Field(
        default=None, description="文件夹ID（二选一）"
    )
# endregion req



# region res
class UploadGroupFileRes(BaseModel):
    """
    上传群文件响应模型
    """
    
    status: Literal["ok"] = Field(
        ..., description="状态"
    )
    retcode: int = Field(
        ..., description="返回码"
    )
    data: None = Field(
        ..., description="数据体 (此接口数据体为 null)"
    )
    message: str = Field(
        ..., description="消息"
    )
    wording: str = Field(
        ..., description="提示信息"
    )
    echo: str | None = Field(
        default=None, description="Echo回显"
    )
# endregion res

# region api
class UploadGroupFileAPI(BaseModel):
    """upload_group_file接口数据模型"""
    endpoint: str = "upload_group_file"
    method: str = "POST"
    Req: type[BaseModel] = UploadGroupFileReq
    Res: type[BaseModel] = UploadGroupFileRes
# endregion api




# endregion code
