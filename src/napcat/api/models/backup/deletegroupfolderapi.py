# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658779e0
@llms.txt: https://napcat.apifox.cn/226658779e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:删除群文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_folder"
__id__ = "226658779e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class DeleteGroupFolderReq(BaseModel):
    """
    删除群文件夹请求模型
    """

    group_id: int | str = Field(
        ..., description="群号"
    )
    folder_id: str = Field(
        ..., description="文件夹ID"
    )
# endregion req



# region res
class DeleteGroupFolderRes(BaseModel):
    """
    删除群文件夹响应模型
    """
    class Data(BaseModel):
        """
        响应数据详情
        """
        retCode: int = Field(..., description="返回码")
        retMsg: str = Field(..., description="返回信息")
        clientWording: str = Field(..., description="客户端提示信息")

    status: str = Field(..., description="状态, 'ok' 表示成功")
    retcode: int = Field(..., description="状态码")
    data: Data = Field(..., description="响应数据详情")
    message: str = Field(..., description="错误信息, 当 status 不为 'ok' 时有效")
    wording: str = Field(..., description="错误提示, 当 status 不为 'ok' 时有效")
    echo: str | None = Field(None, description="发送请求时携带的 echo", alias="echo") # Use Field for nullable with alias

# endregion res

# region api
class DeleteGroupFolderAPI(BaseModel):
    """delete_group_folder接口数据模型"""
    endpoint: str = "delete_group_folder"
    method: str = "POST"
    Req: type[BaseModel] = DeleteGroupFolderReq
    Res: type[BaseModel] = DeleteGroupFolderRes
# endregion api




# endregion code
