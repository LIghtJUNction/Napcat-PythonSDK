# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658773e0
@llms.txt: https://napcat.apifox.cn/226658773e0.md
@last_update: 2025-05-28 01:34:09

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
from typing import Any, Literal
import logging

logger = logging.getLogger(__name__)

# region req
class CreateGroupFileFolderReq(BaseModel):
    """创建群文件文件夹请求模型"""
    group_id: int | str = Field(description="群组标识ID，可以是数字或字符串")
    folder_name: str = Field(description="要创建的文件夹名称")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class CreateGroupFileFolderRes(BaseModel):
    """创建群文件文件夹响应模型"""
    class Data(BaseModel):
        """响应数据类型"""
        class Result(BaseModel):
            """操作结果信息"""
            retCode: int = Field(description="返回码")
            retMsg: str = Field(description="返回消息")
            clientWording: str = Field(description="客户端提示语")

            model_config = {
                "extra": "allow",
            }

        class GroupItem(BaseModel):
            """群组文件项信息"""
            peerId: str = Field(description="对端ID")
            type: int = Field(description="类型")

            class FolderInfo(BaseModel):
                """文件夹详细信息"""
                folderId: str = Field(description="文件夹ID")
                parentFolderId: str = Field(description="父文件夹ID")
                folderName: str = Field(description="文件夹名称")
                createTime: int = Field(description="创建时间戳")
                modifyTime: int = Field(description="修改时间戳")
                createUin: str = Field(description="创建者UIN")
                creatorName: str = Field(description="创建者名称")
                totalFileCount: int = Field(description="文件夹内文件总数")
                modifyUin: str = Field(description="修改者UIN")
                modifyName: str = Field(description="修改者名称")
                usedSpace: str = Field(description="已使用空间大小")

                model_config = {
                    "extra": "allow",
                }

            folderInfo: FolderInfo = Field(description="文件夹信息")
            fileInfo: str | None = Field(None, description="文件信息，如果适用")

            model_config = {
                "extra": "allow",
            }

        result: Result = Field(description="操作结果详情")
        groupItem: GroupItem = Field(description="群组文件项详情")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field("ok", description="响应状态，固定为 'ok'")
    retcode: float = Field(description="响应返回码")
    data: Data = Field(default_factory=Data, description="响应数据内容")
    message: str = Field(description="响应消息")
    wording: str = Field(description="响应提示语")
    echo: str | None = Field(None, description="回显信息，可能为空")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class CreateGroupFileFolderAPI(BaseModel):
    """create_group_file_folder接口数据模型"""
    endpoint: str = "create_group_file_folder"
    method: str = "POST"
    Req: type[BaseModel] = CreateGroupFileFolderReq
    Res: type[BaseModel] = CreateGroupFileFolderRes

# region api/
# endregion code
