# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226659254e0
@endpoint: fetch_user_profile_like
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659254e0
@llms.txt: https://napcat.apifox.cn/226659254e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: fetch_user_profile_like API
@usage: 使用 `client.fetch_user_profile_like()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_user_profile_like"
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
class FetchUserProfileLikeReq(BaseHttpRequest):
    """
    fetch_user_profile_like 请求参数
    """

    pass
# region req/

# region data
class FetchUserProfileLikeData(BaseModel):
    """
    fetch_user_profile_like 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class FetchUserProfileLikeRes(BaseHttpResponse[FetchUserProfileLikeData]):
    """
    fetch_user_profile_like 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class FetchUserProfileLikeAPI(BaseHttpAPI[FetchUserProfileLikeReq, FetchUserProfileLikeRes]):
    """
    fetch_user_profile_like
    """
    api: str = "/fetch_user_profile_like"
    method: Literal["POST", "GET"] = "POST"

    Request = FetchUserProfileLikeReq
    Response = FetchUserProfileLikeRes

    request: FetchUserProfileLikeReq
    response: FetchUserProfileLikeRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(FetchUserProfileLikeAPI)

# region code/

