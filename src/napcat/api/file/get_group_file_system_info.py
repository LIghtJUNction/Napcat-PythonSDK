# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658789e0
@endpoint: get_group_file_system_info
@tags: 文件相关
@homepage: https://napcat.apifox.cn/226658789e0
@llms.txt: https://napcat.apifox.cn/226658789e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: get_group_file_system_info API
@usage: 使用 `client.get_group_file_system_info()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_file_system_info"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetGroupFileSystemInfoReq(BaseHttpRequest):
    """
    get_group_file_system_info 请求参数
    """

    pass
# region req/

# region data
class GetGroupFileSystemInfoData(BaseModel):
    """
    get_group_file_system_info 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupFileSystemInfoRes(BaseHttpResponse[GetGroupFileSystemInfoData]):
    """
    get_group_file_system_info 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupFileSystemInfoAPI(BaseHttpAPI[GetGroupFileSystemInfoReq, GetGroupFileSystemInfoRes]):
    """
    获取群文件系统信息
    """
    api: str = "/get_group_file_system_info"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupFileSystemInfoReq
    Response = GetGroupFileSystemInfoRes

    request: GetGroupFileSystemInfoReq
    response: GetGroupFileSystemInfoRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupFileSystemInfoAPI)

# region code/

