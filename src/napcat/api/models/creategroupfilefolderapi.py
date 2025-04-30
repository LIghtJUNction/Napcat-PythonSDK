# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658773e0
@llms.txt: https://napcat.apifox.cn/226658773e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:创建群文件文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "create_group_file_folder"
__id__ = "226658773e0"
__method__ = "POST"

# endregion METADATA


# region code
from pydantic import BaseModel, Field
from typing import Literal


# region req
class CreateGroupFileFolderReq(BaseModel):
    """
    请求模型：创建群文件文件夹
    """

    group_id: int | str = Field(..., description="群号")
    folder_name: str = Field(..., description="文件夹名称")

# endregion req



# region res
class CreateGroupFileFolderRes(BaseModel):
    """
    响应模型：创建群文件文件夹
    """

    class Data(BaseModel):
        """
        响应数据
        """
        class Result(BaseModel):
            """
            操作结果
            """
            retCode: int = Field(..., description="返回码")
            retMsg: str = Field(..., description="返回消息")
            clientWording: str = Field(..., description="客户端提示")

        class GroupItem(BaseModel):
            """
            群文件信息项
            """
            class FolderInfo(BaseModel):
                """
                文件夹信息
                """
                folderId: str = Field(..., description="文件夹ID")
                parentFolderId: str = Field(..., description="父文件夹ID")
                folderName: str = Field(..., description="文件夹名称")
                createTime: int = Field(..., description="创建时间")
                modifyTime: int = Field(..., description="修改时间")
                createUin: str = Field(..., description="创建者UIN")
                creatorName: str = Field(..., description="创建者名称")
                totalFileCount: int = Field(..., description="文件总数")
                modifyUin: str = Field(..., description="修改者UIN")
                modifyName: str = Field(..., description="修改者名称")
                usedSpace: str = Field(..., description="已用空间")

            peerId: str = Field(..., description="对端ID")
            type: int = Field(..., description="类型")
            folderInfo: FolderInfo = Field(..., description="文件夹信息")
            fileInfo: str | None = Field(None, description="文件信息 (可能为null)")

        result: Result = Field(..., description="操作结果")
        groupItem: GroupItem = Field(..., description="群文件信息项")

    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示")
    echo: str | None = Field(None, description="回显")

# endregion res

# region api
class CreateGroupFileFolderAPI(BaseModel):
    """create_group_file_folder接口数据模型"""
    endpoint: str = "create_group_file_folder"
    method: str = "POST"
    Req: type[BaseModel] = CreateGroupFileFolderReq
    Res: type[BaseModel] = CreateGroupFileFolderRes
# endregion api




# endregion code