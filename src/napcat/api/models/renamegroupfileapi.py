# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136375e0
@llms.txt: https://napcat.apifox.cn/283136375e0.md
@last_update: 2025-04-27 00:53:41

@description: 

summary:重命名群文件

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "rename_group_file"
__id__ = "283136375e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class RenameGroupFileReq(BaseModel):
    """
    重命名群文件 请求模型
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    file_id: str = Field(
        ..., description="文件ID"
    )
    current_parent_directory: str = Field(
        ..., description="当前文件所在的父目录"
    )
    new_name: str = Field(
        ..., description="新文件名"
    )
# endregion req



# region res
class RenameGroupFileRes(BaseModel):
    """
    重命名群文件 响应模型
    """
    class Data(BaseModel):
        """
        响应数据data字段模型
        """
        ok: bool = Field(..., description="操作是否成功")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="响应码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="响应消息")
    wording: str = Field(..., description="响应描述")
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