# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226658755e0
@endpoint: delete_group_file
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658755e0
@llms.txt: https://napcat.apifox.cn/226658755e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: delete_group_file API
@usage: 使用 `client.delete_group_file()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "delete_group_file"
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
class DeleteGroupFileReq(BaseHttpRequest):
    """
    delete_group_file 请求参数
    """

    pass
# region req/

# region data
class DeleteGroupFileData(BaseModel):
    """
    delete_group_file 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class DeleteGroupFileRes(BaseHttpResponse[DeleteGroupFileData]):
    """
    delete_group_file 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class DeleteGroupFileAPI(BaseHttpAPI[DeleteGroupFileReq, DeleteGroupFileRes]):
    """
    删除群文件
    """
    api: str = "/delete_group_file"
    method: Literal["POST", "GET"] = "POST"

    Request = DeleteGroupFileReq
    Response = DeleteGroupFileRes

    request: DeleteGroupFileReq
    response: DeleteGroupFileRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(DeleteGroupFileAPI)

# region code/

