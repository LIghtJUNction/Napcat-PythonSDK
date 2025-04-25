# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659182e0
@llms.txt: https://napcat.apifox.cn/226659182e0.md
@last_update: 2025-04-26 01:17:44

@description: 

summary:获取收藏列表

"""
__author__ = "LIghtJUNction"
__version__ = "4.7.17"
__endpoint__ = "get_collection_list"
__id__ = "226659182e0"
__method__ = "POST"

# endregion METADATA


# region code
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

# region req
class GetCollectionListReq(BaseModel):
    """
    请求体模型
    """
    category: str = Field(..., description="类别")
    count: str = Field(..., description="数量")
# endregion req



# region res
class GetCollectionListRes(BaseModel):
    """
    响应体模型
    """
    status: str = Field("ok", description="状态") # OpenAPI spec says const: ok
    retcode: int = Field(..., description="返回码")
    data: list[str] = Field(..., description="收藏列表数据")
    message: str = Field(..., description="消息")
    wording: str = Field(..., description="提示信息")
    echo: str | None = Field(None, description="echo字段") # Nullable field
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
