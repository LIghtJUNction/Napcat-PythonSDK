# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658773e0
@llms.txt: https://napcat.apifox.cn/226658773e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:创建群文件文件夹

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "create_group_file_folder"
__id__ = "226658773e0"
__method__ = "POST"

# endregion METADATA


# region code

from pydantic import BaseModel, Field

# region req
class CreateGroupFileFolderReq(BaseModel):
    """
    创建群文件文件夹请求模型
    """

    group_id: int | str = Field(..., description="群号")
    folder_name: str = Field(..., description="文件夹名称")

# endregion req



# region res
class CreateGroupFileFolderRes(BaseModel):
    """
    创建群文件文件夹响应模型
    """

    class FolderInfo(BaseModel):
        """
        文件夹信息
        """
        folderId: str = Field(..., description="文件夹ID")
        parentFolderId: str = Field(..., description="父文件夹ID")
        folderName: str = Field(..., description="文件夹名称")
        createTime: int = Field(..., description="创建时间戳")
        modifyTime: int = Field(..., description="修改时间戳")
        createUin: str = Field(..., description="创建者Uin")
        creatorName: str = Field(..., description="创建者昵称")
        totalFileCount: str = Field(..., description="文件总数")
        modifyUin: str = Field(..., description="修改者Uin")
        modifyName: str = Field(..., description="修改者昵称")
        usedSpace: str = Field(..., description="已用空间")

    class GroupItem(BaseModel):
        """
        群组信息
        """
        peerId: str = Field(..., description="群组ID")
        type: str = Field(..., description="类型") # Possible values? e.g., "group"
        folderInfo: FolderInfo = Field(..., description="文件夹信息")

    class Result(BaseModel):
        """
        内部操作结果
        """
        retCode: int = Field(..., description="返回码")
        retMsg: str = Field(..., description="返回信息")
        clientWording: str = Field(..., description="客户端提示文字")

    class Data(BaseModel):
        """
        响应数据体
        """
        result: Result = Field(..., description="内部操作结果")
        groupItem: GroupItem = Field(..., description="群组和文件夹信息")

    status: str = Field(..., description="状态码", const="ok")
    retcode: int = Field(..., description="返回码")
    data: Data = Field(..., description="响应数据")
    message: str = Field(..., description="信息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="Echo数据")

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
