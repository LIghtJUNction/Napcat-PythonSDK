# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226659210e0
@endpoint: fetch_custom_face
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226659210e0
@llms.txt: https://napcat.apifox.cn/226659210e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: fetch_custom_face API
@usage: 使用 `client.fetch_custom_face()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "fetch_custom_face"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class FetchCustomFaceReq(BaseHttpRequest):
    """
    fetch_custom_face 请求参数
    """

    pass
# region req/

# region data
class FetchCustomFaceData(BaseModel):
    """
    fetch_custom_face 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class FetchCustomFaceRes(BaseHttpResponse[list[FetchCustomFaceData]]):
    """
    fetch_custom_face 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class FetchCustomFaceAPI(BaseHttpAPI[FetchCustomFaceReq, FetchCustomFaceRes]):
    """
    获取收藏表情
    """
    api: str = "/fetch_custom_face"
    method: Literal["POST", "GET"] = "POST"

    Request = FetchCustomFaceReq
    Response = FetchCustomFaceRes

    request: FetchCustomFaceReq
    response: FetchCustomFaceRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(FetchCustomFaceAPI)

# region code/

