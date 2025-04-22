# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658965e0
@endpoint: ArkSharePeer
@tags: 账号相关
@homepage: https://napcat.apifox.cn/226658965e0
@llms.txt: https://napcat.apifox.cn/226658965e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:50

@description: ArkSharePeer API
@usage: 使用 `client.ArkSharePeer()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "ArkSharePeer"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class ArksharepeerReq(BaseHttpRequest):
    """
    ArkSharePeer 请求参数
    """

    pass
# region req/

# region data
class ArksharepeerData(BaseModel):
    """
    ArkSharePeer 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class ArksharepeerRes(BaseHttpResponse[ArksharepeerData]):
    """
    ArkSharePeer 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class ArksharepeerAPI(BaseHttpAPI[ArksharepeerReq, ArksharepeerRes]):
    """
    获取推荐好友/群聊卡片
    """
    api: str = "/ArkSharePeer"
    method: Literal["POST", "GET"] = "POST"

    Request = ArksharepeerReq
    Response = ArksharepeerRes

    request: ArksharepeerReq
    response: ArksharepeerRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(ArksharepeerAPI)

# region code/

