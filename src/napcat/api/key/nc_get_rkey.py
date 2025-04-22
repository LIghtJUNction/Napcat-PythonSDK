# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659297e0
@endpoint: nc_get_rkey
@tags: 密钥相关
@homepage: https://napcat.apifox.cn/226659297e0
@llms.txt: https://napcat.apifox.cn/226659297e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: nc_get_rkey API
@usage: 使用 `client.nc_get_rkey()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "nc_get_rkey"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class NcGetRkeyReq(BaseHttpRequest):
    """
    nc_get_rkey 请求参数
    """

    pass
# region req/

# region data
class NcGetRkeyData(BaseModel):
    """
    nc_get_rkey 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class NcGetRkeyRes(BaseHttpResponse[list[NcGetRkeyData]]):
    """
    nc_get_rkey 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class NcGetRkeyAPI(BaseHttpAPI[NcGetRkeyReq, NcGetRkeyRes]):
    """
    nc获取rkey
    """
    api: str = "/nc_get_rkey"
    method: Literal["POST", "GET"] = "POST"

    Request = NcGetRkeyReq
    Response = NcGetRkeyRes

    request: NcGetRkeyReq
    response: NcGetRkeyRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(NcGetRkeyAPI)

# region code/

