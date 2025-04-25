# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136375e0
@llms.txt: https://napcat.apifox.cn/283136375e0.md
@last_update: 2025-04-26 01:17:46

@description: 

summary:重命名群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "rename_group_file"
__id__ = "283136375e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field


# region req
class RenameGroupFileReq(BaseModel):
    """
    重命名群文件请求体
    """

    group_id: int | str = Field(
        ..., description="群号")
    file_id: str = Field(..., description="文件 ID")
    current_parent_directory: str = Field(
        ..., description="当前文件所在的目录")
    new_name: str = Field(..., description="新的文件名")

# endregion req


# region res
class RenameGroupFileRes(BaseModel):
    """
    重命名群文件响应体
    """

    class Data(BaseModel):
        """
        响应数据
        """
        ok: bool = Field(..., description="是否成功")

    status: str = Field(
        'ok', description="响应状态", const=True
    ) # Pydantic v2 const is True for literal values
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="错误信息")
    wording: str = Field(..., description="错误提示")
    echo: str | None = Field(None, description="echo")

# endregion res

# region api
class RenameGroupFileAPI(BaseModel):
    """rename_group_file接口数据模型"""
    endpoint: str = "rename_group_file"
    method: str = "POST"
    Req: type[BaseModel] = RenameGroupFileReq
    Res: type[BaseModel] = RenameGroupFileRes
# endregion api


# endregion code
