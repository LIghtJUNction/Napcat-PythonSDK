# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226659317e0
@endpoint: get_guild_service_profile
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/226659317e0
@llms.txt: https://napcat.apifox.cn/226659317e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: get_guild_service_profile API
@usage: 使用 `client.get_guild_service_profile()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_guild_service_profile"
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
class GetGuildServiceProfileReq(BaseHttpRequest):
    """
    get_guild_service_profile 请求参数
    """

    pass
# region req/

# region data
class GetGuildServiceProfileData(BaseModel):
    """
    get_guild_service_profile 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetGuildServiceProfileRes(BaseHttpResponse[GetGuildServiceProfileData]):
    """
    get_guild_service_profile 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetGuildServiceProfileAPI(BaseHttpAPI[GetGuildServiceProfileReq, GetGuildServiceProfileRes]):
    """
    get_guild_service_profile
    """
    api: str = "/get_guild_service_profile"
    method: Literal["POST", "GET"] = "POST"

    Request = GetGuildServiceProfileReq
    Response = GetGuildServiceProfileRes

    request: GetGuildServiceProfileReq
    response: GetGuildServiceProfileRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetGuildServiceProfileAPI)

# region code/

