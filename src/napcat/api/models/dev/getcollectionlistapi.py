# -*- coding: utf-8 -*-
# region METADATA
"""
@tags: 其他/bug
@homepage: https://napcat.apifox.cn/226659182e0
@llms.txt: https://napcat.apifox.cn/226659182e0.md
@last_update: 2025-05-28 01:34:10

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
from pydantic import BaseModel, Field
from typing import Literal, Any
import logging

logger = logging.getLogger(__name__)

# region component_models
class Result(BaseModel):
    status: Literal["ok"] = Field("ok", description="状态字段，固定为'ok'")
    retcode: float = Field(..., description="返回码字段")
    data: dict[str, Any] = Field(..., description="数据字段（通用对象）")
    message: str = Field(..., description="消息字段")
    wording: str = Field(..., description="文案字段")
    echo: str | None = Field(None, description="回显字段")

    model_config = {
        "extra": "allow",
    }
# region component_models/

# region req
class GetCollectionListReq(BaseModel):
    """获取收藏列表请求模型"""
    category: str = Field(..., description="收藏分类")
    count: str = Field(..., description="收藏数量")

    model_config = {
        "extra": "allow",
    }
# region req/


# region res
class GetCollectionListRes(BaseModel):
    """获取收藏列表响应模型"""
    status: Literal["ok"] = Field("ok", description="响应状态，固定为'ok'")
    retcode: float = Field(0.0, description="响应返回码")
    data: list[str] = Field(default_factory=list, description="收藏列表数据，每个元素为字符串")
    message: str = Field("", description="响应消息")
    wording: str = Field("", description="响应文案")
    echo: str | None = Field(None, description="回显字段")

    model_config = {
        "extra": "allow",
    }
# region res/

# region api
class GetCollectionListAPI(BaseModel):
    """get_collection_list接口数据模型"""
    endpoint: str = "get_collection_list"
    method: str = "POST"
    Req: type[BaseModel] = GetCollectionListReq
    Res: type[BaseModel] = GetCollectionListRes

# region api/
# endregion code
