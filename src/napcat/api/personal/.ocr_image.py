# -*- coding: utf-8 -*-
"""
@author: LIghtJUNction
@builder: AI

@build_id: 214
@api_id: 226658234e0
@endpoint: .ocr_image
@tags: 个人操作
@homepage: https://napcat.apifox.cn/226658234e0
@llms.txt: https://napcat.apifox.cn/226658234e0.md
@version: 4.7.17
@last_update: 2025-04-23 04:39:51

@description: .ocr_image API
@usage: 使用 `client..ocr_image()` 调用此API

"""
# region METADATA

__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".ocr_image"
__method__ = "POST"


# region code
from typing import Literal, Any

from pydantic import BaseModel, Field
from napcat.base.models import BaseHttpAPI, BaseHttpResponse, BaseHttpRequest



# region req
class OcrImageReq(BaseHttpRequest):
    """
    .ocr_image 请求参数
    """

    pass
# region req/

# region data
class OcrImageData(BaseModel):
    """
    .ocr_image 数据结构
    """
    # 定义可选数据字段
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region data/

# region res
class OcrImageRes(BaseHttpResponse[list[OcrImageData]]):
    """
    .ocr_image 响应参数
    """
    # 定义响应参数
    # 例如：
    # param1: str = Field(..., description="参数1的描述")
    # param2: int = Field(..., description="参数2的描述")
    
    pass
# region res/

# region api
class OcrImageAPI(BaseHttpAPI[OcrImageReq, OcrImageRes]):
    """
    .OCR 图片识别
    """
    api: str = "/.ocr_image"
    method: Literal["POST", "GET"] = "POST"

    Request = OcrImageReq
    Response = OcrImageRes

    request: OcrImageReq
    response: OcrImageRes
# region api/


if __name__ == "__main__":

    from napcat.base.utils import test_model
    test_model(OcrImageAPI)

# region code/

