# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659292e0
@endpoint: nc_get_user_status
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659292e0
@llms.txt: https://napcat.apifox.cn/226659292e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: nc_get_user_status API
@usage: 使用 `client.nc_get_user_status()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_user_status"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class NcGetUserStatusReq(BaseHttpRequest):
    """
    nc_get_user_status 请求参数
    """

    pass
# region req/

# region data
class NcGetUserStatusData(BaseModel):
    """
    nc_get_user_status 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class NcGetUserStatusRes(BaseHttpResponse[NcGetUserStatusData]):
    """
    nc_get_user_status 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
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
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(NcGetUserStatusAPI)

# region code/

