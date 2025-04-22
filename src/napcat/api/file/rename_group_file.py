# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 283136375e0
@endpoint: rename_group_file
@tags: 文件相关
@homepage: https://napcat.apifox.cn/283136375e0
@llms.txt: https://napcat.apifox.cn/283136375e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: rename_group_file API
@usage: 使用 `client.rename_group_file()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "rename_group_file"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class RenameGroupFileReq(BaseHttpRequest):
    """
    rename_group_file 请求参数
    """

    pass
# region req/

# region data
class RenameGroupFileData(BaseModel):
    """
    rename_group_file 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class RenameGroupFileRes(BaseHttpResponse[RenameGroupFileData]):
    """
    rename_group_file 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class RenameGroupFileAPI(BaseHttpAPI[RenameGroupFileReq, RenameGroupFileRes]):
    """
    重命名群文件
    """
    api: str = "/rename_group_file"
    method: Literal["POST", "GET"] = "POST"

    Request = RenameGroupFileReq
    Response = RenameGroupFileRes

    request: RenameGroupFileReq
    response: RenameGroupFileRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(RenameGroupFileAPI)

# region code/

