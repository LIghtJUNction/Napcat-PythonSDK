# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658779e0
@llms.txt: https://napcat.apifox.cn/226658779e0.md
@last_update: 2025-05-28 01:34:09

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
from pydantic import BaseModel, Field
from typing import Literal

# region component_models
class result(BaseModel):
    """
    通用响应结果模型，对应 OpenAPI components/schemas/result
    """
    status: Literal["ok"] = Field(description="status字段，固定为 'ok'")
    retcode: float = Field(description="retcode字段")
    data: dict = Field(description="data字段，一个任意结构的字典")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# endregion component_models/

# region req
class DeleteGroupFolderReq(BaseModel):
    """删除群文件夹的请求模型"""
    # group_id 字段根据 OpenAPI 定义应为 number 或 string
    group_id: int | str = Field(description="群组ID，可以是群号(int)或群字符串ID(str)")
    folder_id: str = Field(description="文件夹ID")

    model_config = {
        "extra": "allow",
    }
# endregion req/


# region res
class DeleteGroupFolderRes(BaseModel):
    """删除群文件夹的响应模型"""
    class Data(BaseModel):
        """响应数据类型"""
        # 根据 OpenAPI specification，这些字段是 required 且没有默认值，因此不设置 default
        retCode: float = Field(description="retCode字段")
        retMsg: str = Field(description="retMsg字段")
        clientWording: str = Field(description="clientWording字段")

        model_config = {
            "extra": "allow",
        }

    status: Literal["ok"] = Field(description="status字段，固定为 'ok'")
    retcode: float = Field(description="retcode字段")
    # data 字段是 required，Pydantic 会从响应数据中解析，不需要 default_factory
    data: Data = Field(description="data字段")
    message: str = Field(description="message字段")
    wording: str = Field(description="wording字段")
    echo: str | None = Field(description="echo字段")

    model_config = {
        "extra": "allow",
    }
# endregion res/

# region api
class DeleteGroupFolderAPI(BaseModel):
    """delete_group_folder接口数据模型"""
    endpoint: str = "delete_group_folder"
    method: str = "POST"
    Req: type[BaseModel] = DeleteGroupFolderReq
    Res: type[BaseModel] = DeleteGroupFolderRes

# endregion api/
# endregion code