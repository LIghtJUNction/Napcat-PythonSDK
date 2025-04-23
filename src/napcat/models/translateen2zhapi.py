# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659102e0
@llms.txt: https://napcat.apifox.cn/226659102e0.md
@last_update: 2025-04-23 20:23:17

@description: 

summary:英译中

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "translate_en2zh"
__id__ = "226659102e0"
__method__ = "POST"

# region METADATA/


# region code
from typing import Any
from pydantic import BaseModel, Field

# region req
class TranslateEn2zhReq(BaseModel):
    """
    请求参数
    """

    words: list[str] = Field(..., description="英文数组")
# region req/


# region res
class TranslateEn2zhRes(BaseModel):
    """
    响应参数
    """

    pass
# region res/

# region api
class TranslateEn2zhAPI(BaseModel):
    
    Request : type[TranslateEn2zhReq] = TranslateEn2zhReq
    Response  : type[TranslateEn2zhRes] = TranslateEn2zhRes


# region api/
# region code/

