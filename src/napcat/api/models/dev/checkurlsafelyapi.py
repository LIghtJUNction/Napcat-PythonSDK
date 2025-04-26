# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/228534361e0
@llms.txt: https://napcat.apifox.cn/228534361e0.md
@last_update: 2025-04-27 00:53:41

@description:

summary:检查链接安全性

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "check_url_safely"
__id__ = "228534361e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal # Import Literal

logger = logging.getLogger(__name__)

# region req
class CheckUrlSafelyReq(BaseModel):
    """
    检查链接安全性请求模型
    """
    # OpenAPI spec shows no request body.
    pass
# endregion req



# region res
class CheckUrlSafelyRes(BaseModel):
    """
    检查链接安全性响应模型
    """
    # OpenAPI spec shows an empty response object (properties: {}).
    # Adding common response fields based on user instructions to add descriptions, defaults, and handle status.
    status: Literal["ok"] = Field(default="ok", description="响应状态")
    message: str = Field(default="success", description="响应消息")

# endregion res

# region api
class CheckUrlSafelyAPI(BaseModel):
    """check_url_safely接口数据模型"""
    endpoint: str = "check_url_safely"
    method: str = "POST"
    Req: type[BaseModel] = CheckUrlSafelyReq
    Res: type[BaseModel] = CheckUrlSafelyRes
# endregion api




# endregion code
