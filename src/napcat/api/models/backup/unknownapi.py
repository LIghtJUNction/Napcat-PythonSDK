# -*- coding: utf-8 -*-# region METADATA
"""
@tags: 其他/接口
@homepage: https://napcat.apifox.cn/226658925e0
@llms.txt: https://napcat.apifox.cn/226658925e0.md
@last_update: 2025-04-26 01:17:44

@description: Represents the data models for the 'unknown' API endpoint.

summary: unknown

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "unknown"
__id__ = "226658925e0"
__method__ = "POST"

# endregion METADATA

# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class UnknownReq(BaseModel):
    """
    Request model for the unknown endpoint.
The OpenAPI spec defines no request body parameters.
    """
    pass
# endregion req


# region res
class UnknownRes(BaseModel):
    """
    Response model for the unknown endpoint.
The OpenAPI spec defines an empty response object.
    """
    pass
# endregion res

# region api
class UnknownAPI(BaseModel):
    """unknown接口数据模型"""
    endpoint: str = "unknown"
    method: str = "POST"
    Req: type[BaseModel] = UnknownReq
    Res: type[BaseModel] = UnknownRes
# endregion api

# endregion code