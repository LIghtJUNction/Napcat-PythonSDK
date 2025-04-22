# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 227233981e0
@endpoint: _get_model_show
@tags: 账号相关
@homepage: https://napcat.apifox.cn/227233981e0
@llms.txt: https://napcat.apifox.cn/227233981e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: _get_model_show API
@usage: 使用 `client._get_model_show()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "_get_model_show"
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
class GetModelShowReq(BaseHttpRequest):
    """
    _get_model_show 请求参数
    """

    pass
# region req/

# region data
class GetModelShowData(BaseModel):
    """
    _get_model_show 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetModelShowRes(BaseHttpResponse[list[GetModelShowData]]):
    """
    _get_model_show 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetModelShowAPI(BaseHttpAPI[GetModelShowReq, GetModelShowRes]):
    """
    _获取在线机型
    """
    api: str = "/_get_model_show"
    method: Literal["POST", "GET"] = "POST"

    Request = GetModelShowReq
    Response = GetModelShowRes

    request: GetModelShowReq
    response: GetModelShowRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetModelShowAPI)

# region code/

