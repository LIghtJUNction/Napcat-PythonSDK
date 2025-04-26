# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: {{tags}}
@homepage: https://napcat.apifox.cn/226659102e0
@llms.txt: https://napcat.apifox.cn/226659102e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:英译中

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "translate_en2zh"
__id__ = "226659102e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from typing import Literal
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class TranslateEn2zhReq(BaseModel):
    """
    英译中请求模型
    """
    words: list[str] = Field(..., description="英文数组")
# endregion req



# region res
class TranslateEn2zhRes(BaseModel):
    """
    英译中响应模型
    """
    status: Literal["ok"] = Field(..., description="响应状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[str] = Field(..., description="翻译结果数组")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="Echo字段")
# endregion res

# region api
class TranslateEn2zhAPI(BaseModel):
    """translate_en2zh接口数据模型"""
    endpoint: str = "translate_en2zh"
    method: str = "POST"
    Req: type[BaseModel] = TranslateEn2zhReq
    Res: type[BaseModel] = TranslateEn2zhRes
# endregion api




# endregion code
