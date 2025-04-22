# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226658779e0
@endpoint: delete_group_folder
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658779e0
@llms.txt: https://napcat.apifox.cn/226658779e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: delete_group_folder API
@usage: 使用 `client.delete_group_folder()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_folder"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    -
    -
    -
    -
    -
    -
    -
    # 本行注释旨在测试构建清理逻辑


# region req
class DeleteGroupFolderReq(BaseHttpRequest):
    """
    delete_group_folder 请求参数
    """

    pass
# region req/

# region data
class DeleteGroupFolderData(BaseModel):
    """
    delete_group_folder 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class DeleteGroupFolderRes(BaseHttpResponse[DeleteGroupFolderData]):
    """
    delete_group_folder 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class DeleteGroupFolderAPI(BaseHttpAPI[DeleteGroupFolderReq, DeleteGroupFolderRes]):
    """
    删除群文件夹
    """
    api: str = "/delete_group_folder"
    method: Literal["POST", "GET"] = "POST"

    Request = DeleteGroupFolderReq
    Response = DeleteGroupFolderRes

    request: DeleteGroupFolderReq
    response: DeleteGroupFolderRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(DeleteGroupFolderAPI)

# region code/

