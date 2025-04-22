# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226659229e0
@endpoint: get_group_info_ex
@tags: 群聊相关
@homepage: https://napcat.apifox.cn/226659229e0
@llms.txt: https://napcat.apifox.cn/226659229e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: get_group_info_ex API
@usage: 使用 `client.get_group_info_ex()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_group_info_ex"
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
class GetGroupInfoExReq(BaseHttpRequest):
    """
    get_group_info_ex 请求参数
    """

    pass
# region req/

# region data
class GetGroupInfoExData(BaseModel):
    """
    get_group_info_ex 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGroupInfoExRes(BaseHttpResponse[GetGroupInfoExData]):
    """
    get_group_info_ex 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGroupInfoExAPI(BaseHttpAPI[GetGroupInfoExReq, GetGroupInfoExRes]):
    """
    获取群信息ex
    """
    api: str = "/get_group_info_ex"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGroupInfoExReq
    Response = GetGroupInfoExRes

    request: GetGroupInfoExReq
    response: GetGroupInfoExRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGroupInfoExAPI)

# region code/

