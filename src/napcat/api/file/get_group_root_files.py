# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658823e0
@endpoint: get_group_root_files
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658823e0
@llms.txt: https://napcat.apifox.cn/226658823e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_group_root_files API
@usage: 使用 `client.get_group_root_files()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_root_files"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetGroupRootFilesReq(BaseHttpRequest):
    """
    get_group_root_files 请求参数
    """

    pass
# region req/

# region data
class GetGroupRootFilesData(BaseModel):
    """
    get_group_root_files 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupRootFilesRes(BaseHttpResponse[GetGroupRootFilesData]):
    """
    get_group_root_files 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupRootFilesAPI(BaseHttpAPI[GetGroupRootFilesReq, GetGroupRootFilesRes]):
    """
    获取群根目录文件列表
    """
    api: str = "/get_group_root_files"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupRootFilesReq
    Response = GetGroupRootFilesRes

    request: GetGroupRootFilesReq
    response: GetGroupRootFilesRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupRootFilesAPI)

# region code/

