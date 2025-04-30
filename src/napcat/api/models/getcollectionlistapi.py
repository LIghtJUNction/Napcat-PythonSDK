# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659182e0
@llms.txt: https://napcat.apifox.cn/226659182e0.md
@last_update: 2025-04-27 00:53:40

@description: 

summary:获取收藏列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.43"
__endpoint__ = "get_collection_list"
__id__ = "226659182e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field
from typing import Literal

logger = logging.getLogger(__name__)

# region req
class GetCollectionListReq(BaseModel):
    """
    获取收藏列表请求模型
    """
    category: str = Field(..., description="收藏类别")
    count: str = Field(..., description="数量") # Note: OpenAPI spec says string for count, which might be unusual.
# endregion req



# region res
class GetCollectionListRes(BaseModel):
    """
    获取收藏列表响应模型
    """
    status: Literal["ok"] = Field("ok", description="状态码，固定为 'ok'")
    retcode: int = Field(..., description="返回码")
    data: list[str] = Field(..., description="收藏列表数据，元素为字符串")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="补充说明")
    echo: str | None = Field(..., description="回显信息")
# endregion res

# region api
class GetCollectionListAPI(BaseModel):
    """get_collection_list接口数据模型"""
    endpoint: str = "get_collection_list"
    method: str = "POST"
    Req: type[BaseModel] = GetCollectionListReq
    Res: type[BaseModel] = GetCollectionListRes
# endregion api




# endregion code