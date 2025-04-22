# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 213
@api_id: 228534368e0
@endpoint: .get_word_slices
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/228534368e0
@llms.txt: https://napcat.apifox.cn/228534368e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:35:54

@description: .get_word_slices API
@usage: 使用 `client..get_word_slices()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".get_word_slices"
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
class GetWordSlicesReq(BaseHttpRequest):
    """
    .get_word_slices 请求参数
    """

    pass
# region req/

# region data
class GetWordSlicesData(BaseModel):
    """
    .get_word_slices 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class GetWordSlicesRes(BaseHttpResponse[GetWordSlicesData]):
    """
    .get_word_slices 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class GetWordSlicesAPI(BaseHttpAPI[GetWordSlicesReq, GetWordSlicesRes]):
    """
    获取中文分词
    """
    api: str = "/.get_word_slices"
    method: Literal["POST", "GET"] = "POST"

    Request = GetWordSlicesReq
    Response = GetWordSlicesRes

    request: GetWordSlicesReq
    response: GetWordSlicesRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(GetWordSlicesAPI)

# region code/

