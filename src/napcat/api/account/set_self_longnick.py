# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226659186e0
@endpoint: set_self_longnick
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659186e0
@llms.txt: https://napcat.apifox.cn/226659186e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:53

@description: set_self_longnick API
@usage: 使用 `client.set_self_longnick()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "set_self_longnick"
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
class SetSelfLongnickReq(BaseHttpRequest):
    """
    set_self_longnick 请求参数
    """

    pass
# region req/

# region data
class SetSelfLongnickData(BaseModel):
    """
    set_self_longnick 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class SetSelfLongnickRes(BaseHttpResponse[SetSelfLongnickData]):
    """
    set_self_longnick 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class SetSelfLongnickAPI(BaseHttpAPI[SetSelfLongnickReq, SetSelfLongnickRes]):
    """
    设置个性签名
    """
    api: str = "/set_self_longnick"
    method: Literal["POST", "GET"] = "POST"

    Request = SetSelfLongnickReq
    Response = SetSelfLongnickRes

    request: SetSelfLongnickReq
    response: SetSelfLongnickRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(SetSelfLongnickAPI)

# region code/

