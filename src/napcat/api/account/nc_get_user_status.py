# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 165
@api_id: 226659292e0
@endpoint: nc_get_user_status
@tags: 账号相关
@homepage: https://api.napcat.com/226659292e0
@llms.txt: https://api.napcat.com/226659292e0.md
@version: 4.7.17
@last_update: 2025-04-22 22:32:34

@description: nc_get_user_status API
@usage: 使用 `client.nc_get_user_status()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_user_status"
__method__ = "POST"


# region {
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest

    # 示例 endpoint : send_group_message  特殊 endpoint : _开头 .开头 给类命名时 .忽略即可(如 _get_model_show -> GetModelShowAPI)
    # 示例 class : SendGroupMessageAPI
    # 示例 request : SendGroupMessageReq
    # 示例 response : SendGroupMessageRes
    # 示例 data : SendGroupMessageData
    # 请将你需要展示给用户的注释符："#"放置于行首
    # 否则将被清理掉


# request model
class NcGetUserStatusReq(BaseHttpRequest):
    """
    nc_get_user_status 请求参数
    """

    pass


class NcGetUserStatusData(BaseModel):
    """
    nc_get_user_status 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# response model
class NcGetUserStatusRes(BaseHttpResponse[NcGetUserStatusData]):
    """
    nc_get_user_status 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass


# API class
class NcGetUserStatusAPI(BaseHttpAPI[NcGetUserStatusReq, NcGetUserStatusRes]):
    """
    获取用户状态
    """
    api: str = "/nc_get_user_status"
    method: Literal["POST", "GET"] = "POST"

    Request = NcGetUserStatusReq
    Response = NcGetUserStatusRes

    request: NcGetUserStatusReq
    response: NcGetUserStatusRes
    

if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(NcGetUserStatusAPI)

# region }

