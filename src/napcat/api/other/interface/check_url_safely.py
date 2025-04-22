# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 228534361e0
@endpoint: check_url_safely
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/228534361e0
@llms.txt: https://napcat.apifox.cn/228534361e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: check_url_safely API
@usage: 使用 `client.check_url_safely()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "check_url_safely"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class CheckUrlSafelyReq(BaseHttpRequest):
    """
    check_url_safely 请求参数
    """

    pass
# region req/

# region data
class CheckUrlSafelyData(BaseModel):
    """
    check_url_safely 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class CheckUrlSafelyRes(BaseHttpResponse[CheckUrlSafelyData]):
    """
    check_url_safely 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class CheckUrlSafelyAPI(BaseHttpAPI[CheckUrlSafelyReq, CheckUrlSafelyRes]):
    """
    检查链接安全性
    """
    api: str = "/check_url_safely"
    method: Literal["POST", "GET"] = "POST"

    Request = CheckUrlSafelyReq
    Response = CheckUrlSafelyRes

    request: CheckUrlSafelyReq
    response: CheckUrlSafelyRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(CheckUrlSafelyAPI)

# region code/

