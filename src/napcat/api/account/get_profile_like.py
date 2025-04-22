# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659197e0
@endpoint: get_profile_like
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659197e0
@llms.txt: https://napcat.apifox.cn/226659197e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: get_profile_like API
@usage: 使用 `client.get_profile_like()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_profile_like"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class GetProfileLikeReq(BaseHttpRequest):
    """
    get_profile_like 请求参数
    """

    pass
# region req/

# region data
class GetProfileLikeData(BaseModel):
    """
    get_profile_like 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetProfileLikeRes(BaseHttpResponse[GetProfileLikeData]):
    """
    get_profile_like 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetProfileLikeAPI(BaseHttpAPI[GetProfileLikeReq, GetProfileLikeRes]):
    """
    获取点赞列表
    """
    api: str = "/get_profile_like"
    method: Literal["POST", "GET"] = "POST"

    Request = GetProfileLikeReq
    Response = GetProfileLikeRes

    request: GetProfileLikeReq
    response: GetProfileLikeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetProfileLikeAPI)

# region code/

