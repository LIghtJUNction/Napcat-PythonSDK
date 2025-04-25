# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658753e0
@llms.txt: https://napcat.apifox.cn/226658753e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:上传群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
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
    上传群文件请求体
    """
    group_id: int | str = Field(..., description="群号") # 根据components/schemas/group_id定义
    file: str = Field(..., description="文件路径")
    name: str = Field(..., description="文件名")
    folder_id: str = Field(..., description="文件夹ID")

# endregion req



# region res
class UploadGroupFileRes(BaseModel):
    """
    上传群文件响应体
    """
    status: Literal["ok"] = Field("ok", description="状态")
    retcode: int | float = Field(..., description="状态码")
    data: None = Field(..., description="响应数据，在此接口中固定为null") # 根据响应体data schema定义
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="附加信息")
    echo: str | None = Field(..., description="Echo回显") # nullable: true but required

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