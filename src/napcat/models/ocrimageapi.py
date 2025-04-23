# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226658234e0
@llms.txt: https://napcat.apifox.cn/226658234e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:.OCR 图片识别

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = ".ocr_image"
__id__ = "226658234e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class .ocrImageReq(BaseModel):
    """
    请求参数
    """

    image: str = Field(..., description="")
# region req/


# region res
class .ocrImageRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class .ocrImageAPI(BaseModel):
    
    Request : type[.ocrImageReq] = .ocrImageReq
    Response  : type[.ocrImageRes] = .ocrImageRes


# region api/
# region code/

