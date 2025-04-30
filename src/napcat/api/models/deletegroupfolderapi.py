# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658779e0
@llms.txt: https://napcat.apifox.cn/226658779e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:删除群文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "delete_group_folder"
__id__ = "226658779e0"
__method__ = "POST"

# endregion METADATA


# region code
from typing import Literal
from pydantic import BaseModel, Field

# logger is defined but not used directly, maybe useful for future debugging
# logger = logging.getLogger(__name__)

# region req
class DeleteGroupFolderReq(BaseModel):
    """
    删除群文件夹请求参数
    """
    group_id: int | str = Field(..., description="群号")
    folder_id: str = Field(..., description="文件或文件夹ID")
# endregion req



# region res
class DeleteGroupFolderRes(BaseModel):
    """
    删除群文件夹响应参数
    """

    class DeleteGroupFolderResData(BaseModel):
        """
        响应数据详情
        """
        retCode: int = Field(..., description="返回码")
        retMsg: str = Field(..., description="返回信息")
        clientWording: str = Field(..., description="给客户端的提示信息")

    # Corrected status field according to rule 2
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: DeleteGroupFolderResData = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="提示词")
    echo: str | None = Field(None, description="回显")
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