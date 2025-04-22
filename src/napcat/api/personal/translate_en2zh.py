# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 226659102e0
@endpoint: translate_en2zh
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226659102e0
@llms.txt: https://napcat.apifox.cn/226659102e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: translate_en2zh API
@usage: 使用 `client.translate_en2zh()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "translate_en2zh"
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
class TranslateEn2zhReq(BaseHttpRequest):
    """
    translate_en2zh 请求参数
    """

    pass
# region req/

# region data
class TranslateEn2zhData(BaseModel):
    """
    translate_en2zh 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class TranslateEn2zhRes(BaseHttpResponse[list[TranslateEn2zhData]]):
    """
    translate_en2zh 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class TranslateEn2zhAPI(BaseHttpAPI[TranslateEn2zhReq, TranslateEn2zhRes]):
    """
    英译中
    """
    api: str = "/translate_en2zh"
    method: Literal["POST", "GET"] = "POST"

    Request = TranslateEn2zhReq
    Response = TranslateEn2zhRes

    request: TranslateEn2zhReq
    response: TranslateEn2zhRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(TranslateEn2zhAPI)

# region code/

